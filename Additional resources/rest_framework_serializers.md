# 📦 Django REST Framework: Basic Serializer

---

## 🔹 What is a Serializer?

A **serializer** in Django REST Framework is used to:

* Convert complex data types like Django models into **JSON** (for APIs).
* Convert **JSON back into Python objects** (for validation & saving).

> 🧠 Think of it as the DRF version of a Django Form.

---

## ✅ When to Use a Basic Serializer

Use `serializers.Serializer` when:

* You **don’t** want to tie directly to a Django model.
* You want **more control** over the fields and validation.
* You're just getting started with DRF.

---

## 🧱 Example: Basic `BookSerializer`

### 📁 `serializers.py`

```python
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published = serializers.DateField()
```

---

## 📥 Using the Serializer in a View

### 📁 `views.py`

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        # For now, we’ll just return the validated data
        return Response(serializer.validated_data)
    return Response(serializer.errors, status=400)
```

---

## 🧪 Test It

Send a POST request to `/api/create-book/` with this JSON:

```json
{
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "published": "2023-09-01"
}
```

You should get back the same data in the response.

---

## 🧠 What Happens Under the Hood?

| Step                                | Purpose                   |
| ----------------------------------- | ------------------------- |
| `BookSerializer(data=request.data)` | Load data for validation  |
| `is_valid()`                        | Validate the input        |
| `validated_data`                    | Safe, clean data          |
| `serializer.errors`                 | Returns validation errors |

---

## ➕ Example: `BookCreateSerializer` (ModelSerializer)

If you actually want to **save books to the database**, use a `ModelSerializer`.

### 📁 `serializers.py`

```python
from rest_framework import serializers
from .models import Book

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published']
```

---

### 📁 `views.py`

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookCreateSerializer

@api_view(['POST'])
def create_book_db(request):
    serializer = BookCreateSerializer(data=request.data)
    if serializer.is_valid():
        book = serializer.save()  # Save to DB
        return Response(BookCreateSerializer(book).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

## 🧪 Test It

Send a POST request to `/api/create-book-db/` with:

```json
{
    "title": "Two Scoops of Django",
    "author": "Daniel Roy Greenfeld",
    "published": "2024-01-15"
}
```

✅ This will **save the book in the database** and return the stored object with its `id`.

---

## 🧰 Summary

| Feature           | Description             |
| ----------------- | ----------------------- |
| `Serializer`      | Manually defined fields |
| `.is_valid()`     | Validates the input     |
| `.validated_data` | Cleaned data            |
| `.errors`         | Validation errors       |
