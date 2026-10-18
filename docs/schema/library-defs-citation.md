# Citation Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation
```

Connects one source to exactly one target: provide a nonblank protocolID or productID, never both. The unused target may be omitted or null. The source and target must exist in this file; the app checks these relationships.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## citation Type

`object` ([Citation](library-defs-citation.md))

one (and only one) of

* [Protocol citation](library-defs-citation-oneof-protocol-citation.md "check type definition")

* [Product citation](library-defs-citation-oneof-product-citation.md "check type definition")

# citation Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocolID](#protocolid)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocol-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID") |
| [productID](#productid)       | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-product-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")   |
| [sourceID](#sourceid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")                            |
| [locator](#locator)           | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-source-location.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")       |
| [evidenceNote](#evidencenote) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidence-note.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote")    |
| [supports](#supports)         | `array`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supported-fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")     |

## protocolID

ID of a protocol in this file. Provide a nonblank value when citing a protocol; otherwise omit this field or set it to null.

`protocolID`

* is optional

* Type: `string` ([Protocol target ID](library-defs-citation-properties-protocol-target-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocol-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID")

### protocolID Type

`string` ([Protocol target ID](library-defs-citation-properties-protocol-target-id.md))

## productID

ID of the product in this file. Provide a nonblank value when citing the product; otherwise omit this field or set it to null.

`productID`

* is optional

* Type: `string` ([Product target ID](library-defs-citation-properties-product-target-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-product-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")

### productID Type

`string` ([Product target ID](library-defs-citation-properties-product-target-id.md))

## sourceID

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`sourceID`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")

### sourceID Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### sourceID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## locator

Optional page, section, table, or other locator within the source. Omit or set to null when unavailable.

`locator`

* is optional

* Type: `string` ([Source location](library-defs-citation-properties-source-location.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-source-location.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")

### locator Type

`string` ([Source location](library-defs-citation-properties-source-location.md))

## evidenceNote

Optional explanation of what the source supports and any relevant limits. Omit or set to null when unavailable.

`evidenceNote`

* is optional

* Type: `string` ([Evidence note](library-defs-citation-properties-evidence-note.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidence-note.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote")

### evidenceNote Type

`string` ([Evidence note](library-defs-citation-properties-evidence-note.md))

## supports

Field names or reference paths supported by this citation, such as /phases or /benefits. The app retains these strings as descriptions and does not resolve them as JSON Pointers.

`supports`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supported-fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")

### supports Type

`string[]`
