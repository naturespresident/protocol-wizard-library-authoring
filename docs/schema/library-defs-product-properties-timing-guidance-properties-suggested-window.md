# Suggested window Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window
```

24-hour HH:mm start and end. The end may be earlier than the start, meaning the window crosses midnight.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## window Type

`object` ([Suggested window](library-defs-product-properties-timing-guidance-properties-suggested-window.md))

# window Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                             |
| :-------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [start](#start) | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-start.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window/properties/start") |
| [end](#end)     | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-end.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window/properties/end")     |

## start



`start`

* is required

* Type: `string` ([Window start](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-start.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-start.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window/properties/start")

### start Type

`string` ([Window start](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-start.md))

### start Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?:[01][0-9]|2[0-3]):[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F%3A%5B01%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")

## end



`end`

* is required

* Type: `string` ([Window end](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-end.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-end.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window/properties/end")

### end Type

`string` ([Window end](library-defs-product-properties-timing-guidance-properties-suggested-window-properties-window-end.md))

### end Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?:[01][0-9]|2[0-3]):[0-5][0-9]$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F%3A%5B01%5D%5B0-9%5D%7C2%5B0-3%5D\)%3A%5B0-5%5D%5B0-9%5D%24 "try regular expression with regexr.com")
