# Duration amount Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/duration/properties/value
```

Single duration amount in the stated unit. Use an integer from 1 through 365000, or null when unreported.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## value Type

`integer` ([Duration amount](library-defs-regimen-properties-phases-phase-properties-phase-duration-properties-duration-amount.md))

## value Constraints

**maximum**: the value of this number must smaller than or equal to: `365000`

**minimum**: the value of this number must greater than or equal to: `1`
