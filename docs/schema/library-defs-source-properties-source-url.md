# Source URL Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url
```

HTTP or HTTPS source URL without embedded credentials. The app also checks the parsed URL; it does not fetch the source during import.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## url Type

`string` ([Source URL](library-defs-source-properties-source-url.md))

## url Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https?://[^\s/@]+(?:[/:?#][^\s]*)?$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3F%3A%2F%2F%5B%5E%5Cs%2F%40%5D%2B\(%3F%3A%5B%2F%3A%3F%23%5D%5B%5E%5Cs%5D*\)%3F%24 "try regular expression with regexr.com")
