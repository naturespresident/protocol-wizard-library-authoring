# Storage Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage
```

Optional source-reported storage, handling, and discard guidance. This reference metadata does not set personal expiry dates or reminders.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## storage Type

`object` ([Storage](library-defs-regimen-properties-storage.md))

# storage Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                    |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [basis](#basis)                 | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/basis")                 |
| [discard_if](#discard_if)       | `array`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-discard_if.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/discard_if")       |
| [dry](#dry)                     | `object` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-dry.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/dry")                     |
| [notes](#notes)                 | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/notes")                 |
| [provenance](#provenance)       | `object` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/provenance")       |
| [reconstituted](#reconstituted) | `object` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-reconstituted.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/reconstituted") |
| [source_id](#source_id)         | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-source_id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/source_id")         |
| [source_tables](#source_tables) | `array`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-source_tables.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/source_tables") |
| Additional Properties           | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                               |

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/basis")

### basis Type

`string`

## discard_if



`discard_if`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-discard_if.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/discard_if")

### discard_if Type

`string[]`

## dry



`dry`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-storage-properties-dry.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-dry.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/dry")

### dry Type

`object` ([Details](library-defs-regimen-properties-storage-properties-dry.md))

## notes



`notes`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/notes")

### notes Type

`string`

## provenance



`provenance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-storage-properties-provenance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/provenance")

### provenance Type

`object` ([Details](library-defs-regimen-properties-storage-properties-provenance.md))

## reconstituted



`reconstituted`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-storage-properties-reconstituted.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-reconstituted.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/reconstituted")

### reconstituted Type

`object` ([Details](library-defs-regimen-properties-storage-properties-reconstituted.md))

## source_id



`source_id`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-source_id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/source_id")

### source_id Type

`string`

## source_tables



`source_tables`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-storage-properties-source_tables-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage-properties-source_tables.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage/properties/source_tables")

### source_tables Type

`object[]` ([Details](library-defs-regimen-properties-storage-properties-source_tables-items.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
