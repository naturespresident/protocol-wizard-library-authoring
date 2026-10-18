# Phase schedule Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule
```

Required description of when doses occur. Choose a pattern and the relevant count, interval, weekdays, or suggested times. Reference alternatives do not become an active schedule on import.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## schedule Type

`object` ([Phase schedule](library-defs-regimen-properties-phases-phase-properties-phase-schedule.md))

# schedule Properties

| Property                                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [block_pattern](#block_pattern)                               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-block_pattern.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/block_pattern")                               |
| [description](#description)                                   | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-description.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/description")                          |
| [doses_per_day](#doses_per_day)                               | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-day.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/doses_per_day")                               |
| [frequency_range](#frequency_range)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-frequency_range.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/frequency_range")                           |
| [interval_days](#interval_days)                               | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-days-between-doses.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/interval_days")                          |
| [interval_days_range](#interval_days_range)                   | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-interval_days_range.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/interval_days_range")                   |
| [maximum_doses_per_24_hours](#maximum_doses_per_24_hours)     | `number`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-maximum_doses_per_24_hours.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/maximum_doses_per_24_hours")     |
| [maximum_doses_per_month](#maximum_doses_per_month)           | `number`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-maximum_doses_per_month.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/maximum_doses_per_month")           |
| [minimum_minutes_before_event](#minimum_minutes_before_event) | `number`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-minimum_minutes_before_event.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/minimum_minutes_before_event") |
| [pattern](#pattern)                                           | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-pattern.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/pattern")                                  |
| [suggested_times](#suggested_times)                           | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-suggested-dose-times.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/suggested_times")                      |
| [times_per_week](#times_per_week)                             | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-week.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/times_per_week")                             |
| [times_per_week_options](#times_per_week_options)             | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-times_per_week_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/times_per_week_options")             |
| [timing_instruction](#timing_instruction)                     | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-timing_instruction.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/timing_instruction")                     |
| [weekdays](#weekdays)                                         | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-dosing-weekdays.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/weekdays")                                  |
| Additional Properties                                         | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                     |

## block_pattern



`block_pattern`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-block_pattern.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-block_pattern.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/block_pattern")

### block_pattern Type

`object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-block_pattern.md))

## description

Optional source wording or explanation that a structured pattern alone cannot express.

`description`

* is optional

* Type: `string` ([Schedule description](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-description.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-description.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/description")

### description Type

`string` ([Schedule description](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-description.md))

## doses_per_day

Number of administrations on each dosing day, from 1 through 1440, or null when unreported.

`doses_per_day`

* is optional

* Type: `integer` ([Doses per day](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-day.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-day.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/doses_per_day")

### doses_per_day Type

`integer` ([Doses per day](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-day.md))

### doses_per_day Constraints

**maximum**: the value of this number must smaller than or equal to: `1440`

**minimum**: the value of this number must greater than or equal to: `1`

## frequency_range



`frequency_range`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-frequency_range.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-frequency_range.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/frequency_range")

### frequency_range Type

`object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-frequency_range.md))

## interval_days

Interval in days for every_n_days, from 1 through 365000, or null when unreported.

`interval_days`

* is optional

* Type: `integer` ([Days between doses](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-days-between-doses.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-days-between-doses.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/interval_days")

### interval_days Type

`integer` ([Days between doses](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-days-between-doses.md))

### interval_days Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`

## interval_days_range



`interval_days_range`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-interval_days_range.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-interval_days_range.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/interval_days_range")

### interval_days_range Type

`object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-interval_days_range.md))

## maximum_doses_per_24_hours



`maximum_doses_per_24_hours`

* is optional

* Type: `number`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-maximum_doses_per_24_hours.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/maximum_doses_per_24_hours")

### maximum_doses_per_24_hours Type

`number`

## maximum_doses_per_month



`maximum_doses_per_month`

* is optional

* Type: `number`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-maximum_doses_per_month.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/maximum_doses_per_month")

### maximum_doses_per_month Type

`number`

## minimum_minutes_before_event



`minimum_minutes_before_event`

* is optional

* Type: `number`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-minimum_minutes_before_event.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/minimum_minutes_before_event")

### minimum_minutes_before_event Type

`number`

## pattern

Describes daily, interval, selected weekdays, weekly frequency, as-needed, or source-described use. Users must choose a valid personal schedule before saving.

`pattern`

* is required

* Type: `string` ([Schedule pattern](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-pattern.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-pattern.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/pattern")

### pattern Type

`string` ([Schedule pattern](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-pattern.md))

### pattern Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                | Explanation |
| :------------------- | :---------- |
| `"daily"`            |             |
| `"every_n_days"`     |             |
| `"weekdays"`         |             |
| `"times_per_week"`   |             |
| `"as_needed"`        |             |
| `"source_described"` |             |

## suggested_times

Local 24-hour times in HH:mm format. An empty array leaves times for the user to choose; importing does not schedule reminders.

`suggested_times`

* is optional

* Type: `string[]` ([Local dose time](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-suggested-dose-times-local-dose-time.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-suggested-dose-times.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/suggested_times")

### suggested_times Type

`string[]` ([Local dose time](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-suggested-dose-times-local-dose-time.md))

## times_per_week

Source-reported weekly frequency from 1 through 7, or null when unreported. A weekly count alone does not select dosing weekdays.

`times_per_week`

* is optional

* Type: `integer` ([Doses per week](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-week.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-week.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/times_per_week")

### times_per_week Type

`integer` ([Doses per week](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-week.md))

### times_per_week Constraints

**maximum**: the value of this number must smaller than or equal to: `7`

**minimum**: the value of this number must greater than or equal to: `1`

## times_per_week_options



`times_per_week_options`

* is optional

* Type: `number[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-times_per_week_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/times_per_week_options")

### times_per_week_options Type

`number[]`

## timing_instruction



`timing_instruction`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-timing_instruction.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/timing_instruction")

### timing_instruction Type

`string`

## weekdays

ISO weekday numbers for the routine: Monday is 1 and Sunday is 7.

`weekdays`

* is optional

* Type: `integer[]` ([ISO weekday](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-dosing-weekdays-iso-weekday.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-dosing-weekdays.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/weekdays")

### weekdays Type

`integer[]` ([ISO weekday](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-dosing-weekdays-iso-weekday.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
