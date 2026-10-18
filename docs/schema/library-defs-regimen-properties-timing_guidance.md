# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## timing_guidance Type

`object` ([Details](library-defs-regimen-properties-timing_guidance.md))

# timing_guidance Properties

| Property                                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [applies_to](#applies_to)                                 | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-applies_to.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/applies_to")                                 |
| [basis](#basis)                                           | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/basis")                                           |
| [certainty](#certainty)                                   | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-certainty.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/certainty")                                   |
| [example_iso_weekdays](#example_iso_weekdays)             | `array`       | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-example_iso_weekdays.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/example_iso_weekdays")             |
| [food_guidance](#food_guidance)                           | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-food_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/food_guidance")                           |
| [optional_split_windows](#optional_split_windows)         | `array`       | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-optional_split_windows.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/optional_split_windows")         |
| [preferred_time_of_day](#preferred_time_of_day)           | `string`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-preferred_time_of_day.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/preferred_time_of_day")           |
| [provenance](#provenance)                                 | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/provenance")                                 |
| [relative_events](#relative_events)                       | `array`       | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-relative_events.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/relative_events")                       |
| [site_as_reported](#site_as_reported)                     | `string`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-site_as_reported.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/site_as_reported")                     |
| [spacing](#spacing)                                       | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-spacing.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/spacing")                                       |
| [spacing_between_components](#spacing_between_components) | `object`      | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-spacing_between_components.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/spacing_between_components") |
| [spacing_between_doses](#spacing_between_doses)           | `object`      | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-spacing_between_doses.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/spacing_between_doses")           |
| [suggested_clock_times](#suggested_clock_times)           | `array`       | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-suggested_clock_times.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/suggested_clock_times")           |
| Additional Properties                                     | Any           | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                         |

## applies_to



`applies_to`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-applies_to.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/applies_to")

### applies_to Type

`string`

## basis



`basis`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-basis.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/basis")

### basis Type

`string`

## certainty



`certainty`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-certainty.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/certainty")

### certainty Type

`string`

## example_iso_weekdays



`example_iso_weekdays`

* is optional

* Type: `number[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-example_iso_weekdays.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/example_iso_weekdays")

### example_iso_weekdays Type

`number[]`

## food_guidance



`food_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-timing_guidance-properties-food_guidance.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-food_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/food_guidance")

### food_guidance Type

`object` ([Details](library-defs-regimen-properties-timing_guidance-properties-food_guidance.md))

## optional_split_windows



`optional_split_windows`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-optional_split_windows.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/optional_split_windows")

### optional_split_windows Type

`string[]`

## preferred_time_of_day



`preferred_time_of_day`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-preferred_time_of_day.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/preferred_time_of_day")

### preferred_time_of_day Type

`string`

## provenance



`provenance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-timing_guidance-properties-provenance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-provenance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/provenance")

### provenance Type

`object` ([Details](library-defs-regimen-properties-timing_guidance-properties-provenance.md))

## relative_events



`relative_events`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-timing_guidance-properties-relative_events-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-relative_events.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/relative_events")

### relative_events Type

`object[]` ([Details](library-defs-regimen-properties-timing_guidance-properties-relative_events-items.md))

## site_as_reported



`site_as_reported`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-site_as_reported.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/site_as_reported")

### site_as_reported Type

`string`

## spacing



`spacing`

* is optional

* Type: `null`, the value must be null

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-spacing.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/spacing")

### spacing Type

`null`, the value must be null

## spacing_between_components



`spacing_between_components`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-timing_guidance-properties-spacing_between_components.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-spacing_between_components.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/spacing_between_components")

### spacing_between_components Type

`object` ([Details](library-defs-regimen-properties-timing_guidance-properties-spacing_between_components.md))

## spacing_between_doses



`spacing_between_doses`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-timing_guidance-properties-spacing_between_doses.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-spacing_between_doses.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/spacing_between_doses")

### spacing_between_doses Type

`object` ([Details](library-defs-regimen-properties-timing_guidance-properties-spacing_between_doses.md))

## suggested_clock_times



`suggested_clock_times`

* is optional

* Type: unknown\[]

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance-properties-suggested_clock_times.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance/properties/suggested_clock_times")

### suggested_clock_times Type

unknown\[]

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
