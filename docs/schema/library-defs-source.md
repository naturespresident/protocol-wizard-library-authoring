# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## source Type

`object` ([Details](library-defs-source.md))

# source Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                        |
| :-------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                   | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")                               |
| [url](#url)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")                 |
| [title](#title)             | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")             |
| [publisher](#publisher)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")     |
| [type](#type)               | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")               |
| [publishedAt](#publishedat) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publishedat.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt") |

## id



`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")

### id Type

`string`

### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## url

HTTP or HTTPS source URL without embedded credentials. The app also validates the parsed URL.

`url`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")

### url Type

`string`

### url Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https?://[^\s/@]+(?:[/:?#][^\s]*)?$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3F%3A%2F%2F%5B%5E%5Cs%2F%40%5D%2B\(%3F%3A%5B%2F%3A%3F%23%5D%5B%5E%5Cs%5D*\)%3F%24 "try regular expression with regexr.com")

## title



`title`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")

### title Type

`string`

## publisher



`publisher`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")

### publisher Type

`string`

## type

Free-form source category; common values are shown as examples.

`type`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")

### type Type

`string`

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



`publishedAt`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publishedat.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt")

### publishedAt Type

`string`
