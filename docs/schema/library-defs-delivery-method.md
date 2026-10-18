# Delivery method Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method
```

A display label for a supported delivery method ID. The ID must use an app choice even when the label is customized.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## method Type

`object` ([Delivery method](library-defs-delivery-method.md))

# method Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                    |
| :------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)     | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/id") |
| [name](#name) | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/name")    |

## id

An exact, lowercase delivery choice supported by the app. Use unspecified when the user should choose the method; a custom display label does not allow a new ID.

`id`

* is required

* Type: `string` ([Delivery method ID](library-defs-delivery-method-id.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/id")

### id Type

`string` ([Delivery method ID](library-defs-delivery-method-id.md))

### id Constraints

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

## name

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`name`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/name")

### name Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")
