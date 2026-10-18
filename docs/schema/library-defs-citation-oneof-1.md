# Untitled undefined type in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## 1 Type

unknown

# 1 Properties

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :------------------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [productID](#productid)   | `string`      | Required | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-1-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/productID")   |
| [protocolID](#protocolid) | Not specified | Optional | can be null    | [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-1-properties-protocolid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/protocolID") |

## productID



`productID`

* is required

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-1-properties-productid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/productID")

### productID Type

`string`

### productID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\S
```

[try pattern](https://regexr.com/?expression=%5CS "try regular expression with regexr.com")

## protocolID



`protocolID`

* is optional

* Type: `null`, the value must be null

* can be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-citation-oneof-1-properties-protocolid.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/citation/oneOf/1/properties/protocolID")

### protocolID Type

`null`, the value must be null
