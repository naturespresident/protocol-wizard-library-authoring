# Dose basis Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/basis
```

How to interpret the quantity, such as per administration, a daily total, a component amount, or a body-weight amount. This label does not convert quantities or choose a personal dose.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## basis Type

`string` ([Dose basis](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-basis.md))

## basis Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"total_product"`       |             |
| `"per_administration"`  |             |
| `"biological_activity"` |             |
| `"component"`           |             |
| `"body_weight"`         |             |
| `"daily_total"`         |             |
| `"weekly_total"`        |             |
| `"per_session"`         |             |
| `"not_reported"`        |             |
