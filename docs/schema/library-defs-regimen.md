# Regimen Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen
```

The reusable dose, duration, and schedule content of a protocol. Version and phases are required. Optional source metadata supplies context; the editor only copies settings it understands.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## regimen Type

`object` ([Regimen](library-defs-regimen.md))

# regimen Properties

| Property                                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cautions](#cautions)                                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cautions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cautions")                                           |
| [clinical_context](#clinical_context)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-clinical_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/clinical_context")                           |
| [component_regimens](#component_regimens)                       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-component_regimens.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/component_regimens")                       |
| [conditional_escalation](#conditional_escalation)               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-conditional_escalation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/conditional_escalation")               |
| [cycle_guidance](#cycle_guidance)                               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cycle_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cycle_guidance")                               |
| [dose_arm_context](#dose_arm_context)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-dose_arm_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/dose_arm_context")                           |
| [evidence_context](#evidence_context)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-evidence_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/evidence_context")                           |
| [formulation](#formulation)                                     | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-formulation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/formulation")                                     |
| [handling_guidance](#handling_guidance)                         | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-handling_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/handling_guidance")                         |
| [maintenance_alternatives](#maintenance_alternatives)           | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_alternatives")           |
| [maintenance_option](#maintenance_option)                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_option.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_option")                       |
| [notes](#notes)                                                 | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/notes")                                                 |
| [off_period](#off_period)                                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-off_period.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/off_period")                                       |
| [optional_extension](#optional_extension)                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension")                       |
| [phase_alternatives](#phase_alternatives)                       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives")                       |
| [phases](#phases)                                               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases")                                               |
| [preparation_options](#preparation_options)                     | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options")                     |
| [reference_urls](#reference_urls)                               | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-reference_urls.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/reference_urls")                               |
| [regimen_type](#regimen_type)                                   | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type")                                   |
| [repeat_guidance](#repeat_guidance)                             | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-repeat_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/repeat_guidance")                             |
| [schedule_alternative](#schedule_alternative)                   | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-schedule_alternative.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/schedule_alternative")                   |
| [source_calendar_duration](#source_calendar_duration)           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_calendar_duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_calendar_duration")           |
| [source_upper_community_limits](#source_upper_community_limits) | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits") |
| [source_upper_limit](#source_upper_limit)                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_limit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_limit")                       |
| [storage](#storage)                                             | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage")                                             |
| [study_exposure_context](#study_exposure_context)               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-study_exposure_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/study_exposure_context")               |
| [target_rule](#target_rule)                                     | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-target_rule.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/target_rule")                                     |
| [timing_guidance](#timing_guidance)                             | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance")                             |
| [trial_arms](#trial_arms)                                       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_arms.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_arms")                                       |
| [trial_context](#trial_context)                                 | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context")                                 |
| [trial_target_options](#trial_target_options)                   | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_target_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_target_options")                   |
| [unresolved_fields](#unresolved_fields)                         | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-unresolved_fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/unresolved_fields")                         |
| [version](#version)                                             | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/version")                                     |
| [weight_examples](#weight_examples)                             | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples")                             |
| Additional Properties                                           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                         |

## cautions

Optional source context for exclusions, interactions, monitoring, and reported effects. This reference metadata does not create alerts or monitoring tasks.

`cautions`

* is optional

* Type: `object` ([Cautions](library-defs-regimen-properties-cautions.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cautions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cautions")

### cautions Type

`object` ([Cautions](library-defs-regimen-properties-cautions.md))

## clinical_context



`clinical_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-clinical_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-clinical_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/clinical_context")

### clinical_context Type

`object` ([Details](library-defs-regimen-properties-clinical_context.md))

## component_regimens



`component_regimens`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-component_regimens-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-component_regimens.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/component_regimens")

### component_regimens Type

`object[]` ([Details](library-defs-regimen-properties-component_regimens-items.md))

## conditional_escalation



`conditional_escalation`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-conditional_escalation.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-conditional_escalation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/conditional_escalation")

### conditional_escalation Type

`object` ([Details](library-defs-regimen-properties-conditional_escalation.md))

## cycle_guidance



`cycle_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-cycle_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cycle_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cycle_guidance")

### cycle_guidance Type

`object` ([Details](library-defs-regimen-properties-cycle_guidance.md))

## dose_arm_context



`dose_arm_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-dose_arm_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-dose_arm_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/dose_arm_context")

### dose_arm_context Type

`object` ([Details](library-defs-regimen-properties-dose_arm_context.md))

## evidence_context



`evidence_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-evidence_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-evidence_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/evidence_context")

### evidence_context Type

`object` ([Details](library-defs-regimen-properties-evidence_context.md))

## formulation



`formulation`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-formulation.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-formulation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/formulation")

### formulation Type

`object` ([Details](library-defs-regimen-properties-formulation.md))

## handling_guidance



`handling_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-handling_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-handling_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/handling_guidance")

### handling_guidance Type

`object` ([Details](library-defs-regimen-properties-handling_guidance.md))

## maintenance_alternatives



`maintenance_alternatives`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-maintenance_alternatives-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_alternatives")

### maintenance_alternatives Type

`object[]` ([Details](library-defs-regimen-properties-maintenance_alternatives-items.md))

## maintenance_option



