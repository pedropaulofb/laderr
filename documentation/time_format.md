# DateTime Format for `createdOn` and `modifiedOn` Fields

The `createdOn` and `modifiedOn` fields in a LaDeRR specification must comply with the `xsd:dateTime` format. These fields represent timestamps and must follow the [**ISO 8601** standard](https://en.wikipedia.org/wiki/ISO_8601) to ensure correct parsing and interpretation.

## **Allowed Formats**
TOML natively supports `datetime` values, so the recommended way to input these fields is **without quotation marks**:

```toml
createdOn = 2025-03-14T15:30:00Z
modifiedOn = 2025-03-14T15:30:00+01:00
```

Alternatively, if the values are provided as strings, they will be correctly processed if they still conform to `xsd:dateTime`:

```toml
createdOn = "2025-03-14T15:30:00Z"
modifiedOn = "2025-03-14T15:30:00+01:00"
```

### **Detailed Format Requirements**
- **Full Date and Time with UTC**:
  - ✅ `2025-03-14T15:30:00Z`
  - ✅ `2025-03-14T15:30:00.123Z` (with milliseconds)

- **Full Date and Time with Timezone Offset**:
  - ✅ `2025-03-14T15:30:00+01:00`
  - ✅ `2025-03-14T15:30:00.123-05:00`

- **Full Date and Time Without Timezone** (May cause ambiguity):
  - ⚠️ `2025-03-14T15:30:00` (Interpreted as local time)

## **Invalid Formats**
The following formats are **not accepted** because they do not conform to `xsd:dateTime`:

```toml
createdOn = 14-03-2025  # ❌ Incorrect order
createdOn = "March 14, 2025"  # ❌ Not ISO 8601
createdOn = 2025/03/14 15:30  # ❌ Uses '/' and missing 'T'
createdOn = 2025-03-14T15:30  # ❌ Missing seconds
createdOn = "14-03-2025T15:30:00Z"  # ❌ Wrong order
```

## **Best Practices**
- Use ISO 8601 format.
- Avoid ambiguous local times (`YYYY-MM-DDTHH:MM:SS`).
- Prefer native TOML datetime (without quotes) for automatic parsing.
- If using quotes, ensure the format remains correct for RDF processing.

By following these guidelines, your LaDeRR specification will be correctly parsed and compatible with `xsd:dateTime` standards.