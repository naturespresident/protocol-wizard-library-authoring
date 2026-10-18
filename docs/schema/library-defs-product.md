# Product Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item
```

The single product described by this library file. Keep its ID stable so future imports can update the same reference entry.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## item Type

`object` ([Product](library-defs-product.md))

# item Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :-------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                         | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/id")                                  |
| [name](#name)                     | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/name")                                |
| [aliases](#aliases)               | `array`   | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-alternative-names.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/aliases")      |
| [kind](#kind)                     | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-product-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind")              |
| [identityStatus](#identitystatus) | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-product-properties-identity-status.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/identityStatus") |
| [categoryID](#categoryid)         | `integer` | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-product-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/categoryID")         |
| [benefits](#benefits)             | `string`  | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-product-properties-benefits-and-context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/benefits")  |

## id

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`id`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/id")

### id Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## name

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`name`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/name")

### name Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## aliases

Other names readers may use for this product. Use an empty array when there are none.

`aliases`

* is required

* Type: `string[]`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-alternative-names.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/aliases")

### aliases Type

`string[]`

## kind

Classifies the identity as a product, blend, other item, or unresolved item. Use one of the exact listed values.

`kind`

* is required

* Type: `string` ([Product kind](library-defs-product-properties-product-kind.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-product-kind.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/kind")

### kind Type

`string` ([Product kind](library-defs-product-properties-product-kind.md))

### kind Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"product"`    |             |
| `"blend"`      |             |
| `"other"`      |             |
| `"unresolved"` |             |

## identityStatus

Use resolved for a confirmed identity or needs_confirmation when the identity still needs clarification.

`identityStatus`

* is required

* Type: `string` ([Identity status](library-defs-product-properties-identity-status.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-identity-status.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/identityStatus")

### identityStatus Type

`string` ([Identity status](library-defs-product-properties-identity-status.md))

### identityStatus Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"resolved"`           |             |
| `"needs_confirmation"` |             |

## categoryID

Integer ID of a category in this file. Omit or set to null when the product has no category.

`categoryID`

* is optional

* Type: `integer` ([Category ID](library-defs-product-properties-category-id.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/categoryID")

### categoryID Type

`integer` ([Category ID](library-defs-product-properties-category-id.md))

## benefits

Optional text describing intended benefits and their supporting context or limitations. Omit or set to null when unavailable.

`benefits`

* is optional

* Type: `string` ([Benefits and context](library-defs-product-properties-benefits-and-context.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-product-properties-benefits-and-context.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/item/properties/benefits")

### benefits Type

`string` ([Benefits and context](library-defs-product-properties-benefits-and-context.md))
