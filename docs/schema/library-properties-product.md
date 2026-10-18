# Product Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/items
```

Exactly one product identity. Include its reusable protocols in the protocols array; importing does not create a personal product or start a schedule.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## items Type

`object[]` ([Product](library-defs-product.md))

## items Constraints

**maximum number of items**: the maximum number of items for this array is: `1`

**minimum number of items**: the minimum number of items for this array is: `1`
