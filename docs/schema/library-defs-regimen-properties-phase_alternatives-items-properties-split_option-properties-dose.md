# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## dose Type

`object` ([Details](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose.md))

# dose Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [basis](#basis)       | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose/properties/basis")          |
| [unit](#unit)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose/properties/unit")            |
| [value](#value)       | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose/properties/value") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                          |

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose/properties/basis")

### basis Type

`string`

## unit



`unit`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose/properties/unit")

### unit Type

`string`

### unit Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"mg"`          |             |
| `"mcg"`         |             |
| `"IU"`          |             |
| `"mL"`          |             |
| `"tablet"`      |             |
| `"capsule"`     |             |
| `"spray"`       |             |
| `"drop"`        |             |
| `"application"` |             |

## value

A plain period-separated decimal string, such as 0.25 or 500. Signs, exponents, grouping separators, and whitespace are invalid.

`value`

* is optional

* Type: `string` ([Decimal amount](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-decimal-amount.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives/items/properties/split_option/properties/dose/properties/value")

### value Type

`string` ([Decimal amount](library-defs-regimen-properties-phase_alternatives-items-properties-split_option-properties-dose-properties-decimal-amount.md))

### value Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]+(\.[0-9]+)?(?![\s\S])
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%2B\(%5C.%5B0-9%5D%2B\)%3F\(%3F!%5B%5Cs%5CS%5D\) "try regular expression with regexr.com")

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
