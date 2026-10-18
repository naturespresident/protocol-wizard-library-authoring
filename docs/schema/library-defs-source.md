# Source Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source
```

A bibliographic record with a stable ID and an HTTP or HTTPS URL. Citations use this ID to link supporting material to a product or protocol.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## source Type

`object` ([Source](library-defs-source.md))

# source Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :-------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                   | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")                               |
| [url](#url)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")               |
| [title](#title)             | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")           |
| [publisher](#publisher)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")          |
| [type](#type)               | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")             |
| [publishedAt](#publishedat) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publication-date.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt") |

## id

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`id`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")

### id Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## url

HTTP or HTTPS source URL without embedded credentials. The app also checks the parsed URL; it does not fetch the source during import.

`url`

* is required

* Type: `string` ([Source URL](library-defs-source-properties-source-url.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")

### url Type

`string` ([Source URL](library-defs-source-properties-source-url.md))

### url Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https?://[^\s/@]+(?:[/:?#][^\s]*)?$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3F%3A%2F%2F%5B%5E%5Cs%2F%40%5D%2B\(%3F%3A%5B%2F%3A%3F%23%5D%5B%5E%5Cs%5D*\)%3F%24 "try regular expression with regexr.com")

## title

Display title of the source material.

`title`

* is required

* Type: `string` ([Source title](library-defs-source-properties-source-title.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")

### title Type

`string` ([Source title](library-defs-source-properties-source-title.md))

## publisher

Optional authoring organization or publisher name. Omit or set to null when unavailable.

`publisher`

* is optional

* Type: `string` ([Publisher](library-defs-source-properties-publisher.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")

### publisher Type

`string` ([Publisher](library-defs-source-properties-publisher.md))

## type

Free-form source category. The listed examples are suggestions, not a fixed set of choices.

`type`

* is required

* Type: `string` ([Source type](library-defs-source-properties-source-type.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")

### type Type

`string` ([Source type](library-defs-source-properties-source-type.md))

### type Examples

```json
"human_study"
```

```json
"animal_study"
```

```json
"lab_study"
```

```json
"regulatory_label"
```

```json
"manufacturer"
```

```json
"clinical_guidance"
```

```json
"other"
```

## publishedAt

Optional publication date retained as text, without date parsing or a required date format. Omit or set to null when unavailable.

`publishedAt`

* is optional

* Type: `string` ([Publication date](library-defs-source-properties-publication-date.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publication-date.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt")

### publishedAt Type

`string` ([Publication date](library-defs-source-properties-publication-date.md))
