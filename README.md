# Protocol Wizard library authoring

Create optional JSON reference libraries for Protocol Wizard, a personal protocol tracker for supplements, bio-optimization, and wellness logging. Libraries supply reusable reference content. Importing one does not start a protocol, schedule doses, or replace personal records.

## Files

- `template/library.schema.json` — the complete JSON Schema for library format 1, including required fields, types, choices, and optional reference metadata.
- [Generated schema reference](docs/schema/library.md) — field types, required attributes, supported values, and constraints, generated with Adobe's `jsonschema2md`.
- `community-examples/<product-id>.json` — 52 individual product libraries containing 107 supported approved protocols in total. Each file contains exactly one product and all of its supported protocols, with the sources, citations, category, and delivery methods they use. Unsupported structured delivery methods or dose units are omitted without converting quantities or changing the authoring database.

Create your own product files with the [schema](template/library.schema.json), or start with the [community examples](community-examples/README.md). Download the individual JSON files you want to import into Protocol Wizard.

## Import a library

1. Save the library as a UTF-8 `.json` file containing one JSON object, without comments or trailing commas.
2. In Protocol Wizard, open **Library → Import library → Choose library JSON file**.
3. Select the file in Files. The app validates its structure, choices, unique IDs, and references before displaying a preview.
4. Review the product and check the protocols you want. Nothing is selected initially. **Select All** chooses eligible protocols; **Clear** resets the selection.
5. Choose **Import selected protocols**. The product is included automatically. If existing entries would change, review the replacement list and choose **Replace & Import**, or **Cancel** to keep the installed content.

Imports add to the installed reference library. Products and selected protocols match by stable ID: new IDs are added, changed matching IDs require confirmation, and identical entries stay unchanged. Protocol IDs cannot move between products. Unchecked protocols, entries absent from the file, and other products are retained. Supporting source/category/method changes are included in the replacement warning. Cancelling the warning preserves the selection so you can adjust it.

Personal products, templates, active protocols, calculations, source snapshots, and history stay unchanged. Files work offline. Importing a local file disconnects automatic updates only for that product; other products keep their connected URLs. The app retains the reviewed bytes, so changing the original file after review does not change what gets installed. Validation, download, cancellation, or save failures leave installed content unchanged.

The JSON file must be between 1 byte and 10,000,000 bytes. It is a library catalog, not a personal backup, schema document, ZIP archive, or web page.

## Start with this small library

The values below are fictional format examples. Replace them with your own content and sources.

```json
{
  "schemaVersion": 1,
  "catalogVersion": 1,
  "items": [{
    "id": "example-supplement",
    "name": "Example supplement",
    "aliases": [],
    "kind": "product",
    "identityStatus": "resolved",
    "categoryID": 1,
    "benefits": null
  }],
  "protocols": [{
    "id": "example-daily-routine",
    "productID": "example-supplement",
    "title": "Example daily routine",
    "purpose": "Fictional authoring example",
    "methodID": "oral",
    "population": "",
    "evidenceNotes": null,
    "regimen": {
      "version": 1,
      "regimen_type": "single_compound",
      "phases": [{
        "name": "Daily routine",
        "duration": {"kind": "ongoing", "value": null, "unit": "day"},
        "dose": {"value": "1", "unit": "capsule", "basis": "per_administration"},
        "schedule": {"pattern": "daily", "doses_per_day": 1, "suggested_times": ["09:00"]}
      }]
    }
  }],
  "sources": [],
  "citations": [],
  "categories": [{"id": 1, "name": "Daily supplements"}],
  "methods": [{"id": "oral", "name": "Oral"}]
}
```

## Root attributes

Every row below is required. `items` contains exactly one product, `protocols` contains at least one protocol, and each protocol's `regimen.phases` contains at least one phase. Other root arrays may be empty. Unknown attributes are rejected at the root and on products, protocols, sources, citations, categories, and methods. An optional root `$schema` string may point your editor to `template/library.schema.json`; the app always uses its own bundled schema and does not download that URL.

| Attribute | JSON type | Rule |
| --- | --- | --- |
| `schemaVersion` | integer | Exactly `1`; identifies the file format. |
| `catalogVersion` | integer | Exactly `1` during development. |
| `items` | array of product objects | Exactly one product identity. |
| `protocols` | array of protocol objects | All reference routines for this product; every `productID` equals `items[0].id`. |
| `sources` | array of source objects | Bibliographic entries used by citations. |
| `citations` | array of citation objects | Source links supporting a product or protocol. |
| `categories` | array of category objects | Product grouping labels. |
| `methods` | array of method objects | Delivery method IDs and labels. |

Keep `schemaVersion`, `catalogVersion`, and every regimen `version` at `1` during development. Content updates are detected using the payload's SHA-256 digest rather than increasing a version. New imports use the documented field names and supported app choices.

