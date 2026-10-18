# Protocol citation Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/0
```

Requires a nonblank protocolID. Omit productID or set it to null so the citation has only one target.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## 0 Type

unknown ([Protocol citation](library-defs-citation-oneof-protocol-citation.md))

# 0 Properties

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                    |
| :------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [protocolID](#protocolid) | `string`      | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-protocol-citation-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/0/properties/protocolID")        |
| [productID](#productid)   | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-protocol-citation-properties-unused-product-target.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/0/properties/productID") |

## protocolID

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`protocolID`

* is required

* Type: `string` ([Nonblank text](library-defs-citation-oneof-protocol-citation-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-protocol-citation-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/0/properties/protocolID")

### protocolID Type

`string` ([Nonblank text](library-defs-citation-oneof-protocol-citation-properties-nonblank-text.md))

### protocolID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## productID

For a protocol citation, omit productID or set it to null. A citation cannot target both a product and a protocol.

`productID`

* is optional

* Type: `null`, the value must be null ([Unused product target](library-defs-citation-oneof-protocol-citation-properties-unused-product-target.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-protocol-citation-properties-unused-product-target.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/0/properties/productID")

### productID Type

`null`, the value must be null ([Unused product target](library-defs-citation-oneof-protocol-citation-properties-unused-product-target.md))
