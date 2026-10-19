# Dose amount Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/value
```

Single dose quantity as a plain decimal string, such as 0.25 or 500, or null when unknown. Use a dot for the decimal separator and no grouping commas or unit suffix.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## value Type

`string` ([Dose amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount.md))

one (and only one) of

* [Untitled null in Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount-oneof-0.md "check type definition")

* [Decimal amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-dose-amount-oneof-decimal-amount.md "check type definition")
