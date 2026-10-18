# Catalog version Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/catalogVersion
```

Content version marker. Use the integer 1 during development; the app detects content updates by SHA-256 digest.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## catalogVersion Type

`integer` ([Catalog version](library-properties-catalog-version.md))

## catalogVersion Constraints

**constant**: the value of this property must be equal to:

```json
1
```