`maintenance_option`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-maintenance_option.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_option.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_option")

### maintenance_option Type

`object` ([Details](library-defs-regimen-properties-maintenance_option.md))

## notes



`notes`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/notes")

### notes Type

`string`

## off_period



`off_period`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-off_period.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-off_period.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/off_period")

### off_period Type

`object` ([Details](library-defs-regimen-properties-off_period.md))

## optional_extension



`optional_extension`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-optional_extension.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension")

### optional_extension Type

`object` ([Details](library-defs-regimen-properties-optional_extension.md))

## phase_alternatives



`phase_alternatives`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-phase_alternatives-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives")

### phase_alternatives Type

`object[]` ([Details](library-defs-regimen-properties-phase_alternatives-items.md))

## phases

Required, nonempty list of routine stages in source order. Each stage needs a name, duration, dose, and schedule.

`phases`

* is required

* Type: `object[]` ([Phase](library-defs-regimen-properties-phases-phase.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases")

### phases Type

`object[]` ([Phase](library-defs-regimen-properties-phases-phase.md))

### phases Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## preparation_options

Optional alternatives for product form, amounts, diluent, and concentration. Keep quantities and units explicit; the app retains this reference metadata without preparing a personal product.

`preparation_options`

* is optional

* Type: `object[]` ([Preparation option](library-defs-regimen-properties-preparation-options-preparation-option.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options")

### preparation_options Type

`object[]` ([Preparation option](library-defs-regimen-properties-preparation-options-preparation-option.md))

## reference_urls



`reference_urls`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-reference_urls-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-reference_urls.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/reference_urls")

### reference_urls Type

`object[]` ([Details](library-defs-regimen-properties-reference_urls-items.md))

## regimen_type

Use single_compound for one product, premixed_blend for a prepared blend, or stack for separate components. Stacks are viewable reference content and cannot be activated as a single personal protocol.

`regimen_type`

* is optional

* Type: `string` ([Regimen type](library-defs-regimen-properties-regimen-type.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type")

### regimen_type Type

`string` ([Regimen type](library-defs-regimen-properties-regimen-type.md))

### regimen_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"single_compound"` |             |
| `"premixed_blend"`  |             |
| `"stack"`           |             |

## repeat_guidance



`repeat_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-repeat_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-repeat_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/repeat_guidance")

### repeat_guidance Type

`object` ([Details](library-defs-regimen-properties-repeat_guidance.md))

## schedule_alternative



`schedule_alternative`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-schedule_alternative.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-schedule_alternative.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/schedule_alternative")

### schedule_alternative Type

`object` ([Details](library-defs-regimen-properties-schedule_alternative.md))

## source_calendar_duration



`source_calendar_duration`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-source_calendar_duration.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_calendar_duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_calendar_duration")

### source_calendar_duration Type

`object` ([Details](library-defs-regimen-properties-source_calendar_duration.md))

## source_upper_community_limits



`source_upper_community_limits`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-source_upper_community_limits.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits")

### source_upper_community_limits Type

`object` ([Details](library-defs-regimen-properties-source_upper_community_limits.md))

## source_upper_limit



`source_upper_limit`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-source_upper_limit.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_limit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_limit")

### source_upper_limit Type

`object` ([Details](library-defs-regimen-properties-source_upper_limit.md))

## storage

Optional source-reported storage, handling, and discard guidance. This reference metadata does not set personal expiry dates or reminders.

`storage`

* is optional

* Type: `object` ([Storage](library-defs-regimen-properties-storage.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage")

### storage Type

`object` ([Storage](library-defs-regimen-properties-storage.md))

## study_exposure_context



`study_exposure_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-study_exposure_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-study_exposure_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/study_exposure_context")

### study_exposure_context Type

`object` ([Details](library-defs-regimen-properties-study_exposure_context.md))

## target_rule



`target_rule`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-target_rule.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/target_rule")

### target_rule Type

`string`

## timing_guidance



`timing_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-timing_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance")

### timing_guidance Type

`object` ([Details](library-defs-regimen-properties-timing_guidance.md))

## trial_arms



`trial_arms`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-trial_arms-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_arms.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_arms")

### trial_arms Type

`object[]` ([Details](library-defs-regimen-properties-trial_arms-items.md))

## trial_context



`trial_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-trial_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context")

### trial_context Type

`object` ([Details](library-defs-regimen-properties-trial_context.md))

## trial_target_options



`trial_target_options`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-trial_target_options.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_target_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_target_options")

### trial_target_options Type

`object` ([Details](library-defs-regimen-properties-trial_target_options.md))

## unresolved_fields



`unresolved_fields`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-unresolved_fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/unresolved_fields")

### unresolved_fields Type

`string[]`

## version

Regimen format version. Use the integer 1 during development, including for content updates.

`version`

* is required

* Type: `integer` ([Regimen version](library-defs-regimen-properties-regimen-version.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/version")

### version Type

`integer` ([Regimen version](library-defs-regimen-properties-regimen-version.md))

### version Constraints

**constant**: the value of this property must be equal to:

```json
1
```

## weight_examples



`weight_examples`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-weight_examples-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples")

### weight_examples Type

`object[]` ([Details](library-defs-regimen-properties-weight_examples-items.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
