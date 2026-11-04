"""Split a library file's translatable strings into small chunks and merge translated chunks back.

Large library files are too big to rewrite in one response. This tool lets a translator work on
small chunks of strings and rebuilds the full JSON mechanically, so structure can never drift.

    python3 translation_chunks.py extract <language> <file.json> [--force]
    python3 translation_chunks.py status  <language> <file.json>
    python3 translation_chunks.py apply   <language> <file.json>

`extract` writes translation-work/<language>/<stem>/chunk-NNN.json ({"<path>": "<English>"}).
The translator writes chunk-NNN.translated.json beside each one (same keys, translated values).
`apply` merges every translated chunk into the English file and saves
community-examples/<language>/<file.json>. Validate the result with validate_translations.py.
"""

import json
import sys
from pathlib import Path

from validate_translations import EXAMPLES, LANGUAGES, ROOT, is_prose_path

WORK = ROOT / "translation-work"
MAX_STRINGS = 60
MAX_CHARS = 12000


def strings(node, path=()):
    """Yield (path, text) for every translatable string, in document order."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield from strings(value, (*path, key))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from strings(value, (*path, index))
    elif isinstance(node, str) and is_prose_path(path) and node.strip():
        yield path, node


def chunks(items):
    current, size = [], 0
    for path, text in items:
        if current and (len(current) >= MAX_STRINGS or size + len(text) > MAX_CHARS):
            yield current
            current, size = [], 0
        current.append((path, text))
        size += len(text)
    if current:
        yield current


def setup(argv):
    argv = [a for a in argv if a != "--force"]
    if len(argv) != 2 or argv[0] not in LANGUAGES:
        raise ValueError(f"usage: <{'|'.join(LANGUAGES)}> <file.json>")
    language, name = argv[0], Path(argv[1]).name
    source = EXAMPLES / "english" / name
    if not source.is_file():
        raise ValueError(f"{source}: no English original")
    return language, name, source, WORK / language / Path(name).stem


def pending(work):
    """Chunk files that have no translated counterpart yet, plus the total chunk count."""
    originals = sorted(work.glob("chunk-[0-9][0-9][0-9].json"))
    todo = [o for o in originals if not o.with_name(o.stem + ".translated.json").is_file()]
    return todo, len(originals)


def status(argv):
    language, name, source, work = setup(argv)
    todo, total = pending(work)
    if not total:
        raise ValueError(f"{work}: no chunks; run extract first")
    if todo:
        print(f"{total - len(todo)} of {total} chunks translated; {len(todo)} remaining.")
        print(f"NOT DONE. Next: {todo[0]} -> write {todo[0].stem}.translated.json")
    else:
        print(f"All {total} chunks translated. Now run apply, then validate_translations.py.")


def extract(argv):
    language, name, source, work = setup(argv)
    if "--force" not in argv and any(work.glob("chunk-*.json")):
        print("Chunks already exist; keeping your translated work. Use --force only to start over.")
        status(argv)
        return
    work.mkdir(parents=True, exist_ok=True)
    for old in work.glob("chunk-*.json"):
        old.unlink()
    items = list(strings(json.loads(source.read_text())))
    parts = list(chunks(items))
    for number, part in enumerate(parts, 1):
        data = {json.dumps(list(path)): text for path, text in part}
        (work / f"chunk-{number:03d}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n"
        )
    print(f"{len(items)} strings in {len(parts)} chunks: {work}")
    print("Translate each chunk-NNN.json into chunk-NNN.translated.json (same keys). "
          "Run `status` after each chunk until none remain, then run apply.")


def apply(argv):
    language, name, source, work = setup(argv)
    originals = sorted(work.glob("chunk-[0-9][0-9][0-9].json"))
    if not originals:
        raise ValueError(f"{work}: no chunks; run extract first")
    document = json.loads(source.read_text())
    replacements = {}
    for original in originals:
        translated = original.with_name(original.stem + ".translated.json")
        if not translated.is_file():
            raise ValueError(f"{translated}: missing; translate this chunk")
        left = json.loads(original.read_text())
        right = json.loads(translated.read_text())
        if left.keys() != right.keys():
            missing = sorted(left.keys() - right.keys())[:3]
            extra = sorted(right.keys() - left.keys())[:3]
            raise ValueError(f"{translated}: keys differ (missing {missing}, extra {extra})")
        replacements.update(right)
    for key, text in replacements.items():
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"{key}: translation must be a non-empty string")
        node = document
        *parents, last = json.loads(key)
        for part in parents:
            node = node[part]
        node[last] = text
    target = EXAMPLES / language / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {target} ({len(replacements)} strings merged). Now run validate_translations.py.")


if __name__ == "__main__":
    commands = {"extract": extract, "status": status, "apply": apply}
    try:
        if len(sys.argv) < 2 or sys.argv[1] not in commands:
            raise ValueError(__doc__)
        commands[sys.argv[1]](sys.argv[2:])
    except (OSError, ValueError, KeyError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
