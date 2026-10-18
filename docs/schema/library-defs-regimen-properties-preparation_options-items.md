# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## items Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items.md))

# items Properties

| Property                                                        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------------------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [calculation_basis](#calculation_basis)                         | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-calculation_basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/calculation_basis")                         |
| [component_amounts](#component_amounts)                         | `array`       | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-component_amounts.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_amounts")                         |
| [component_id](#component_id)                                   | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-component_id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_id")                                   |
| [container_amount](#container_amount)                           | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-container_amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_amount")                           |
| [container_volume](#container_volume)                           | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-container_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_volume")                           |
| [diluent](#diluent)                                             | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-diluent.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent")                                             |
| [diluent_volume](#diluent_volume)                               | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-diluent_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume")                               |
| [discard_after_first_open_days](#discard_after_first_open_days) | `number`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-discard_after_first_open_days.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/discard_after_first_open_days") |
| [dry_amount](#dry_amount)                                       | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-dry_amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/dry_amount")                                       |
| [final_solution_volume](#final_solution_volume)                 | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-final_solution_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/final_solution_volume")                 |
| [form](#form)                                                   | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-form.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/form")                                                   |
| [labeled_concentration](#labeled_concentration)                 | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-labeled_concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/labeled_concentration")                 |
| [provenance](#provenance)                                       | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/provenance")                                       |
| [reconstitution_required](#reconstitution_required)             | `boolean`     | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-reconstitution_required.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/reconstitution_required")             |
| [source_reported_concentration](#source_reported_concentration) | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-source_reported_concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/source_reported_concentration") |
| [storage](#storage)                                             | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/storage")                                             |
| Additional Properties                                           | Any           | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                   |

## calculation_basis



`calculation_basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-calculation_basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/calculation_basis")

### calculation_basis Type

`string`

## component_amounts



`component_amounts`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-preparation_options-items-properties-component_amounts-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-component_amounts.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_amounts")

### component_amounts Type

`object[]` ([Details](library-defs-regimen-properties-preparation_options-items-properties-component_amounts-items.md))

## component_id



`component_id`

* is optional

* Type: `null`, the value must be null

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-component_id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_id")

### component_id Type

`null`, the value must be null

## container_amount



`container_amount`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-container_amount.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-container_amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_amount")

### container_amount Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-container_amount.md))

## container_volume



`container_volume`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-container_volume.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-container_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_volume")

### container_volume Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-container_volume.md))

## diluent



`diluent`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-diluent.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent")

### diluent Type

`string`

## diluent_volume



`diluent_volume`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-diluent_volume.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-diluent_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume")

### diluent_volume Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-diluent_volume.md))

## discard_after_first_open_days



`discard_after_first_open_days`

* is optional

* Type: `number`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-discard_after_first_open_days.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/discard_after_first_open_days")

### discard_after_first_open_days Type

`number`

## dry_amount



`dry_amount`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-dry_amount.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-dry_amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/dry_amount")

### dry_amount Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-dry_amount.md))

## final_solution_volume



`final_solution_volume`

* is optional

* Type: `null`, the value must be null

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-final_solution_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/final_solution_volume")

### final_solution_volume Type

`null`, the value must be null

## form



`form`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-form.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/form")

### form Type

`string`

## labeled_concentration



`labeled_concentration`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-labeled_concentration.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-labeled_concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/labeled_concentration")

### labeled_concentration Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-labeled_concentration.md))

## provenance



`provenance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-provenance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/provenance")

### provenance Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-provenance.md))

## reconstitution_required



`reconstitution_required`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-reconstitution_required.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/reconstitution_required")

### reconstitution_required Type

`boolean`

## source_reported_concentration



`source_reported_concentration`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-source_reported_concentration.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-source_reported_concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/source_reported_concentration")

### source_reported_concentration Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-source_reported_concentration.md))

## storage



`storage`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-storage.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options-items-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/storage")

### storage Type

`object` ([Details](library-defs-regimen-properties-preparation_options-items-properties-storage.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
