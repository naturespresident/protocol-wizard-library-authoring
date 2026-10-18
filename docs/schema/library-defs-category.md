# Category Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category
```

A product grouping label with an integer ID. Reuse an installed ID only for the same category; changes to shared labels require replacement confirmation.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## category Type

`object` ([Category](library-defs-category.md))

# category Properties

| Property      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                   |
| :------------ | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)     | `integer` | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-category-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/id") |
| [name](#name) | `string`  | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/name")                 |

## id

Integer identifier unique within the categories array. Reuse an installed ID only for the same category.

`id`

* is required

* Type: `integer` ([Category ID](library-defs-category-properties-category-id.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-category-properties-category-id.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/id")

### id Type

`integer` ([Category ID](library-defs-category-properties-category-id.md))

## name

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`name`

* is required

* Type: `string` ([Nonblank text](library-defs-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/category/properties/name")

### name Type

`string` ([Nonblank text](library-defs-nonblank-text.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")
