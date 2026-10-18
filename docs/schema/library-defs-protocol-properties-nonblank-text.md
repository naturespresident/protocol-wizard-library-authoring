# Nonblank text Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id
```

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## id Type

`string` ([Nonblank text](library-defs-protocol-properties-nonblank-text.md))

## id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")
