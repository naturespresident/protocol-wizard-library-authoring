# Phases Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases
```

Required, nonempty list of routine stages in source order. Each stage needs a name, duration, dose, and schedule.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## phases Type

`object[]` ([Phase](library-defs-regimen-properties-phases-phase.md))

## phases Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
