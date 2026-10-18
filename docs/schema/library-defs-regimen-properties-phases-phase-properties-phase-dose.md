# Phase dose Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose
```

Required dose content: a decimal string value, a minimum/maximum range, options, or null when unknown. Dose objects need a supported unit. The app checks plain decimal strings; ranges and component or body-weight amounts are not automatically chosen.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## dose Type

`object` ([Phase dose](library-defs-regimen-properties-phases-phase-properties-phase-dose.md))

# dose Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [approximate](#approximate)     | `boolean` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-approximate-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/approximate") |
| [basis](#basis)                 | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/basis")             |
| [conditions](#conditions)       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions")        |
| [kind](#kind)                   | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/kind")                    |
| [maximum](#maximum)             | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-maximum-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/maximum")         |
| [minimum](#minimum)             | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/minimum")         |
| [options](#options)             | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-choices.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/options")         |
| [range_options](#range_options) | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-range_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/range_options")  |
| [unit](#unit)                   | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/unit")               |
| [value](#value)                 | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/value")            |
| Additional Properties           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                |

## approximate

Whether the source describes the amount as approximate.

`approximate`

* is optional

* Type: `boolean` ([Approximate dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-approximate-dose.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-approximate-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/approximate")

### approximate Type

`boolean` ([Approximate dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-approximate-dose.md))

## basis

How to interpret the quantity, such as per administration, a daily total, a component amount, or a body-weight amount. This label does not convert quantities or choose a personal dose.

`basis`

* is optional

* Type: `string` ([Dose basis](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-basis.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/basis")

### basis Type

`string` ([Dose basis](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-basis.md))

### basis Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"total_product"`       |             |
| `"per_administration"`  |             |
| `"biological_activity"` |             |
| `"component"`           |             |
| `"body_weight"`         |             |
| `"daily_total"`         |             |
| `"weekly_total"`        |             |
| `"per_session"`         |             |
| `"not_reported"`        |             |

## conditions



`conditions`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions")

### conditions Type

`object[]` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items.md))

## kind



`kind`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/kind")

### kind Type

`string`

## maximum

Upper end of a source-reported dose range as a plain decimal string. The user chooses a concrete personal dose.

`maximum`

* is optional

* Type: `string` ([Maximum dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-maximum-dose.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-maximum-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/maximum")

### maximum Type

`string` ([Maximum dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-maximum-dose.md))

## minimum

Lower end of a source-reported dose range as a plain decimal string, or null when unknown. The user chooses a concrete personal dose.

`minimum`

* is optional

* Type: `string` ([Minimum dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/minimum")

### minimum Type

`string` ([Minimum dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose.md))

## options

Alternative source-reported quantities as plain decimal strings in the stated unit. Listing choices does not select a personal dose.

`options`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-choices.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/options")

### options Type

`string[]`

## range_options



`range_options`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-range_options-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-range_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/range_options")

### range_options Type

`object[]` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-range_options-items.md))

## unit

Exact app-supported unit for all quantities in this dose object. IU represents biological activity and does not imply a mass conversion.

`unit`

* is required

* Type: `string` ([Dose unit](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-unit.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/unit")

### unit Type

`string` ([Dose unit](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-unit.md))

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

Single dose quantity as a plain decimal string, such as 0.25 or 500, or null when unknown. Use a dot for the decimal separator and no grouping commas or unit suffix.

`value`

* is optional

* Type: `string` ([Dose amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/value")

### value Type

`string` ([Dose amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
