# Suggested dose times Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/suggested_times
```

Local 24-hour times in HH:mm format. An empty array leaves times for the user to choose; importing does not schedule reminders.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## suggested_times Type

`string[]` ([Local dose time](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-suggested-dose-times-local-dose-time.md))
