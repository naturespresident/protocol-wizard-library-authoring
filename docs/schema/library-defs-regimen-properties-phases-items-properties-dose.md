# Untitled undefined type in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose
```

A single decimal string value, a minimum/maximum range, options, or null when unknown. These are reference quantities; ranges and component/body-weight doses are not automatically chosen.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## dose Type

`object` ([Details](library-defs-regimen-properties-phases-items-properties-dose.md))

# dose Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                              |
| :------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [approximate](#approximate)     | `boolean` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-approximate.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/approximate")     |
| [basis](#basis)                 | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/basis")                 |
| [conditions](#conditions)       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-conditions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions")       |
| [kind](#kind)                   | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/kind")                   |
| [maximum](#maximum)             | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-maximum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/maximum")             |
| [minimum](#minimum)             | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-minimum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/minimum")             |
| [options](#options)             | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/options")             |
| [range_options](#range_options) | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-range_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/range_options") |
| [unit](#unit)                   | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/unit")                   |
| [value](#value)                 | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/value")                 |
| Additional Properties           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                         |

## approximate



`approximate`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-approximate.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/approximate")

### approximate Type

`boolean`

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/basis")

### basis Type

`string`

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

* Type: `object[]` ([Details](library-defs-regimen-properties-phases-items-properties-dose-properties-conditions-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-conditions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions")

### conditions Type

`object[]` ([Details](library-defs-regimen-properties-phases-items-properties-dose-properties-conditions-items.md))

## kind



`kind`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/kind")

### kind Type

`string`

## maximum



`maximum`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-maximum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/maximum")

### maximum Type

`string`

## minimum



`minimum`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-minimum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/minimum")

### minimum Type

`string`

## options



`options`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/options")

### options Type

`string[]`

## range_options



`range_options`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-phases-items-properties-dose-properties-range_options-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-range_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/range_options")

### range_options Type

`object[]` ([Details](library-defs-regimen-properties-phases-items-properties-dose-properties-range_options-items.md))

## unit



`unit`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/unit")

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



`value`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-dose-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/value")

### value Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
