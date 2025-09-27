# 📘 Django REST Framework: Serializer Field Options

This repository documents **Serializer Field options** available in **Django REST Framework (DRF)**.

---

## 🔹 Serializer Fields

DRF provides different field types to handle validation, transformation, and representation of data.

### ✅ Core Field Types

* **`BooleanField`** – `True` / `False` values
* **`CharField`** – String input
* **`EmailField`** – Validated email format
* **`SlugField`** – Short “slug” strings
* **`URLField`** – Fully qualified URLs
* **`UUIDField`** – UUID values

---

### 🔢 Numeric Fields

* **`IntegerField`** – Whole numbers
* **`FloatField`** – Floating point numbers
* **`DecimalField`** – Arbitrary precision decimals

---

### 📅 Date & Time Fields

* **`DateField`** – Date only (`YYYY-MM-DD`)
* **`TimeField`** – Time only (`HH:MM[:ss[.uuuuuu]]`)
* **`DateTimeField`** – Full date & time

---

### 🗂 File & Image Fields

* **`FileField`** – File uploads
* **`ImageField`** – Image uploads (validates file type)

---

### 🔗 Relational Fields

* **`PrimaryKeyRelatedField`** – Uses the primary key of related model
* **`StringRelatedField`** – Uses the model’s `__str__` representation
* **`SlugRelatedField`** – Uses a slug field for relation
* **`ManyRelatedField`** – Handles lists of relations

---

### 📦 Other Special Fields

* **`SerializerMethodField`** – Read-only field defined by a custom method
* **`ReadOnlyField`** – Non-editable field
* **`HiddenField`** – Value not shown but still used internally (e.g., current user)
* **`JSONField`** – Stores arbitrary JSON objects
* **`DictField`** – Dictionary mapping
* **`ListField`** – Generic list of items

---

## ⚙️ Common Field Options

All fields accept some common arguments:

* `required=True|False` – Whether the field is mandatory
* `read_only=True|False` – If field is read-only
* `write_only=True|False` – If field is write-only
* `default=value` – Default value if not provided
* `allow_null=True|False` – Accept `null` as a value
* `allow_blank=True|False` – Accept empty string (`CharField`)
* `validators=[...]` – Custom validators list
* `max_length`, `min_length` – String length constraints
* `max_value`, `min_value` – Numeric constraints
* `help_text="..."` – Helper text for API docs
* `label="..."` – Human-readable name
* `style={...}` – UI hinting for browsable API
