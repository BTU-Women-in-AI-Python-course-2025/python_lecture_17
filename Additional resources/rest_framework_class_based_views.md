# 📘 Django REST Framework: Class-Based Views (CBVs)

---

## 🧩 What Are Class-Based Views in DRF?

DRF provides a set of **class-based views (CBVs)** that give you more structure and reusability compared to function-based views.

Instead of writing logic with decorators like `@api_view`, you subclass classes like `APIView` or `GenericAPIView`.

---

## ✅ 1. Using `APIView` (Base Class)

This is the DRF equivalent of Django’s `View` class — you implement HTTP methods as class methods.

---

### 🔸 Example: GET and POST using `APIView`

#### 📁 `views.py`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # Normally, you'd save to the DB here
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

### 🔗 Add to `urls.py`

```python
from django.urls import path
from .views import BookListCreateView

urlpatterns = [
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
]
```

---

## 🧠 Benefits of Using `APIView`

| Feature         | Benefit                                    |
| --------------- | ------------------------------------------ |
| Class structure | Clean, organized logic per method          |
| Reusability     | Easier to extend and reuse logic           |
| Full control    | You define everything (great for learning) |

---

## 🚀 What’s Next?

After `APIView`, DRF provides **shortcuts** that save time:

| Class                          | Purpose                                 |
| ------------------------------ | --------------------------------------- |
| `GenericAPIView` + mixins      | Add reusable behaviors                  |
| `ListCreateAPIView`            | Prebuilt GET (list) and POST (create)   |
| `RetrieveUpdateDestroyAPIView` | Prebuilt detail view (GET, PUT, DELETE) |

We'll cover these next.

---

## 📚 Summary

| Concept               | Description                               |
| --------------------- | ----------------------------------------- |
| `APIView`             | Base class for defining GET, POST, etc.   |
| `get(self, request)`  | Handles GET requests                      |
| `post(self, request)` | Handles POST requests                     |
| `.as_view()`          | Turns class into a view function for URLs |

