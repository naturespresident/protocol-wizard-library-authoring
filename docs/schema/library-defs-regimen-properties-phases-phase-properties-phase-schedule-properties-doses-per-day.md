# Doses per day Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/doses_per_day
```

Number of administrations on each dosing day, from 1 through 1440, or null when unreported.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## doses_per_day Type

`integer` ([Doses per day](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-doses-per-day.md))

## doses_per_day Constraints

**maximum**: the value of this number must smaller than or equal to: `1440`

**minimum**: the value of this number must greater than or equal to: `1`
