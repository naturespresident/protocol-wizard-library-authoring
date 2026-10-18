# Protocols Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/protocols
```

One or more reusable protocols for the included product. Each productID must equal items\[0].id. Users choose which protocols to import.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## protocols Type

`object[]` ([Protocol](library-defs-protocol.md))

## protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
