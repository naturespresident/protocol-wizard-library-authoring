# Regimen type Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type
```

Use single_compound for one product, premixed_blend for a prepared blend, or stack for separate components. Stacks are viewable reference content and cannot be activated as a single personal protocol.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## regimen_type Type

`string` ([Regimen type](library-defs-regimen-properties-regimen-type.md))

## regimen_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"single_compound"` |             |
| `"premixed_blend"`  |             |
| `"stack"`           |             |
