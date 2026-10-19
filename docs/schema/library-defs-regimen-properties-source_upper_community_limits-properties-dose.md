# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## dose Type

`object` ([Details](library-defs-regimen-properties-source_upper_community_limits-properties-dose.md))

# dose Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                           |
| :-------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [basis](#basis)       | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/basis")            |
| [kind](#kind)         | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/kind")              |
| [maximum](#maximum)   | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/maximum") |
| [minimum](#minimum)   | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-minimum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/minimum")        |
| [unit](#unit)         | `string`      | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/unit")              |
| Additional Properties | Any           | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                      |

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/basis")

### basis Type

`string`

## kind



`kind`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/kind")

### kind Type

`string`

## maximum

A plain period-separated decimal string, such as 0.25 or 500. Signs, exponents, grouping separators, and whitespace are invalid.

`maximum`

* is optional

* Type: `string` ([Decimal amount](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-decimal-amount.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/maximum")

### maximum Type

`string` ([Decimal amount](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-decimal-amount.md))

### maximum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]+(\.[0-9]+)?(?![\s\S])
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%2B\(%5C.%5B0-9%5D%2B\)%3F\(%3F!%5B%5Cs%5CS%5D\) "try regular expression with regexr.com")

## minimum

Reserved in the version 1 format; if provided, this field must be null.

`minimum`

* is optional

* Type: `null`, the value must be null ([Minimum](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-minimum.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-minimum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/minimum")

### minimum Type

`null`, the value must be null ([Minimum](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-minimum.md))

## unit



`unit`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits/properties/dose/properties/unit")

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
