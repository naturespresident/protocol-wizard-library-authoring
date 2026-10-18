# Phase Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items
```

One stage of the reusable routine. Reference ranges, alternatives, and source descriptions still require the user to choose valid personal settings.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## items Type

`object` ([Phase](library-defs-regimen-properties-phases-phase.md))

# items Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [administration_volume](#administration_volume) | `object` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-administration_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/administration_volume") |
| [component_doses](#component_doses)             | `array`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-component_doses.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/component_doses")             |
| [condition](#condition)                         | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-condition.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/condition")                         |
| [dose](#dose)                                   | `object` | Required | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose")                             |
| [duration](#duration)                           | `object` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration")                     |
| [name](#name)                                   | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/name")                             |
| [schedule](#schedule)                           | `object` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule")                     |
| [source_dose_basis](#source_dose_basis)         | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-source_dose_basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/source_dose_basis")         |
| [source_measurement](#source_measurement)       | `object` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-source_measurement.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/source_measurement")       |
| [status](#status)                               | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-status.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/status")                               |
| Additional Properties                           | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                         |

## administration_volume



`administration_volume`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-phases-phase-properties-administration_volume.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-administration_volume.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/administration_volume")

### administration_volume Type

`object` ([Details](library-defs-regimen-properties-phases-phase-properties-administration_volume.md))

## component_doses



`component_doses`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-phases-phase-properties-component_doses-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-component_doses.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/component_doses")

### component_doses Type

`object[]` ([Details](library-defs-regimen-properties-phases-phase-properties-component_doses-items.md))

## condition



`condition`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-condition.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/condition")

### condition Type

`string`

## dose

Required dose content: a decimal string value, a minimum/maximum range, options, or null when unknown. Dose objects need a supported unit. The app checks plain decimal strings; ranges and component or body-weight amounts are not automatically chosen.

`dose`

* is required

* Type: `object` ([Phase dose](library-defs-regimen-properties-phases-phase-properties-phase-dose.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose")

### dose Type

`object` ([Phase dose](library-defs-regimen-properties-phases-phase-properties-phase-dose.md))

## duration

Required description of how long this stage lasts. Choose kind and include the applicable value or bounds with their unit. Ongoing or unreported durations can omit a numeric amount.

`duration`

* is required

* Type: `object` ([Phase duration](library-defs-regimen-properties-phases-phase-properties-phase-duration.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration")

### duration Type

`object` ([Phase duration](library-defs-regimen-properties-phases-phase-properties-phase-duration.md))

## name

Nonblank display label for this stage, such as Initial phase or Maintenance.

`name`

* is required

* Type: `string` ([Phase name](library-defs-regimen-properties-phases-phase-properties-phase-name.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/name")

### name Type

`string` ([Phase name](library-defs-regimen-properties-phases-phase-properties-phase-name.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## schedule

Required description of when doses occur. Choose a pattern and the relevant count, interval, weekdays, or suggested times. Reference alternatives do not become an active schedule on import.

`schedule`

* is required

* Type: `object` ([Phase schedule](library-defs-regimen-properties-phases-phase-properties-phase-schedule.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule")

### schedule Type

`object` ([Phase schedule](library-defs-regimen-properties-phases-phase-properties-phase-schedule.md))

## source_dose_basis



`source_dose_basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-source_dose_basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/source_dose_basis")

### source_dose_basis Type

`string`

## source_measurement



`source_measurement`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-phases-phase-properties-source_measurement.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-source_measurement.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/source_measurement")

### source_measurement Type

`object` ([Details](library-defs-regimen-properties-phases-phase-properties-source_measurement.md))

## status



`status`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-status.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/status")

### status Type

`string`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
