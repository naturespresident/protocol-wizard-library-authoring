# Window end Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window/properties/end
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## end Type

`string` ([Window end](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-end.md))

## end Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?:[01][0-9]|2[0-3]):[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F%3A%5B01%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")
