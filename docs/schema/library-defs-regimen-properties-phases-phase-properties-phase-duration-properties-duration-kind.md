# Duration kind Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/kind
```

Describes a fixed length, a range, a minimum or maximum, an ongoing or unreported duration, or a source-defined target. Only fixed day or week lengths can seed a concrete editor duration.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## kind Type

`string` ([Duration kind](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-kind.md))

## kind Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"fixed"`               |             |
| `"range"`               |             |
| `"minimum"`             |             |
| `"maximum"`             |             |
| `"ongoing"`             |             |
| `"unreported"`          |             |
| `"target_dose"`         |             |
| `"target_dose_choices"` |             |
