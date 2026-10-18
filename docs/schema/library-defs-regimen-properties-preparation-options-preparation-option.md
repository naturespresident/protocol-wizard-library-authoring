# Preparation option Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items
```

One source-reported preparation alternative. Amounts, volumes, and concentrations describe reference content; users enter their own personal product details.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## items Type

`object` ([Preparation option](library-defs-regimen-properties-preparation-options-preparation-option.md))

# items Properties

| Property                                                        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [calculation_basis](#calculation_basis)                         | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-calculation_basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/calculation_basis")                         |
| [component_amounts](#component_amounts)                         | `array`       | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-component_amounts.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_amounts")                         |
| [component_id](#component_id)                                   | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-component-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_id")                                   |
| [container_amount](#container_amount)                           | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_amount")                           |
| [container_volume](#container_volume)                           | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_volume")                           |
| [diluent](#diluent)                                             | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent")                                             |
| [diluent_volume](#diluent_volume)                               | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume")                               |
| [discard_after_first_open_days](#discard_after_first_open_days) | `number`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-discard_after_first_open_days.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/discard_after_first_open_days") |
| [dry_amount](#dry_amount)                                       | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-dry-product-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/dry_amount")                               |
| [final_solution_volume](#final_solution_volume)                 | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-final-solution-volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/final_solution_volume")                 |
| [form](#form)                                                   | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-product-form.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/form")                                           |
| [labeled_concentration](#labeled_concentration)                 | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-labeled_concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/labeled_concentration")                 |
| [provenance](#provenance)                                       | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/provenance")                                       |
| [reconstitution_required](#reconstitution_required)             | `boolean`     | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-reconstitution-required.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/reconstitution_required")             |
| [source_reported_concentration](#source_reported_concentration) | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-source-concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/source_reported_concentration")          |
| [storage](#storage)                                             | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/storage")                                             |
| Additional Properties                                           | Any           | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                |

## calculation_basis



`calculation_basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-calculation_basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/calculation_basis")

### calculation_basis Type

`string`

## component_amounts



`component_amounts`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-component_amounts-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-component_amounts.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_amounts")

### component_amounts Type

`object[]` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-component_amounts-items.md))

## component_id

Reserved in the version 1 format; if provided, this field must be null.

`component_id`

* is optional

* Type: `null`, the value must be null ([Component ID](library-defs-regimen-properties-preparation-options-preparation-option-properties-component-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-component-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/component_id")

### component_id Type

`null`, the value must be null ([Component ID](library-defs-regimen-properties-preparation-options-preparation-option-properties-component-id.md))

## container_amount



`container_amount`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_amount.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_amount")

### container_amount Type

`object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_amount.md))

## container_volume



`container_volume`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_volume.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/container_volume")

### container_volume Type

`object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-container_volume.md))

## diluent

Source-reported diluent name for this preparation option.

`diluent`

* is optional

* Type: `string` ([Diluent](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent")

### diluent Type

`string` ([Diluent](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent.md))

## diluent_volume

Source-reported diluent quantity with its unit, or null when unknown. Do not infer a final solution volume from this field.

`diluent_volume`

* is optional

* Type: `object` ([Diluent volume](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/diluent_volume")

### diluent_volume Type

`object` ([Diluent volume](library-defs-regimen-properties-preparation-options-preparation-option-properties-diluent-volume.md))

## discard_after_first_open_days



`discard_after_first_open_days`

* is optional

* Type: `number`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-discard_after_first_open_days.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/discard_after_first_open_days")

### discard_after_first_open_days Type

`number`

## dry_amount

Source-reported dry quantity with its unit, or null when unknown.

`dry_amount`

* is optional

* Type: `object` ([Dry product amount](library-defs-regimen-properties-preparation-options-preparation-option-properties-dry-product-amount.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-dry-product-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/dry_amount")

### dry_amount Type

`object` ([Dry product amount](library-defs-regimen-properties-preparation-options-preparation-option-properties-dry-product-amount.md))

## final_solution_volume

Reserved in the version 1 format; if provided, this field must be null.

`final_solution_volume`

* is optional

* Type: `null`, the value must be null ([Final solution volume](library-defs-regimen-properties-preparation-options-preparation-option-properties-final-solution-volume.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-final-solution-volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/final_solution_volume")

### final_solution_volume Type

`null`, the value must be null ([Final solution volume](library-defs-regimen-properties-preparation-options-preparation-option-properties-final-solution-volume.md))

## form

Source description of the product's physical form for this option.

`form`

* is optional

* Type: `string` ([Product form](library-defs-regimen-properties-preparation-options-preparation-option-properties-product-form.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-product-form.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/form")

### form Type

`string` ([Product form](library-defs-regimen-properties-preparation-options-preparation-option-properties-product-form.md))

## labeled_concentration



`labeled_concentration`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-labeled_concentration.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-labeled_concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/labeled_concentration")

### labeled_concentration Type

`object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-labeled_concentration.md))

## provenance



`provenance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-provenance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/provenance")

### provenance Type

`object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-provenance.md))

## reconstitution_required

Whether the source preparation requires mixing before use.

`reconstitution_required`

* is optional

* Type: `boolean` ([Reconstitution required](library-defs-regimen-properties-preparation-options-preparation-option-properties-reconstitution-required.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-reconstitution-required.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/reconstitution_required")

### reconstitution_required Type

`boolean` ([Reconstitution required](library-defs-regimen-properties-preparation-options-preparation-option-properties-reconstitution-required.md))

## source_reported_concentration

Source-reported concentration with its unit, or null when unknown. Retain the source quantity rather than inferring a personal calculation.

`source_reported_concentration`

* is optional

* Type: `object` ([Source concentration](library-defs-regimen-properties-preparation-options-preparation-option-properties-source-concentration.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-source-concentration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/source_reported_concentration")

### source_reported_concentration Type

`object` ([Source concentration](library-defs-regimen-properties-preparation-options-preparation-option-properties-source-concentration.md))

## storage



`storage`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-storage.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options-preparation-option-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options/items/properties/storage")

### storage Type

`object` ([Details](library-defs-regimen-properties-preparation-options-preparation-option-properties-storage.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
