# ISO weekday Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/weekdays/items
```

One integer from 1 for Monday through 7 for Sunday.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## items Type

`integer` ([ISO weekday](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-dosing-weekdays-iso-weekday.md))

## items Constraints

**maximum**: the value of this number must smaller than or equal to: `7`

**minimum**: the value of this number must greater than or equal to: `1`
