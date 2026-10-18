# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## citation Type

`object` ([Details](library-defs-citation.md))

one (and only one) of

* [Untitled undefined type in Protocol Wizard product library — schema version 1](library-defs-citation-oneof-0.md "check type definition")

* [Untitled undefined type in Protocol Wizard product library — schema version 1](library-defs-citation-oneof-1.md "check type definition")

# citation Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :---------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocolID](#protocolid)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocolid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID")     |
| [productID](#productid)       | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")       |
| [sourceID](#sourceid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")                             |
| [locator](#locator)           | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-locator.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")           |
| [evidenceNote](#evidencenote) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidencenote.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote") |
| [supports](#supports)         | `array`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supports.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")         |

## protocolID



`protocolID`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocolid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID")

### protocolID Type

`string`

## productID



`productID`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")

### productID Type

`string`

## sourceID



`sourceID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")

### sourceID Type

`string`

### sourceID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## locator



`locator`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-locator.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")

### locator Type

`string`

## evidenceNote



`evidenceNote`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidencenote.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote")

### evidenceNote Type

`string`

## supports



`supports`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supports.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")

### supports Type

`string[]`
