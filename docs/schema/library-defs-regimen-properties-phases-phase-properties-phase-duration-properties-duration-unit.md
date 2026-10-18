# Duration unit Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/unit
```

Unit for the duration amount and bounds: day, week, or calendar_month. Calendar months are retained as reference context.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## unit Type

`string` ([Duration unit](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-unit.md))

## unit Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"day"`            |             |
| `"week"`           |             |
| `"calendar_month"` |             |
