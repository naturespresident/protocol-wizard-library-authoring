# Protocol Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol
```

A reusable routine for the included product. Importing adds reference content; the user creates and confirms a personal schedule separately.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## protocol Type

`object` ([Protocol](library-defs-protocol.md))

# protocol Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                       | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")                                 |
| [productID](#productid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")                          |
| [title](#title)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")                              |
| [purpose](#purpose)             | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")              |
| [methodID](#methodid)           | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")                      |
| [population](#population)       | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-intended-audience.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population") |
| [evidenceNotes](#evidencenotes) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidence-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes") |
| [regimen](#regimen)             | `object` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")                                  |

## id

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`id`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")

### id Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## productID

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`productID`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")

### productID Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### productID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## title

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`title`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")

### title Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## purpose

Optional explanation of the routine's intended goal. Omit or set to null when unavailable.

`purpose`

* is optional

* Type: `string` ([Purpose](library-defs-protocol-properties-purpose.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")

### purpose Type

`string` ([Purpose](library-defs-protocol-properties-purpose.md))

## methodID

An exact, lowercase delivery choice supported by the app. Use unspecified when the user should choose the method; a custom display label does not allow a new ID.

`methodID`

* is required

* Type: `string` ([Delivery method ID](library-defs-delivery-method-id.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")

### methodID Type

`string` ([Delivery method ID](library-defs-delivery-method-id.md))

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

Text describing who the source routine applies to. Use an empty string when no audience is specified.

`population`

* is required

* Type: `string` ([Intended audience](library-defs-protocol-properties-intended-audience.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-intended-audience.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population")

### population Type

`string` ([Intended audience](library-defs-protocol-properties-intended-audience.md))

## evidenceNotes

Optional qualifications, uncertainties, or source context for this routine. Omit or set to null when unavailable.

`evidenceNotes`

* is optional

* Type: `string` ([Evidence notes](library-defs-protocol-properties-evidence-notes.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidence-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes")

### evidenceNotes Type

`string` ([Evidence notes](library-defs-protocol-properties-evidence-notes.md))

## regimen

The reusable dose, duration, and schedule content of a protocol. Version and phases are required. Optional source metadata supplies context; the editor only copies settings it understands.

`regimen`

* is required

* Type: `object` ([Regimen](library-defs-regimen.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")

### regimen Type

`object` ([Regimen](library-defs-regimen.md))
