# Django Rest Framework

- **Introduction to Django REST Framework** - https://www.django-rest-framework.org/:
  - Overview of the framework and its capabilities.
- **Setting Up Django REST Framework** - https://www.django-rest-framework.org/#installation
- **serializers (basic)** - https://www.django-rest-framework.org/api-guide/serializers/#serializers
- **Building APIs:**
  - Function-Based Views - https://www.django-rest-framework.org/api-guide/views/#function-based-views
  - Class-based Views - https://www.django-rest-framework.org/api-guide/views/#class-based-views

### 📚 **Student Task: Create a Simple API with Django REST Framework**

1. **Install and set up Django REST Framework**  
   - Add `'rest_framework'` to `INSTALLED_APPS` in `settings.py`.

2. **Create a simple model** (e.g., `Book` with `title`, `author`, `published_date`).

3. **Create a `ModelSerializer`** for the model.  
   - Use `serializers.ModelSerializer`.

4. **Create two views**:
   - A **function-based view** to list all books.
   - A **class-based view** to retrieve a single book by ID.

5. **Register both views in `urls.py`**
