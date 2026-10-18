# Schedule pattern Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/schedule/properties/pattern
```

Describes daily, interval, selected weekdays, weekly frequency, as-needed, or source-described use. Users must choose a valid personal schedule before saving.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## pattern Type

`string` ([Schedule pattern](library-defs-regimen-properties-phases-phase-properties-phase-schedule-properties-schedule-pattern.md))

## pattern Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                | Explanation |
| :------------------- | :---------- |
| `"daily"`            |             |
| `"every_n_days"`     |             |
| `"weekdays"`         |             |
| `"times_per_week"`   |             |
| `"as_needed"`        |             |
| `"source_described"` |             |
