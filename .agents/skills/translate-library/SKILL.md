---
name: translate-library
description: Translate Protocol Wizard product library JSON files from English into the supported community languages (japanese, simplified-chinese, german, french, korean, spanish, brazilian-portuguese). Use when asked to translate, add, or fix a file under community-examples/<language>/.
---

# Translate library JSON

Translate prose in `community-examples/english/<file>.json` into
`community-examples/<language>/<same file name>`. Paths are relative to the repository root
(the folder containing `validate_translations.py`).

## Scope and completion (read this first)

- **Scope is exactly what the user asked for**: the named file(s) in the named language(s). If they
  name one file and one language, do that one pair. Do not expand to other files or languages, and
  do not stop to report that other files/languages remain.
- **Finish the whole file.** Every translatable string (see below) must be translated, including
  long `notes`, `evidenceNotes`, `condition`, `rows` and `aliases`. A file with prose left in English
  is not done. The validator fails on it.
- **Write the result in place** at `community-examples/<language>/<filename>`. Never save a draft
  elsewhere (temp folders, `-INCOMPLETE` names) and never stop with a partial file.
- **Do not stop to ask or to caveat.** You do not need a native-speaker review, and you should not
  report that the translation is unreviewed. Translate everything, run the validator, fix errors,
  and finish. Only list strings you deliberately kept in English for a rule below (names, units).
- The validator checks structure, numbers, units and untranslated prose. It cannot judge
  accuracy, so translate carefully; but accuracy concerns never justify leaving text in English.
- **Language of your replies: English**, whatever the target language. Only the translated file
  content is in the target language.

## Workflow

Library files are large (the 5-amino-1mq file is ~84 KB). Never try to write the whole translated
JSON by hand in one response, or retype it: that is why earlier attempts stopped. Use the chunk
tool, which splits the prose into small pieces and rebuilds the JSON mechanically.
Run everything from the repository root.

1. Extract the chunks (language folder name, then English file name):
   ```bash
   .venv/bin/python3 translation_chunks.py extract brazilian-portuguese 5-amino-1mq.json
   ```
   This creates `translation-work/<language>/<stem>/chunk-001.json`, `chunk-002.json`, ... Each is
   a small JSON object `{"<path>": "<English text>"}`.
   Running `extract` again keeps existing translated chunks (use `--force` only to start over).
2. **Loop until no chunks remain. This is the main job, and one chunk is never the end.**
   - Run `.venv/bin/python3 translation_chunks.py status <language> <file.json>`. It names the next chunk
     and says `NOT DONE` while any remain.
   - Read that `chunk-NNN.json`, then write `chunk-NNN.translated.json` beside it: the **same
     keys exactly**, each value translated per the rules below. Copy names that must stay English
     unchanged.
   - Immediately run `status` again and continue with the next chunk. Repeat for every chunk
     (about 11 for a large file). Do not report to the user, summarize, or ask whether to continue
     while `status` says `NOT DONE`. Reporting "N chunks remain" instead of translating them is a
     failure of the task.
   - If you are interrupted or resumed, run `status` and carry on from where it says.
3. Merge into the final file (this is the only way the final file is produced; never edit it by
   hand):
   ```bash
   .venv/bin/python3 translation_chunks.py apply brazilian-portuguese 5-amino-1mq.json
   ```
   It lists any missing chunk or key mismatch; fix and rerun.
4. Run the validator, naming the language and file(s) you wrote:
   ```bash
   .venv/bin/python3 validate_translations.py brazilian-portuguese 5-amino-1mq.json
   ```
   (uses the project's `.venv`, which already has `jsonschema`; do not install packages or
   point `PYTHONPATH` elsewhere). It fails if the file is missing, so success means your file
   exists and passed. Fix every reported error and rerun until it passes. Do not edit the validator
   to make a file pass. It lists the paths still in English; translate those.
   Output saying "Validated 0" means nothing was checked and the task is NOT done.
5. Delete `translation-work/<language>/<stem>/` once the validator passes.
6. Report in English, in a few lines: the file written and the validator result.

## What to translate

Translate only string values under these keys (the list lives in `TEXT_FIELDS` in
`validate_translations.py`; that file is authoritative):

`name`, `title`, `purpose`, `benefits`, `evidenceNotes`, `evidenceNote`, `notes`, `note`,
`condition`, `excerpt`, `label`, `section`, `subsection`, `description`;
plus `population` inside `regimen`, string cells under `rows`, and strings under `aliases`.

**Keep in English, never translate:** `sources[].title`, `sources[].publisher`, and
`citations[].locator`. Readers use them to find the published material, so they stay exactly as in
the English file (the chunk tool leaves them out, and the validator rejects any change).
`protocols[].title` and product `name` are still translated.

Everything else must stay byte-identical to the original: all keys, key order, array lengths,
ids and cross-references (`id`, `productID`, `protocolID`, `sourceID`, `categoryID`), enums
(`methodID`, `kind`, `identityStatus`), `type`, `url`, `publishedAt`, `supports`, versions, `$schema`,
booleans, nulls, and structured dose fields (`value`, `unit`, ...).

`regimen` allows extra keys. If you find prose under a key not in the list above, do not
translate it; list the key path in your report so the list can be extended.

## Hard rules for text you translate

- **Numbers:** keep every number exactly, with ASCII digits and a `.` decimal point in every
  language (`0.25`, never `0,25` or fullwidth digits). Do not add, drop, or spell out numbers.
- **Units:** keep `mcg`, `µg`, `mg`, `kg`, `mL`, `IU` and `U-100`-style labels verbatim next to their
  numbers. Do not rewrite them in the target language.
- **Names:** keep peptide, compound, and brand names in English. In `aliases` you may add a
  common transliteration or local name as an extra value only if the array length is unchanged
  (replace an alias, do not append).
- **Meaning and severity:** warnings, cautions, contraindications and limits keep their exact
  strength. "may", "should", "must", "do not" must not be softened or strengthened.
- **No new claims:** never add, remove, or reword facts, citations, or study details.
- **Format:** UTF-8, non-ASCII written literally (no `\uXXXX`), same indentation as the original,
  trailing newline. Keep any `\n`, HTML, Markdown, and placeholders such as `%@`, `%d`, `{name}`
  untouched.

## Glossary (use one term consistently across every file in a language)

Keep a consistent rendering for: protocol, phase, vial, reconstitution, titration, cycle, off
period, maintenance, subcutaneous, intramuscular, intranasal, oral, topical. Before starting a
language, grep an existing file in `community-examples/<language>/` and reuse its terms.

## Language notes

- **japanese:** polite です/ます. Omit pronouns where implied. Use 「」 for quotation marks inside
  the text only; never change JSON delimiters.
- **simplified-chinese:** mainland terminology, full-width punctuation. Do not use Traditional characters.
- **german:** formal "Sie". Prefer compact wording for short labels (`name`, `label`, `title`).
- **french:** correct gender/number agreement. Put a no-break space (U+00A0) before `:`, `;`, `!`, `?`.
- **korean:** polite 해요체 throughout. Do not translate subject pronouns literally.
- **spanish:** neutral Latin American Spanish, "usted"/impersonal forms, no "vosotros".
- **brazilian-portuguese:** Brazilian vocabulary and syntax; avoid European Portuguese forms.

## Adding a new language

Add its folder name to `LANGUAGES` in `validate_translations.py`, create the folder, and add a
language note above.
