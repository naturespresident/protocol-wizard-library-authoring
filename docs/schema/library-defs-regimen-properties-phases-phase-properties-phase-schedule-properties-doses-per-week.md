# Doses per week Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/times_per_week
```

Source-reported weekly frequency from 1 through 7, or null when unreported. A weekly count alone does not select dosing weekdays.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## times_per_week Type

`integer` ([Doses per week](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-week.md))

## times_per_week Constraints

**maximum**: the value of this number must smaller than or equal to: `7`

**minimum**: the value of this number must greater than or equal to: `1`
