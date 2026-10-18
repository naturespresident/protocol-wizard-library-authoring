# Diluent volume Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume
```

Source-reported diluent quantity with its unit, or null when unknown. Do not infer a final solution volume from this field.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## diluent_volume Type

`object` ([Diluent volume](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume.md))

# diluent_volume Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [unit](#unit)         | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume/properties/unit")   |
| [value](#value)       | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume/properties/value") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                    |

## unit



`unit`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume-properties-unit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume/properties/unit")

### unit Type

`string`

## value



`value`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume-properties-value.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume/properties/value")

### value Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
