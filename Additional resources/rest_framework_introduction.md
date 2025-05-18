# 📘 Introduction to Django REST Framework (DRF)

---

## 🧩 What is DRF?

Django REST Framework (DRF) is a **powerful and flexible toolkit** for building **Web APIs** on top of Django.

> ✅ DRF builds on Django’s standard views and models to expose data over HTTP using JSON.

---

## 🎯 Why Use DRF?

* 🔄 Automatically converts data to and from JSON
* 🔐 Built-in support for authentication and permissions
* 🔍 Powerful view classes and routers
* 📄 Built-in browsable API for testing

---

## 🏗 Basic Example: Build Your First API

Let’s create a simple `Book` model and expose it as a REST API.

### 1. Install DRF

```bash
pip install djangorestframework
```

Add it to `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

### 2. Create the Model

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField()
```

---

### 3. Create the Serializer

```python
# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

---

### 4. Create the API View (Function-Based View)

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
```

---

### 5. Configure the URL

```python
# urls.py
from django.urls import path
from .views import book_list

urlpatterns = [
    path('api/books/', book_list, name='book-list'),
]
```

Now visiting `http://localhost:8000/api/books/` will return a list of books in **JSON format**.

---

## 🧠 Key Concepts Preview

| Concept               | Description                          |
| --------------------- | ------------------------------------ |
| Serializer            | Converts model instances to JSON     |
| APIView / `@api_view` | Class/func for handling API requests |
| Response              | Like `HttpResponse`, but for APIs    |

