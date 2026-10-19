# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## dose Type

`object` ([Details](library-defs-regimen-properties-optional_extension-properties-dose.md))

# dose Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                       |
| :-------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [basis](#basis)       | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/basis")              |
| [maximum](#maximum)   | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/maximum")   |
| [minimum](#minimum)   | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount-1.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/minimum") |
| [unit](#unit)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/unit")                |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                  |

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/basis")

### basis Type

`string`

## maximum

A plain period-separated decimal string, such as 0.25 or 500. Signs, exponents, grouping separators, and whitespace are invalid.

`maximum`

* is optional

* Type: `string` ([Decimal amount](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/maximum")

### maximum Type

`string` ([Decimal amount](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount.md))

### maximum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]+(\.[0-9]+)?(?![\s\S])
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%2B\(%5C.%5B0-9%5D%2B\)%3F\(%3F!%5B%5Cs%5CS%5D\) "try regular expression with regexr.com")

## minimum

A plain period-separated decimal string, such as 0.25 or 500. Signs, exponents, grouping separators, and whitespace are invalid.

`minimum`

* is optional

* Type: `string` ([Decimal amount](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount-1.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount-1.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/minimum")

### minimum Type

`string` ([Decimal amount](library-defs-regimen-properties-optional_extension-properties-dose-properties-decimal-amount-1.md))

### minimum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]+(\.[0-9]+)?(?![\s\S])
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%2B\(%5C.%5B0-9%5D%2B\)%3F\(%3F!%5B%5Cs%5CS%5D\) "try regular expression with regexr.com")

## unit



`unit`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension/properties/dose/properties/unit")

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

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
