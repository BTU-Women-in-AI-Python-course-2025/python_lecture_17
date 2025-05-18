# 🧾 Django REST Framework: Function-Based Views (FBVs)

---

## 🧠 What Are DRF Function-Based Views?

DRF allows you to use simple Python functions to handle HTTP methods — just like in standard Django — but with added power using the `@api_view` decorator.

---

## ✅ 1. Import the Tools

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
```

---

## 📘 Example: List & Create View (GET and POST)

### 📁 `views.py`

```python
@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # Normally you'd call serializer.save() if using ModelSerializer
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

## 🔗 Add to `urls.py`

```python
from django.urls import path
from .views import book_list_create

urlpatterns = [
    path('api/books/', book_list_create, name='book-list-create'),
]
```

---

## 📌 Notes

* `@api_view(['GET', 'POST'])` tells DRF to handle these HTTP methods.
* You can also use `'PUT'`, `'DELETE'`, `'PATCH'`, etc.
* DRF automatically parses JSON and handles content negotiation.

---

## 📚 Summary

| Concept            | Description                        |
| ------------------ | ---------------------------------- |
| `@api_view([...])` | Declare allowed methods            |
| `request.data`     | Access POST/PUT/PATCH body         |
| `Response()`       | Returns an HTTP response with JSON |
| `status`           | Use status codes for clarity       |
