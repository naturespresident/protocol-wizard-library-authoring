# Timing guidance Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing
```

Optional dose-timing guidance for this product. The app shows it as a recommendation on the Schedule step and never applies it automatically.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## timing Type

`object` ([Timing guidance](library-defs-product-properties-timing-guidance.md))

# timing Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                    |
| :---------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [tags](#tags)     | `array`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-timing-tags.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/tags")        |
| [window](#window) | `object` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-suggested-window.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window") |
| [note](#note)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-timing-note.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/note")        |

## tags

Any of: morning, midday, evening, bedtime, empty_stomach, with_food, before_exercise, after_exercise. Unknown tags are ignored.

`tags`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-timing-tags.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/tags")

### tags Type

`string[]`

## window

24-hour HH:mm start and end. The end may be earlier than the start, meaning the window crosses midnight.

`window`

* is optional

* Type: `object` ([Suggested window](library-defs-product-properties-timing-guidance-properties-suggested-window.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-suggested-window.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/window")

### window Type

`object` ([Suggested window](library-defs-product-properties-timing-guidance-properties-suggested-window.md))

## note

Shown under the recommendation. Up to 500 characters.

`note`

* is optional

* Type: `string` ([Timing note](library-defs-product-properties-timing-guidance-properties-timing-note.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-timing-guidance-properties-timing-note.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/timing/properties/note")

### note Type

`string` ([Timing note](library-defs-product-properties-timing-guidance-properties-timing-note.md))

### note Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")
