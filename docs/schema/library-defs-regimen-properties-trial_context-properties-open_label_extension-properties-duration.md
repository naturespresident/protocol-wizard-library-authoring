# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## duration Type

`object` ([Details](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration.md))

# duration Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [kind](#kind)         | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration/properties/kind")   |
| [unit](#unit)         | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration/properties/unit")   |
| [value](#value)       | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration/properties/value") |
| Additional Properties | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                   |

## kind



`kind`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration/properties/kind")

### kind Type

`string`

## unit



`unit`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration/properties/unit")

### unit Type

`string`

## value



`value`

* is optional

* Type: `integer`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context-properties-open_label_extension-properties-duration-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context/properties/open_label_extension/properties/duration/properties/value")

### value Type

`integer`

### value Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