## Product attributes (`items[]`)

| Attribute | Required | Type and choices |
| --- | --- | --- |
| `id` | Yes | Nonblank string; unique within `items`. Keep it stable between releases. |
| `name` | Yes | Nonblank string. |
| `aliases` | Yes | Array of strings; use `[]` when there are none. |
| `kind` | Yes | `product`, `blend`, `other`, or `unresolved`. |
| `identityStatus` | Yes | `resolved` or `needs_confirmation`. |
| `categoryID` | No | Integer referring to `categories[].id`, or `null`. |
| `benefits` | No | String or `null`. |
| `timing` | No | Timing guidance object or `null`; see below. |

### Optional timing guidance

All timing fields are optional. Unknown keys are rejected, and a note must be nonblank when present. The app enforces its 500-character limit.

| Property | Title | Description |
| --- | --- | --- |
| `timing` | Timing guidance | Optional dose-timing guidance for this product. The app shows it as a recommendation on the Schedule step and never applies it automatically. |
| `timing.tags` | Timing tags | Any of: morning, midday, evening, bedtime, empty_stomach, with_food, before_exercise, after_exercise. Unknown tags are ignored. |
| `timing.window` | Suggested window | 24-hour HH:mm start and end. The end may be earlier than the start, meaning the window crosses midnight. |
| `timing.window.start` | Window start | Required when a window is present. |
| `timing.window.end` | Window end | Required when a window is present. |
| `timing.note` | Timing note | Shown under the recommendation. Up to 500 characters. |

```json
"timing": {
  "tags": ["bedtime", "empty_stomach"],
  "window": { "start": "21:00", "end": "23:00" },
  "note": "At least 2 hours after your last meal."
}
```

Matching template `suggested_times` take precedence over the window. Otherwise, the Schedule step offers times spread across the window and rounded to 15 minutes; one daily dose uses its midpoint. Tags alone provide text guidance. Recommendations require the user's explicit choice.

### Numbers in prose

Write library text in English. Any quantity inside prose uses the same format as dose amounts: a **dot decimal** with no grouping separators. For example, write `0.25 mg`, `0.250 mg` or `1500 mcg`. Never write `0,25 mg` or `1,500 mcg`. This applies to:

- `timing.note`
- phase `condition` and `conditions` text, and regimen `conditional_escalation` text, which the app shows as a check-in's source condition

The app shows this text as written. It reads the numbers aloud for VoiceOver in this format on every device, whatever the user's region. That means a dot is always a decimal point, so `0.250 mg` is read as "zero point two five zero milligrams" in every region, and not as 250 on a device that groups thousands with a dot. A comma in a quantity is therefore ambiguous and must not be used. JSON Schema can't check numbers inside free text, so this rule is up to authors.

## Protocol attributes (`protocols[]`)

| Attribute | Required | Type and choices |
| --- | --- | --- |
| `id` | Yes | Nonblank string; unique within `protocols`. |
| `productID` | Yes | Exactly the included product's `items[0].id`. |
| `title` | Yes | Nonblank string. |
| `purpose` | No | String or `null`. |
| `methodID` | Yes | An existing `methods[].id`, using a supported delivery choice below. |
| `population` | Yes | String describing the intended audience; `""` is allowed. |
| `evidenceNotes` | No | String or `null` for qualifications and context. |
| `regimen` | Yes | Object with `version: 1` and a nonempty `phases` array. |

Supported delivery IDs are `unspecified`, `subcutaneous`, `intramuscular`, `oral`, `intranasal`, `topical`, and `other`. Use the exact lowercase IDs. `unspecified` leaves the delivery choice for the user. The same choices apply to structured `route`, `route_options`, and `preparation_applies_to_routes` fields. Values outside these choices are invalid, even if a custom label is supplied.

## Regimen and phase attributes

Required regimen fields are `version` (integer, exactly `1`) and `phases` (nonempty array). Optional `regimen_type` is `single_compound`, `premixed_blend`, or `stack`. Each phase requires:

| Attribute | Type | Details |
| --- | --- | --- |
| `name` | nonblank string | Phase label. |
| `duration` | object | Required `kind`; see duration choices below. |
| `dose` | object or `null` | A known amount/range/options, or `null` when not specified. |
| `schedule` | object | Required `pattern`; see schedule choices below. |

Dose objects require a `unit` and use decimal **strings**, such as `"0.25"`, to retain exact source quantities. Optional `value`, `minimum`, `maximum`, and `options` (array of strings) describe one value, a range, or choices. `unit` uses the exact app choices: `mg`, `mcg`, `IU`, `mL`, `tablet`, `capsule`, `spray`, `drop`, or `application`. `basis` describes how to interpret the quantity: `total_product`, `per_administration`, `biological_activity`, `component`, `body_weight`, `daily_total`, `weekly_total`, `per_session`, or `not_reported`. No mass conversion is implied by `IU`.

