# Product citation Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1
```

Requires a nonblank productID. Omit protocolID or set it to null so the citation has only one target.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## 1 Type

unknown ([Product citation](library-defs-citation-oneof-product-citation.md))

# 1 Properties

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                     |
| :------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [productID](#productid)   | `string`      | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-product-citation-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/productID")           |
| [protocolID](#protocolid) | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-product-citation-properties-unused-protocol-target.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/protocolID") |

## productID

A string containing at least one non-whitespace character. Use stable IDs and meaningful names where a field refers to this definition.

`productID`

* is required

* Type: `string` ([Nonblank text](library-defs-citation-oneof-product-citation-properties-nonblank-text.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-product-citation-properties-nonblank-text.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/productID")

### productID Type

`string` ([Nonblank text](library-defs-citation-oneof-product-citation-properties-nonblank-text.md))

### productID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## protocolID

For a product citation, omit protocolID or set it to null. A citation cannot target both a product and a protocol.

`protocolID`

* is optional

* Type: `null`, the value must be null ([Unused protocol target](library-defs-citation-oneof-product-citation-properties-unused-protocol-target.md))

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-product-citation-properties-unused-protocol-target.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/protocolID")

### protocolID Type

`null`, the value must be null ([Unused protocol target](library-defs-citation-oneof-product-citation-properties-unused-protocol-target.md))
