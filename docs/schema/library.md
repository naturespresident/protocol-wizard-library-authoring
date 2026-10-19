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

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                         |
| :-------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [$schema](#schema)                | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-editor-schema-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/$schema")         |
| [schemaVersion](#schemaversion)   | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-file-format-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/schemaVersion") |
| [catalogVersion](#catalogversion) | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-catalog-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/catalogVersion")    |
| [items](#items)                   | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-product.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/items")                     |
| [protocols](#protocols)           | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-protocols.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/protocols")               |
| [sources](#sources)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-sources.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/sources")                   |
| [citations](#citations)           | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-citations.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/citations")               |
| [categories](#categories)         | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-categories.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/categories")             |
| [methods](#methods)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-properties-delivery-methods.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/methods")          |

## $schema

Optional editor hint for JSON validation and completion. The app uses its bundled schema and does not download this URL.

`$schema`

* is optional

* Type: `string` ([Editor schema URL](library-properties-editor-schema-url.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-editor-schema-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/$schema")

### $schema Type

`string` ([Editor schema URL](library-properties-editor-schema-url.md))

## schemaVersion

Library file format version. Use the integer 1 during development.

`schemaVersion`

* is required

* Type: `integer` ([File format version](library-properties-file-format-version.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-file-format-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/schemaVersion")

### schemaVersion Type

`integer` ([File format version](library-properties-file-format-version.md))

### schemaVersion Constraints

**constant**: the value of this property must be equal to:

```json
1
```

## catalogVersion

Content version marker. Use the integer 1 during development; the app detects content updates by SHA-256 digest.

`catalogVersion`

* is required

* Type: `integer` ([Catalog version](library-properties-catalog-version.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-catalog-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/catalogVersion")

### catalogVersion Type

`integer` ([Catalog version](library-properties-catalog-version.md))

### catalogVersion Constraints

**constant**: the value of this property must be equal to:

```json
1
```

## items

Exactly one product identity. Include its reusable protocols in the protocols array; importing does not create a personal product or start a schedule.

`items`

* is required

* Type: `object[]` ([Product](library-defs-product.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-product.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/items")

### items Type

`object[]` ([Product](library-defs-product.md))

### items Constraints

**maximum number of items**: the maximum number of items for this array is: `1`

**minimum number of items**: the minimum number of items for this array is: `1`

## protocols

One or more reusable protocols for the included product. Each productID must equal items\[0].id. Users choose which protocols to import.

`protocols`

* is required

* Type: `object[]` ([Protocol](library-defs-protocol.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-protocols.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/protocols")

### protocols Type

`object[]` ([Protocol](library-defs-protocol.md))

### protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## sources

Source records referenced by citations. Use an empty array when there are none; citation sourceIDs must resolve within this file.

`sources`

* is required

* Type: `object[]` ([Source](library-defs-source.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-sources.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/sources")

### sources Type

`object[]` ([Source](library-defs-source.md))

## citations

Links from a product or protocol to a source, with optional location and evidence context. Use an empty array when there are none.

`citations`

* is required

* Type: `object[]` ([Citation](library-defs-citation.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-citations.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/citations")

### citations Type

`object[]` ([Citation](library-defs-citation.md))

## categories

Grouping labels referenced by the product's categoryID. Use an empty array when the product has no category.

`categories`

* is required

* Type: `object[]` ([Category](library-defs-category.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-categories.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/categories")

### categories Type

`object[]` ([Category](library-defs-category.md))

## methods

Labels for supported delivery IDs used by the protocols. Each protocol's methodID must resolve within this file.

`methods`

* is required

* Type: `object[]` ([Delivery method](library-defs-delivery-method.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-properties-delivery-methods.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/properties/methods")

### methods Type

`object[]` ([Delivery method](library-defs-delivery-method.md))

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

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :-------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                         | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/id")               |
| [name](#name)                     | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-nonblank-text-1.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/name")           |
| [aliases](#aliases)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-alternative-names.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/aliases")      |
| [kind](#kind)                     | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-product-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind")              |
| [identityStatus](#identitystatus) | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-identity-status.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/identityStatus") |
| [categoryID](#categoryid)         | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-product-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/categoryID")         |
| [benefits](#benefits)             | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-product-properties-benefits-and-context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/benefits")  |

### id

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`id`

* is required

* Type: `string` ([Nonblank text](library-defs-product-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/id")

#### id Type

`string` ([Nonblank text](library-defs-product-properties-nonblank-text.md))

#### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### name

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`name`

* is required

* Type: `string` ([Nonblank text](library-defs-product-properties-nonblank-text-1.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-nonblank-text-1.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/name")

#### name Type

`string` ([Nonblank text](library-defs-product-properties-nonblank-text-1.md))

#### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### aliases

Other names readers may use for this product. Use an empty array when there are none.

`aliases`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-alternative-names.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/aliases")

#### aliases Type

`string[]`

### kind

Classifies the identity as a product, blend, other item, or unresolved item. Use one of the exact listed values.

`kind`

* is required

* Type: `string` ([Product kind](library-defs-product-properties-product-kind.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-product-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind")

#### kind Type

`string` ([Product kind](library-defs-product-properties-product-kind.md))

#### kind Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"product"`    |             |
| `"blend"`      |             |
| `"other"`      |             |
| `"unresolved"` |             |

### identityStatus

Use resolved for a confirmed identity or needs_confirmation when the identity still needs clarification.

`identityStatus`

* is required

* Type: `string` ([Identity status](library-defs-product-properties-identity-status.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-identity-status.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/identityStatus")

#### identityStatus Type

`string` ([Identity status](library-defs-product-properties-identity-status.md))

#### identityStatus Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"resolved"`           |             |
| `"needs_confirmation"` |             |

### categoryID

Integer ID of a category in this file. Omit or set to null when the product has no category.

`categoryID`

* is optional

* Type: `integer` ([Category ID](library-defs-product-properties-category-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/categoryID")

#### categoryID Type

`integer` ([Category ID](library-defs-product-properties-category-id.md))

### benefits

Optional text describing intended benefits and their supporting context or limitations. Omit or set to null when unavailable.

`benefits`

* is optional

* Type: `string` ([Benefits and context](library-defs-product-properties-benefits-and-context.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-benefits-and-context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/benefits")

#### benefits Type

`string` ([Benefits and context](library-defs-product-properties-benefits-and-context.md))

## Definitions group protocol

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol"}
```

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-1)                     | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")             |
| [productID](#productid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-nonblank-text-1.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")    |
| [title](#title)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-nonblank-text-2.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")        |
| [purpose](#purpose)             | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")              |
| [methodID](#methodid)           | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")  |
| [population](#population)       | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-intended-audience.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population") |
| [evidenceNotes](#evidencenotes) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidence-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes") |
| [regimen](#regimen)             | `object` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")                                  |

### id

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`id`

* is required

* Type: `string` ([Nonblank text](library-defs-protocol-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/id")

#### id Type

`string` ([Nonblank text](library-defs-protocol-properties-nonblank-text.md))

#### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### productID

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`productID`

* is required

* Type: `string` ([Nonblank text](library-defs-protocol-properties-nonblank-text-1.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-nonblank-text-1.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/productID")

#### productID Type

`string` ([Nonblank text](library-defs-protocol-properties-nonblank-text-1.md))

#### productID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### title

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`title`

* is required

* Type: `string` ([Nonblank text](library-defs-protocol-properties-nonblank-text-2.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-nonblank-text-2.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/title")

#### title Type

`string` ([Nonblank text](library-defs-protocol-properties-nonblank-text-2.md))

#### title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### purpose

Optional explanation of the routine's intended goal. Omit or set to null when unavailable.

`purpose`

* is optional

* Type: `string` ([Purpose](library-defs-protocol-properties-purpose.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-purpose.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/purpose")

#### purpose Type

`string` ([Purpose](library-defs-protocol-properties-purpose.md))

### methodID

An exact, lowercase delivery choice supported by the app. Use unspecified when the user should choose the method; a custom display label does not allow a new ID.

`methodID`

* is required

* Type: `string` ([Delivery method ID](library-defs-protocol-properties-delivery-method-id.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/methodID")

#### methodID Type

`string` ([Delivery method ID](library-defs-protocol-properties-delivery-method-id.md))

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

Text describing who the source routine applies to. Use an empty string when no audience is specified.

`population`

* is required

* Type: `string` ([Intended audience](library-defs-protocol-properties-intended-audience.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-intended-audience.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/population")

#### population Type

`string` ([Intended audience](library-defs-protocol-properties-intended-audience.md))

### evidenceNotes

Optional qualifications, uncertainties, or source context for this routine. Omit or set to null when unavailable.

`evidenceNotes`

* is optional

* Type: `string` ([Evidence notes](library-defs-protocol-properties-evidence-notes.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-protocol-properties-evidence-notes.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/evidenceNotes")

#### evidenceNotes Type

`string` ([Evidence notes](library-defs-protocol-properties-evidence-notes.md))

### regimen

The reusable dose, duration, and schedule content of a protocol. Version and phases are required. Optional source metadata supplies context; the editor only copies settings it understands.

`regimen`

* is required

* Type: `object` ([Regimen](library-defs-regimen.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/protocol/properties/regimen")

#### regimen Type

`object` ([Regimen](library-defs-regimen.md))

## Definitions group source

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source"}
```

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :-------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-2)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")             |
| [url](#url)                 | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")               |
| [title](#title-1)           | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")           |
| [publisher](#publisher)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")          |
| [type](#type)               | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")             |
| [publishedAt](#publishedat) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-source-properties-publication-date.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt") |

### id

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`id`

* is required

* Type: `string` ([Nonblank text](library-defs-source-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/id")

#### id Type

`string` ([Nonblank text](library-defs-source-properties-nonblank-text.md))

#### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### url

HTTP or HTTPS source URL without embedded credentials. The app also checks the parsed URL; it does not fetch the source during import.

`url`

* is required

* Type: `string` ([Source URL](library-defs-source-properties-source-url.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-url.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/url")

#### url Type

`string` ([Source URL](library-defs-source-properties-source-url.md))

#### url Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https?://[^\s/@]+(?:[/:?#][^\s]*)?$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3F%3A%2F%2F%5B%5E%5Cs%2F%40%5D%2B\(%3F%3A%5B%2F%3A%3F%23%5D%5B%5E%5Cs%5D*\)%3F%24 "try regular expression with regexr.com")

### title

Display title of the source material.

`title`

* is required

* Type: `string` ([Source title](library-defs-source-properties-source-title.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-title.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/title")

#### title Type

`string` ([Source title](library-defs-source-properties-source-title.md))

### publisher

Optional authoring organization or publisher name. Omit or set to null when unavailable.

`publisher`

* is optional

* Type: `string` ([Publisher](library-defs-source-properties-publisher.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publisher.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publisher")

#### publisher Type

`string` ([Publisher](library-defs-source-properties-publisher.md))

### type

Free-form source category. The listed examples are suggestions, not a fixed set of choices.

`type`

* is required

* Type: `string` ([Source type](library-defs-source-properties-source-type.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-source-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/type")

#### type Type

`string` ([Source type](library-defs-source-properties-source-type.md))

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

Optional publication date retained as text, without date parsing or a required date format. Omit or set to null when unavailable.

`publishedAt`

* is optional

* Type: `string` ([Publication date](library-defs-source-properties-publication-date.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-source-properties-publication-date.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/source/properties/publishedAt")

#### publishedAt Type

`string` ([Publication date](library-defs-source-properties-publication-date.md))

## Definitions group citation

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocolID](#protocolid)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocol-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID") |
| [productID](#productid-1)     | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-product-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")   |
| [sourceID](#sourceid)         | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")        |
| [locator](#locator)           | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-source-location.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")       |
| [evidenceNote](#evidencenote) | `string` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidence-note.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote")    |
| [supports](#supports)         | `array`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supported-fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")     |

### protocolID

ID of a protocol in this file. Provide a nonblank value when citing a protocol; otherwise omit this field or set it to null.

`protocolID`

* is optional

* Type: `string` ([Protocol target ID](library-defs-citation-properties-protocol-target-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-protocol-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/protocolID")

#### protocolID Type

`string` ([Protocol target ID](library-defs-citation-properties-protocol-target-id.md))

### productID

ID of the product in this file. Provide a nonblank value when citing the product; otherwise omit this field or set it to null.

`productID`

* is optional

* Type: `string` ([Product target ID](library-defs-citation-properties-product-target-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-product-target-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/productID")

#### productID Type

`string` ([Product target ID](library-defs-citation-properties-product-target-id.md))

### sourceID

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`sourceID`

* is required

* Type: `string` ([Nonblank text](library-defs-citation-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/sourceID")

#### sourceID Type

`string` ([Nonblank text](library-defs-citation-properties-nonblank-text.md))

#### sourceID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

### locator

Optional page, section, table, or other locator within the source. Omit or set to null when unavailable.

`locator`

* is optional

* Type: `string` ([Source location](library-defs-citation-properties-source-location.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-source-location.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/locator")

#### locator Type

`string` ([Source location](library-defs-citation-properties-source-location.md))

### evidenceNote

Optional explanation of what the source supports and any relevant limits. Omit or set to null when unavailable.

`evidenceNote`

* is optional

* Type: `string` ([Evidence note](library-defs-citation-properties-evidence-note.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-evidence-note.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/evidenceNote")

#### evidenceNote Type

`string` ([Evidence note](library-defs-citation-properties-evidence-note.md))

### supports

Field names or reference paths supported by this citation, such as /phases or /benefits. The app retains these strings as descriptions and does not resolve them as JSON Pointers.

`supports`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-properties-supported-fields.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/properties/supports")

#### supports Type

`string[]`

## Definitions group category

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category"}
```

| Property        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                       |
| :-------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-3)     | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-category-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/id")     |
| [name](#name-1) | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-category-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/name") |

### id

Integer identifier unique within the categories array. Reuse an installed ID only for the same category.

`id`

* is required

* Type: `integer` ([Category ID](library-defs-category-properties-category-id.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-category-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/id")

#### id Type

`integer` ([Category ID](library-defs-category-properties-category-id.md))

### name

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`name`

* is required

* Type: `string` ([Nonblank text](library-defs-category-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-category-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/name")

#### name Type

`string` ([Nonblank text](library-defs-category-properties-nonblank-text.md))

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

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :-------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id-4)     | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-delivery-method-properties-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/id") |
| [name](#name-2) | `string` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-delivery-method-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/name")    |

### id

An exact, lowercase delivery choice supported by the app. Use unspecified when the user should choose the method; a custom display label does not allow a new ID.

`id`

* is required

* Type: `string` ([Delivery method ID](library-defs-delivery-method-properties-delivery-method-id.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-delivery-method-properties-delivery-method-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/id")

#### id Type

`string` ([Delivery method ID](library-defs-delivery-method-properties-delivery-method-id.md))

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

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`name`

* is required

* Type: `string` ([Nonblank text](library-defs-delivery-method-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-delivery-method-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/method/properties/name")

#### name Type

`string` ([Nonblank text](library-defs-delivery-method-properties-nonblank-text.md))

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
| [preparation_options](#preparation_options)                     | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options")                     |
| [reference_urls](#reference_urls)                               | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-reference_urls.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/reference_urls")                               |
| [regimen_type](#regimen_type)                                   | `string`  | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type")                                   |
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
| [version](#version)                                             | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/version")                                     |
| [weight_examples](#weight_examples)                             | `array`   | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-weight_examples.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/weight_examples")                             |
| Additional Properties                                           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                         |

### cautions

Optional source context for exclusions, interactions, monitoring, and reported effects. This reference metadata does not create alerts or monitoring tasks.

`cautions`

* is optional

* Type: `object` ([Cautions](library-defs-regimen-properties-cautions.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-cautions.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/cautions")

#### cautions Type

`object` ([Cautions](library-defs-regimen-properties-cautions.md))

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

Required, nonempty list of routine stages in source order. Each stage needs a name, duration, dose, and schedule.

`phases`

* is required

* Type: `object[]` ([Phase](library-defs-regimen-properties-phases-phase.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases")

#### phases Type

`object[]` ([Phase](library-defs-regimen-properties-phases-phase.md))

#### phases Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

### preparation_options

Optional alternatives for product form, amounts, diluent, and concentration. Keep quantities and units explicit; the app retains this reference metadata without preparing a personal product.

`preparation_options`

* is optional

* Type: `object[]` ([Preparation option](library-defs-regimen-properties-preparation-options-preparation-option.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-preparation-options.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/preparation_options")

#### preparation_options Type

`object[]` ([Preparation option](library-defs-regimen-properties-preparation-options-preparation-option.md))

### reference_urls



`reference_urls`

* is optional

* Type: `object[]` ([Details](library-defs-regimen-properties-reference_urls-items.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-reference_urls.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/reference_urls")

#### reference_urls Type

`object[]` ([Details](library-defs-regimen-properties-reference_urls-items.md))

### regimen_type

Use single_compound for one product, premixed_blend for a prepared blend, or stack for separate components. Stacks are viewable reference content and cannot be activated as a single personal protocol.

`regimen_type`

* is optional

* Type: `string` ([Regimen type](library-defs-regimen-properties-regimen-type.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-type.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/regimen_type")

#### regimen_type Type

`string` ([Regimen type](library-defs-regimen-properties-regimen-type.md))

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

Optional source-reported storage, handling, and discard guidance. This reference metadata does not set personal expiry dates or reminders.

`storage`

* is optional

* Type: `object` ([Storage](library-defs-regimen-properties-storage.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-storage.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/storage")

#### storage Type

`object` ([Storage](library-defs-regimen-properties-storage.md))

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

Regimen format version. Use the integer 1 during development, including for content updates.

`version`

* is required

* Type: `integer` ([Regimen version](library-defs-regimen-properties-regimen-version.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-regimen-version.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/version")

#### version Type

`integer` ([Regimen version](library-defs-regimen-properties-regimen-version.md))

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

## Definitions group decimal_amount

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/decimal_amount"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
