# Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json
```

One product and its protocols. The app validates the selection, installed component dependencies, and the merged library before installation.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json](../../template/library.schema.json "open original schema") |

## Protocol Wizard product library — schema version 1 Type

`object` ([Protocol Wizard product library — schema version 1](library.md))

# Protocol Wizard product library — schema version 1 Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                     |
| :-------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [$schema](#schema)                | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-schema.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/$schema")                |
| [schemaVersion](#schemaversion)   | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-schemaversion.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/schemaVersion")   |
| [catalogVersion](#catalogversion) | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-catalogversion.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/catalogVersion") |
| [items](#items)                   | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-items.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/items")                   |
| [protocols](#protocols)           | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-protocols.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/protocols")           |
| [sources](#sources)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-sources.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/sources")               |
| [citations](#citations)           | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-citations.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/citations")           |
| [categories](#categories)         | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-categories.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/categories")         |
| [methods](#methods)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-methods.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/methods")               |

## $schema

Optional editor hint pointing to this schema.

`$schema`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-schema.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/$schema")

### $schema Type

`string`

## schemaVersion



`schemaVersion`

* is required

* Type: `integer`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-schemaversion.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/schemaVersion")

### schemaVersion Type

`integer`

### schemaVersion Constraints

**constant**: the value of this property must be equal to:

```json
1
```

## catalogVersion



`catalogVersion`

* is required

* Type: `integer`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-catalogversion.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/catalogVersion")

### catalogVersion Type

`integer`

### catalogVersion Constraints

**constant**: the value of this property must be equal to:

```json
1
```

## items



`items`

* is required

* Type: `object[]` ([Details](library-defs-item.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-items.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/items")

### items Type

`object[]` ([Details](library-defs-item.md))

### items Constraints

**maximum number of items**: the maximum number of items for this array is: `1`

**minimum number of items**: the minimum number of items for this array is: `1`

## protocols



`protocols`

* is required

* Type: `object[]` ([Details](library-defs-protocol.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-protocols.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/protocols")

### protocols Type

`object[]` ([Details](library-defs-protocol.md))

### protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## sources



`sources`

* is required

* Type: `object[]` ([Details](library-defs-source.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-sources.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/sources")

### sources Type

`object[]` ([Details](library-defs-source.md))

## citations



`citations`

* is required

* Type: `object[]` ([Details](library-defs-citation.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-citations.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/citations")

### citations Type

`object[]` ([Details](library-defs-citation.md))

## categories



`categories`

* is required

* Type: `object[]` ([Details](library-defs-category.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-categories.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/categories")

### categories Type

`object[]` ([Details](library-defs-category.md))

## methods



`methods`

* is required

* Type: `object[]` ([Details](library-defs-method.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-methods.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/methods")

### methods Type

`object[]` ([Details](library-defs-method.md))

# Protocol Wizard product library — schema version 1 Definitions

## Definitions group nonblank

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/nonblank"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group methodID

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/methodID"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group item

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item"}
```

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                         | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-item-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/id")                         |
| [name](#name)                     | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-item-properties-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/name")                     |
| [aliases](#aliases)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-item-properties-aliases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/aliases")               |
| [kind](#kind)                     | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-item-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind")                     |
| [identityStatus](#identitystatus) | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-item-properties-identitystatus.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/identityStatus") |
| [categoryID](#categoryid)         | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-item-properties-categoryid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/categoryID")         |
| [benefits](#benefits)             | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-item-properties-benefits.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/benefits")             |

### id



`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/id")

#### id Type

`string`

#### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### name



`name`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/name")

#### name Type

`string`

#### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### aliases



`aliases`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-aliases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/aliases")

#### aliases Type

`string[]`

### kind



`kind`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind")

#### kind Type

`string`

#### kind Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"product"`    |             |
| `"blend"`      |             |
| `"other"`      |             |
| `"unresolved"` |             |

### identityStatus



`identityStatus`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-identitystatus.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/identityStatus")

#### identityStatus Type

`string`

#### identityStatus Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"resolved"`           |             |
| `"needs_confirmation"` |             |

### categoryID



`categoryID`

* is optional

* Type: `integer`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-categoryid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/categoryID")

#### categoryID Type

`integer`

### benefits



`benefits`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-item-properties-benefits.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/benefits")

#### benefits Type

`string`

## Definitions group protocol

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol"}
```

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id-1)                     | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")                       |
| [productID](#productid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")         |
| [title](#title)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")                 |
| [purpose](#purpose)             | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")             |
| [methodID](#methodid)           | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-methodid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")           |
| [population](#population)       | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-population.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population")       |
| [evidenceNotes](#evidencenotes) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidencenotes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes") |
| [regimen](#regimen)             | `object` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")                                 |

### id



`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")

#### id Type

`string`

#### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### productID



`productID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")

#### productID Type

`string`

#### productID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### title



`title`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")

#### title Type

`string`

#### title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### purpose



`purpose`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")

#### purpose Type

`string`

### methodID



`methodID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-methodid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")

#### methodID Type

`string`

#### methodID Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"unspecified"`   |             |
| `"subcutaneous"`  |             |
| `"intramuscular"` |             |
| `"oral"`          |             |
| `"intranasal"`    |             |
| `"topical"`       |             |
| `"other"`         |             |

### population



`population`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-population.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population")

#### population Type

`string`

### evidenceNotes



`evidenceNotes`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidencenotes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes")

#### evidenceNotes Type

`string`

### regimen

Structured reference content. Required core fields are version and phases. Optional metadata fields shown here are retained for display; additional metadata is allowed and does not automatically create a personal schedule.

`regimen`

* is required

* Type: `object` ([Details](library-defs-regimen.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")

#### regimen Type

`object` ([Details](library-defs-regimen.md))

## Definitions group source

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source"}
```

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                        |
| :-------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-2)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")                   |
| [url](#url)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")                 |
| [title](#title-1)           | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")             |
| [publisher](#publisher)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")     |
| [type](#type)               | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")               |
| [publishedAt](#publishedat) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publishedat.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt") |

### id



`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")

#### id Type

`string`

#### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### url

HTTP or HTTPS source URL without embedded credentials. The app also validates the parsed URL.

`url`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")

#### url Type

`string`

#### url Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https?://[^\s/@]+(?:[/:?#][^\s]*)?$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3F%3A%2F%2F%5B%5E%5Cs%2F%40%5D%2B\(%3F%3A%5B%2F%3A%3F%23%5D%5B%5E%5Cs%5D*\)%3F%24 "try regular expression with regexr.com")

### title



`title`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")

#### title Type

`string`

### publisher



`publisher`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")

#### publisher Type

`string`

### type

Free-form source category; common values are shown as examples.

`type`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")

#### type Type

`string`

#### type Examples

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

### publishedAt



`publishedAt`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publishedat.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt")

#### publishedAt Type

`string`

## Definitions group citation

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :---------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocolID](#protocolid)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocolid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID")     |
| [productID](#productid-1)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")       |
| [sourceID](#sourceid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-sourceid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")         |
| [locator](#locator)           | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-locator.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")           |
| [evidenceNote](#evidencenote) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidencenote.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote") |
| [supports](#supports)         | `array`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supports.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")         |

### protocolID



`protocolID`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocolid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID")

#### protocolID Type

`string`

### productID



`productID`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")

#### productID Type

`string`

### sourceID



`sourceID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-sourceid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")

#### sourceID Type

`string`

#### sourceID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### locator



`locator`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-locator.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")

#### locator Type

`string`

### evidenceNote



`evidenceNote`

* is optional

* Type: `string`

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidencenote.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote")

#### evidenceNote Type

`string`

### supports



`supports`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supports.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")

#### supports Type

`string[]`

## Definitions group category

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category"}
```

| Property        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :-------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id-3)     | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-category-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/id")     |
| [name](#name-1) | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-category-properties-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/name") |

### id



`id`

* is required

* Type: `integer`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-category-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/id")

#### id Type

`integer`

### name



`name`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-category-properties-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/name")

#### name Type

`string`

#### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## Definitions group method

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method"}
```

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                          |
| :-------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-4)     | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-method-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/id")     |
| [name](#name-2) | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-method-properties-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/name") |

### id



`id`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-method-properties-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/id")

#### id Type

`string`

#### id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"unspecified"`   |             |
| `"subcutaneous"`  |             |
| `"intramuscular"` |             |
| `"oral"`          |             |
| `"intranasal"`    |             |
| `"topical"`       |             |
| `"other"`         |             |

### name



`name`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-method-properties-name.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/name")

#### name Type

`string`

#### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## Definitions group regimen

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen"}
```

| Property                                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cautions](#cautions)                                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cautions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cautions")                                           |
| [clinical_context](#clinical_context)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-clinical_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/clinical_context")                           |
| [component_regimens](#component_regimens)                       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-component_regimens.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/component_regimens")                       |
| [conditional_escalation](#conditional_escalation)               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-conditional_escalation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/conditional_escalation")               |
| [cycle_guidance](#cycle_guidance)                               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cycle_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cycle_guidance")                               |
| [dose_arm_context](#dose_arm_context)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-dose_arm_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/dose_arm_context")                           |
| [evidence_context](#evidence_context)                           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-evidence_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/evidence_context")                           |
| [formulation](#formulation)                                     | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-formulation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/formulation")                                     |
| [handling_guidance](#handling_guidance)                         | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-handling_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/handling_guidance")                         |
| [maintenance_alternatives](#maintenance_alternatives)           | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_alternatives")           |
| [maintenance_option](#maintenance_option)                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_option.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_option")                       |
| [notes](#notes)                                                 | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/notes")                                                 |
| [off_period](#off_period)                                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-off_period.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/off_period")                                       |
| [optional_extension](#optional_extension)                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension")                       |
| [phase_alternatives](#phase_alternatives)                       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives")                       |
| [phases](#phases)                                               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases")                                               |
| [preparation_options](#preparation_options)                     | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options")                     |
| [reference_urls](#reference_urls)                               | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-reference_urls.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/reference_urls")                               |
| [regimen_type](#regimen_type)                                   | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen_type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type")                                   |
| [repeat_guidance](#repeat_guidance)                             | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-repeat_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/repeat_guidance")                             |
| [schedule_alternative](#schedule_alternative)                   | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-schedule_alternative.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/schedule_alternative")                   |
| [source_calendar_duration](#source_calendar_duration)           | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_calendar_duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_calendar_duration")           |
| [source_upper_community_limits](#source_upper_community_limits) | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits") |
| [source_upper_limit](#source_upper_limit)                       | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_limit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_limit")                       |
| [storage](#storage)                                             | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage")                                             |
| [study_exposure_context](#study_exposure_context)               | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-study_exposure_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/study_exposure_context")               |
| [target_rule](#target_rule)                                     | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-target_rule.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/target_rule")                                     |
| [timing_guidance](#timing_guidance)                             | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance")                             |
| [trial_arms](#trial_arms)                                       | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_arms.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_arms")                                       |
| [trial_context](#trial_context)                                 | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context")                                 |
| [trial_target_options](#trial_target_options)                   | `object`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_target_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_target_options")                   |
| [unresolved_fields](#unresolved_fields)                         | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-unresolved_fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/unresolved_fields")                         |
| [version](#version)                                             | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/version")                                             |
| [weight_examples](#weight_examples)                             | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples")                             |
| Additional Properties                                           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                         |

### cautions



`cautions`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-cautions.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cautions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cautions")

#### cautions Type

`object` ([Details](library-defs-regimen-properties-cautions.md))

### clinical_context



`clinical_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-clinical_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-clinical_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/clinical_context")

#### clinical_context Type

`object` ([Details](library-defs-regimen-properties-clinical_context.md))

### component_regimens



`component_regimens`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-component_regimens-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-component_regimens.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/component_regimens")

#### component_regimens Type

`object[]` ([Details](library-defs-regimen-properties-component_regimens-items.md))

### conditional_escalation



`conditional_escalation`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-conditional_escalation.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-conditional_escalation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/conditional_escalation")

#### conditional_escalation Type

`object` ([Details](library-defs-regimen-properties-conditional_escalation.md))

### cycle_guidance



`cycle_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-cycle_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cycle_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cycle_guidance")

#### cycle_guidance Type

`object` ([Details](library-defs-regimen-properties-cycle_guidance.md))

### dose_arm_context



`dose_arm_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-dose_arm_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-dose_arm_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/dose_arm_context")

#### dose_arm_context Type

`object` ([Details](library-defs-regimen-properties-dose_arm_context.md))

### evidence_context



`evidence_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-evidence_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-evidence_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/evidence_context")

#### evidence_context Type

`object` ([Details](library-defs-regimen-properties-evidence_context.md))

### formulation



`formulation`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-formulation.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-formulation.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/formulation")

#### formulation Type

`object` ([Details](library-defs-regimen-properties-formulation.md))

### handling_guidance



`handling_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-handling_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-handling_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/handling_guidance")

#### handling_guidance Type

`object` ([Details](library-defs-regimen-properties-handling_guidance.md))

### maintenance_alternatives



`maintenance_alternatives`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-maintenance_alternatives-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_alternatives")

#### maintenance_alternatives Type

`object[]` ([Details](library-defs-regimen-properties-maintenance_alternatives-items.md))

### maintenance_option



`maintenance_option`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-maintenance_option.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-maintenance_option.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/maintenance_option")

#### maintenance_option Type

`object` ([Details](library-defs-regimen-properties-maintenance_option.md))

### notes



`notes`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/notes")

#### notes Type

`string`

### off_period



`off_period`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-off_period.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-off_period.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/off_period")

#### off_period Type

`object` ([Details](library-defs-regimen-properties-off_period.md))

### optional_extension



`optional_extension`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-optional_extension.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-optional_extension.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/optional_extension")

#### optional_extension Type

`object` ([Details](library-defs-regimen-properties-optional_extension.md))

### phase_alternatives



`phase_alternatives`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-phase_alternatives-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phase_alternatives.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phase_alternatives")

#### phase_alternatives Type

`object[]` ([Details](library-defs-regimen-properties-phase_alternatives-items.md))

### phases



`phases`

* is required

* Type: `object[]` ([Details](library-defs-regimen-properties-phases-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases")

#### phases Type

`object[]` ([Details](library-defs-regimen-properties-phases-items.md))

#### phases Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

### preparation_options



`preparation_options`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-preparation_options-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options")

#### preparation_options Type

`object[]` ([Details](library-defs-regimen-properties-preparation_options-items.md))

### reference_urls



`reference_urls`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-reference_urls-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-reference_urls.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/reference_urls")

#### reference_urls Type

`object[]` ([Details](library-defs-regimen-properties-reference_urls-items.md))

### regimen_type

Stacks are viewable reference content; they cannot be activated as a single personal protocol.

`regimen_type`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen_type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type")

#### regimen_type Type

`string`

#### regimen_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"single_compound"` |             |
| `"premixed_blend"`  |             |
| `"stack"`           |             |

### repeat_guidance



`repeat_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-repeat_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-repeat_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/repeat_guidance")

#### repeat_guidance Type

`object` ([Details](library-defs-regimen-properties-repeat_guidance.md))

### schedule_alternative



`schedule_alternative`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-schedule_alternative.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-schedule_alternative.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/schedule_alternative")

#### schedule_alternative Type

`object` ([Details](library-defs-regimen-properties-schedule_alternative.md))

### source_calendar_duration



`source_calendar_duration`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-source_calendar_duration.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_calendar_duration.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_calendar_duration")

#### source_calendar_duration Type

`object` ([Details](library-defs-regimen-properties-source_calendar_duration.md))

### source_upper_community_limits



`source_upper_community_limits`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-source_upper_community_limits.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_community_limits.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_community_limits")

#### source_upper_community_limits Type

`object` ([Details](library-defs-regimen-properties-source_upper_community_limits.md))

### source_upper_limit



`source_upper_limit`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-source_upper_limit.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-source_upper_limit.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/source_upper_limit")

#### source_upper_limit Type

`object` ([Details](library-defs-regimen-properties-source_upper_limit.md))

### storage



`storage`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-storage.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage")

#### storage Type

`object` ([Details](library-defs-regimen-properties-storage.md))

### study_exposure_context



`study_exposure_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-study_exposure_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-study_exposure_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/study_exposure_context")

#### study_exposure_context Type

`object` ([Details](library-defs-regimen-properties-study_exposure_context.md))

### target_rule



`target_rule`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-target_rule.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/target_rule")

#### target_rule Type

`string`

### timing_guidance



`timing_guidance`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-timing_guidance.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-timing_guidance.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/timing_guidance")

#### timing_guidance Type

`object` ([Details](library-defs-regimen-properties-timing_guidance.md))

### trial_arms



`trial_arms`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-trial_arms-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_arms.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_arms")

#### trial_arms Type

`object[]` ([Details](library-defs-regimen-properties-trial_arms-items.md))

### trial_context



`trial_context`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-trial_context.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_context")

#### trial_context Type

`object` ([Details](library-defs-regimen-properties-trial_context.md))

### trial_target_options



`trial_target_options`

* is optional

* Type: `object` ([Details](library-defs-regimen-properties-trial_target_options.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-trial_target_options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/trial_target_options")

#### trial_target_options Type

`object` ([Details](library-defs-regimen-properties-trial_target_options.md))

### unresolved_fields



`unresolved_fields`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-unresolved_fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/unresolved_fields")

#### unresolved_fields Type

`string[]`

### version



`version`

* is required

* Type: `integer`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/version")

#### version Type

`integer`

#### version Constraints

**constant**: the value of this property must be equal to:

```json
1
```

### weight_examples



`weight_examples`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-weight_examples-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples")

#### weight_examples Type

`object[]` ([Details](library-defs-regimen-properties-weight_examples-items.md))

### Additional Properties

Additional properties are allowed and do not have to follow a specific schema