Duration kinds are `fixed`, `range`, `minimum`, `maximum`, `ongoing`, `unreported`, `target_dose`, and `target_dose_choices`. Optional `value`, `minimum`, and `maximum` are integers from 1 through 365000 or `null`; `unit` is `day`, `week`, or `calendar_month`. A fixed day/week duration can seed an editor; reference ranges and calendar months do not silently become a chosen duration.

Schedule patterns are `daily`, `every_n_days`, `weekdays`, `times_per_week`, `as_needed`, and `source_described`. These include reference descriptions that require a user to choose a concrete personal schedule. Optional fields include `interval_days` (integer 1–365000), `doses_per_day` (integer 1–1440), `times_per_week` (integer 1–7), `weekdays` (array of ISO weekday integers, Monday `1` through Sunday `7`), and `suggested_times` (array of local `HH:mm` strings). These numeric fields may also be `null` when unreported. Empty time arrays leave times for the user to choose. `example_iso_weekdays`, descriptions, and source frequency ranges are reference context rather than an automatically selected schedule.

The schema lists every optional metadata attribute present in the community example, including nested formulation/components, preparation amounts, timing, alternative phases, cycle guidance, storage, cautions, and source context. Optional metadata objects remain extensible: additional attributes are retained for display but do not gain scheduling behavior. Recognized structured delivery and dose fields still require supported choices. Source-reported concentrations, time intervals, and syringe scale annotations are reference metadata, not additional personal dose unit choices.

When a user creates a personal protocol, the editor only copies settings it understands and requires valid personal choices before saving. A nonblank phase `condition` requires separate confirmation before that phase can start, even when its dose and schedule are fully specified. Population descriptions remain visible in the template, editor, final review, and retained source snapshot. Stack content can be viewed but cannot be activated as a single personal protocol. A file passing validation does not mean every reference field can be turned into an automatic schedule.

## Sources, citations, categories, and methods

| Object | Required attributes | Optional attributes |
| --- | --- | --- |
| Source | `id`: nonblank string; `url`: HTTP/HTTPS URL without credentials; `title`: string; `type`: string | `publisher`, `publishedAt`: string or `null`. Dates are retained as text. Common source types include `manufacturer`, `regulatory_label`, `human_study`, `animal_study`, `lab_study`, `clinical_guidance`, and `other`; type is free-form. |
| Citation | `sourceID`: existing source ID; `supports`: array of strings; exactly one nonblank `protocolID` or `productID` | `locator`, `evidenceNote`: string or `null`; the unused target may be absent or `null`. `supports` contains field names or reference paths, such as `/phases`. |
| Category | `id`: unique integer; `name`: nonblank string | None. |
| Method | `id`: unique supported delivery ID; `name`: nonblank string | None. |

IDs must be unique within their respective arrays and remain stable between edits. Matching IDs are also shared across installed files: namespace product, protocol, and source strings (for example, `your-name-product-routine`) to avoid accidental collisions. Reuse category integers only for the same category, or use `categoryID: null` and an empty categories array. Delivery method IDs always use the app's fixed choices. Replacing a shared source, category, or method definition affects all installed references to that ID and appears in the replacement warning.

Product category references, protocol product/method references, and citation targets/source references must resolve within the same file. A citation can target only the included product or one of its protocols.

Nested `library_item_id`/`component_id` references can identify this product or another installed product. Put component products in their own files and import them first. The review screen lists missing component IDs and disables only protocols needing them. At least one eligible protocol must be selected. Avoid circular component dependencies; each component file must have an independently importable protocol. The final assembled library is validated before saving. Citation `supports` paths and metadata source IDs are retained descriptions; the importer does not resolve them as JSON Pointers or fetch source URLs.

Missing optional attributes and explicit `null` are both accepted where the schema lists `null`. Empty strings are allowed for optional descriptions. Required nonblank names and IDs cannot be empty or whitespace. Use JSON numbers for versions, category IDs, counts, and duration values; use strings for dose quantities. Booleans and numeric strings are not interchangeable with numbers.

## Validate before sharing

