# Delivery method ID Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/methodID
```

An exact, lowercase delivery choice supported by the app. Use unspecified when the user should choose the method; a custom display label does not allow a new ID.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## methodID Type

`string` ([Delivery method ID](library-defs-delivery-method-id.md))

## methodID Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"unspecified"`   |             |
| `"subcutaneous"`  |             |
| `"intramuscular"` |             |
| `"oral"`          |             |
| `"intranasal"`    |             |
| `"topical"`       |             |
| `"other"`         |             |
