# Product kind Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind
```

Classifies the identity as a product, blend, other item, or unresolved item. Use one of the exact listed values.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## kind Type

`string` ([Product kind](library-defs-product-properties-product-kind.md))

## kind Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"product"`    |             |
| `"blend"`      |             |
| `"other"`      |             |
| `"unresolved"` |             |