Use a validator supporting [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation). For example, with [uv](https://docs.astral.sh/uv/), run this from the repository root:

```sh
uv run --no-project --with jsonschema python -c 'import json; from jsonschema import Draft202012Validator; s=json.load(open("template/library.schema.json")); Draft202012Validator.check_schema(s); v=Draft202012Validator(s); from pathlib import Path; files=list(Path("community-examples").glob("*.json")); [v.validate(json.loads(p.read_text())) for p in files]; print(f"{len(files)} product libraries have valid structure")'
```

To check your own file, use `Draft202012Validator(s).validate(json.load(open("your-product.json")))`. The schema checks plain decimal syntax on documented dose amounts, including ranges, options, and conditional values. Signs, exponents, grouping separators, and whitespace are invalid. The app additionally checks the file size, unique IDs, cross-references, parsed source URLs, and structured app choices in extensible metadata. Relationship and parsed-URL checks go beyond JSON Schema validation. Both file import and URL import use the bundled authoring schema before a catalog reaches installation review. Validation errors identify the failing JSON path when a structural rule fails.

The app repository embeds the same schema at `ios/ProtocolWizard/Resources/library-schema.json` (with a hyphen in the filename). `LibrarySchema` loads that resource from the app bundle so file and URL imports can validate offline against the installed app's supported format. The payload's optional `$schema` URL is only an editor hint.

Keep `template/library.schema.json` and the bundled copy identical, including `title` and `description` annotations. These annotations explain the format without changing validation rules. Editing this repository's schema does not change an installed app; bundled changes ship with an app update. From the app repository root, check that the copies match:

```sh
cmp library-authoring/template/library.schema.json ios/ProtocolWizard/Resources/library-schema.json
```

## Regenerate the schema reference

The Markdown reference uses [Adobe jsonschema2md](https://github.com/adobe/jsonschema2md), pinned to version `8.0.11`. The schema remains Draft 2020-12. Its `$id` identifies the canonical public schema and lets the generator resolve internal references.

With Node.js and npm installed, run these commands from this repository's root. `docs/schema/` contains generated output; rebuilding from an empty directory removes obsolete pages when fields change.

```sh
rm -r docs/schema
npm exec --yes --package=@adobe/jsonschema2md@8.0.11 -- jsonschema2md -d template -o docs/schema -x -
find docs/schema -type f \( -name 'library-defs.md' -o -name '*-properties.md' \) -delete
```

The `-x -` option disables schema-file output. The cleanup command removes empty definition/property-container pages that the generator labels as an unknown type; it keeps the documentation for their actual fields. Keep field explanations in the schema and regenerate rather than editing generated pages. Review and commit the generated Markdown with schema changes. Use this README for the import workflow and relationship checks that the app performs beyond JSON Schema validation.

## Optional URL distribution

Users can paste a direct HTTPS library JSON URL, including an individual community example's GitHub Raw URL, into **Library → Import library → Import from URL**. Choose **Download for review**, select protocols, and confirm any replacements. The same 10,000,000-byte limit and validation apply as for local files. The app retains the source URL and checks it for updates by downloading the JSON again and comparing its digest.

Alternatively, publish the catalog JSON and a separate HTTPS manifest:

```json
{
  "schemaVersion": 1,
  "catalogVersion": 1,
  "url": "https://example.org/example-supplement.json",
  "size": 12345,
  "sha256": "replace-with-the-64-character-lowercase-sha256-of-the-exact-file"
}
```

The `size` and `sha256` above are placeholders. `size` must be the exact byte count, at most 10,000,000. The SHA-256 digest must match the exact bytes downloaded, including whitespace and any final newline. Both versions must be `1` and match the product file. Downloads are capped at 10,000,000 bytes; responses identified as manifests must also fit within 64,000 bytes. Use HTTPS URLs without credentials or fragments. Publish the payload before updating the manifest; a new immutable payload URL per content edit helps avoid stale caches. Users paste the manifest URL into **Import from URL**, choose protocols, and confirm any replacements. A direct JSON URL has no separately published checksum; the app computes a digest of the validated download. Both paths recheck the cached bytes before installation.

Each product remembers its own source URL and last imported digest. Connected products are checked at most weekly when the app opens, or manually with **Check for updates**. Manifest checks download only the manifest until review; direct JSON checks download and validate the complete product file. A changed digest offers another review even while versions remain `1`. Updates require selection and confirmation; they never silently replace content or upload personal records. Changing a product's connected URL also requires confirmation. An update URL must continue to describe the same product ID.

## Maintaining the supplied examples

Maintainers with access to the Protocol Wizard app repository can regenerate these examples with `make catalog`. Run the commands in this section from that app repository, which contains the exporter and authoring database. The exporter reads the database without modifying it and writes one file per product into `library-authoring/community-examples/`. It excludes protocols with unsupported structured delivery methods, dose units, or dose amount syntax instead of rewriting source quantities.

To export one product and its optional hosted manifest:

```sh
python3 library/export_catalog.py --product-id example-supplement --output /tmp/example-supplement.json --manifest /tmp/latest.json --catalog-url https://example.org/example-supplement.json
```

Replace the example ID with an ID from your database. `--version` defaults to `1` and currently accepts only `1`. To choose another output directory, use `--output-dir /path/to/community-examples` instead of `--output` and omit `--product-id`. Inspect every generated file before publishing. Existing files for products no longer exported are not automatically deleted.
