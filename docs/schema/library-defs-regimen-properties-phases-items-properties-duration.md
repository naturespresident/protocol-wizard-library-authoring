# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## duration Type

`object` ([Details](library-defs-regimen-properties-phases-items-properties-duration.md))

# duration Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                          |
| :-------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [kind](#kind)         | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/kind")       |
| [maximum](#maximum)   | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-maximum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/maximum") |
| [minimum](#minimum)   | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-minimum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/minimum") |
| [unit](#unit)         | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/unit")       |
| [value](#value)       | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/value")     |
| Additional Properties | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                     |

## kind



`kind`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/kind")

### kind Type

`string`

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



`maximum`

* is optional

* Type: `integer`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-maximum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/maximum")

### maximum Type

`integer`

### maximum Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## minimum



`minimum`

* is optional

* Type: `integer`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-minimum.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/minimum")

### minimum Type

`integer`

### minimum Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## unit



`unit`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/unit")

### unit Type

`string`

### unit Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"day"`            |             |
| `"week"`           |             |
| `"calendar_month"` |             |

## value



`value`

* is optional

* Type: `integer`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-items-properties-duration-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/value")

### value Type

`integer`

### value Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
