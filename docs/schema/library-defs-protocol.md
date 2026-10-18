# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## protocol Type

`object` ([Details](library-defs-protocol.md))

# protocol Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                       | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")                                     |
| [productID](#productid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")                              |
| [title](#title)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")                                  |
| [purpose](#purpose)             | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")             |
| [methodID](#methodid)           | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-methodid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")                               |
| [population](#population)       | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-population.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population")       |
| [evidenceNotes](#evidencenotes) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidencenotes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes") |
| [regimen](#regimen)             | `object` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")                                 |

## id



`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")

### id Type

`string`

### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## productID



`productID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")

### productID Type

`string`

### productID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## title



`title`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")

### title Type

`string`

### title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## purpose



`purpose`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")

### purpose Type

`string`

## methodID



`methodID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-methodid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")

### methodID Type

`string`

### methodID Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"unspecified"`   |             |
| `"subcutaneous"`  |             |
| `"intramuscular"` |             |
| `"oral"`          |             |
| `"intranasal"`    |             |
| `"topical"`       |             |
| `"other"`         |             |

## population



`population`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-population.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population")

### population Type

`string`

## evidenceNotes



`evidenceNotes`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidencenotes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes")

### evidenceNotes Type

`string`

## regimen

Structured reference content. Required core fields are version and phases. Optional metadata fields shown here are retained for display; additional metadata is allowed and does not automatically create a personal schedule.

`regimen`

* is required

* Type: `object` ([Details](library-defs-regimen.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")

### regimen Type

`object` ([Details](library-defs-regimen.md))
