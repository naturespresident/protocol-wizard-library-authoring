# Phase duration Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration
```

Required description of how long this stage lasts. Choose kind and include the applicable value or bounds with their unit. Ongoing or unreported durations can omit a numeric amount.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## duration Type

`object` ([Phase duration](library-defs-regimen-properties-phases-phase-properties-phase-duration.md))

# duration Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [kind](#kind)         | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/kind")       |
| [maximum](#maximum)   | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-maximum-duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/maximum") |
| [minimum](#minimum)   | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-minimum-duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/minimum") |
| [unit](#unit)         | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/unit")       |
| [value](#value)       | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/value")    |
| Additional Properties | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                    |

## kind

Describes a fixed length, a range, a minimum or maximum, an ongoing or unreported duration, or a source-defined target. Only fixed day or week lengths can seed a concrete editor duration.

`kind`

* is required

* Type: `string` ([Duration kind](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-kind.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/kind")

### kind Type

`string` ([Duration kind](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-kind.md))

### kind Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"fixed"`               |             |
| `"range"`               |             |
| `"minimum"`             |             |
| `"maximum"`             |             |
| `"ongoing"`             |             |
| `"unreported"`          |             |
| `"target_dose"`         |             |
| `"target_dose_choices"` |             |

## maximum

Upper duration bound in the stated unit, or null when unreported. A source range does not choose a personal duration.

`maximum`

* is optional

* Type: `integer` ([Maximum duration](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-maximum-duration.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-maximum-duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/maximum")

### maximum Type

`integer` ([Maximum duration](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-maximum-duration.md))

### maximum Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## minimum

Lower duration bound in the stated unit, or null when unreported. A source range does not choose a personal duration.

`minimum`

* is optional

* Type: `integer` ([Minimum duration](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-minimum-duration.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-minimum-duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/minimum")

### minimum Type

`integer` ([Minimum duration](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-minimum-duration.md))

### minimum Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## unit

Unit for the duration amount and bounds: day, week, or calendar_month. Calendar months are retained as reference context.

`unit`

* is optional

* Type: `string` ([Duration unit](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-unit.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/unit")

### unit Type

`string` ([Duration unit](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-unit.md))

### unit Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"day"`            |             |
| `"week"`           |             |
| `"calendar_month"` |             |

## value

Single duration amount in the stated unit. Use an integer from 1 through 365000, or null when unreported.

`value`

* is optional

* Type: `integer` ([Duration amount](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-amount.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/value")

### value Type

`integer` ([Duration amount](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-amount.md))

### value Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
