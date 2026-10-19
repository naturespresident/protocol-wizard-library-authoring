# Untitled object in Protocol Wizard product library — schema version 1 Schema

```txt
https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [library.schema.json\*](../../template/library.schema.json "open original schema") |

## items Type

`object` ([Details](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items.md))

# items Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                     |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [condition](#condition) | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items-properties-condition.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions/items/properties/condition")  |
| [value](#value)         | `string` | Optional | cannot be null | [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions/items/properties/value") |
| Additional Properties   | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                |

## condition



`condition`

* is optional

* Type: `string`

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items-properties-condition.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions/items/properties/condition")

### condition Type

`string`

## value

A plain period-separated decimal string, such as 0.25 or 500. Signs, exponents, grouping separators, and whitespace are invalid.

`value`

* is optional

* Type: `string` ([Decimal amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items-properties-decimal-amount.md))

* cannot be null

* defined in: [Protocol Wizard product library — schema version 1](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items-properties-decimal-amount.md "https://raw.githubusercontent.com/naturespresident/protocol-wizard-library-authoring/main/template/library.schema.json#/$defs/regimen/properties/phases/items/properties/dose/properties/conditions/items/properties/value")

### value Type

`string` ([Decimal amount](library-defs-regimen-properties-phases-phase-properties-phase-dose-properties-conditions-items-properties-decimal-amount.md))

### value Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]+(\.[0-9]+)?(?![\s\S])
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%2B\(%5C.%5B0-9%5D%2B\)%3F\(%3F!%5B%5Cs%5CS%5D\) "try regular expression with regexr.com")

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
