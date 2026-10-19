# Minimum dose Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/minimum
```

Lower end of a source-reported dose range as a plain decimal string, or null when unknown. The user chooses a concrete personal dose.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## minimum Type

`string` ([Minimum dose](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose.md))

one (and only one) of

* [Untitled null in Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose-oneof-0.md "check type definition")

* [Decimal amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-minimum-dose-oneof-decimal-amount.md "check type definition")
