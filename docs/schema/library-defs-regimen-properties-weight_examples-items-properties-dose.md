# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## dose Type

`object` ([Details](library-defs-regimen-properties-weight_examples-items-properties-dose.md))

# dose Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [approximate](#approximate) | `boolean` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-approximate.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/approximate") |
| [basis](#basis)             | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/basis")             |
| [unit](#unit)               | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/unit")               |
| [value](#value)             | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/value")             |
| Additional Properties       | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                       |

## approximate



`approximate`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-approximate.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/approximate")

### approximate Type

`boolean`

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/basis")

### basis Type

`string`

## unit



`unit`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/unit")

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

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples-items-properties-dose-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples/items/properties/dose/properties/value")

### value Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
