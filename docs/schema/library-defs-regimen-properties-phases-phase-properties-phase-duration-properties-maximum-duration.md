# Maximum duration Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/maximum
```

Upper duration bound in the stated unit, or null when unreported. A source range does not choose a personal duration.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## maximum Type

`integer` ([Maximum duration](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-maximum-duration.md))

## maximum Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`
