# ⚙️ Setting Up Django REST Framework (DRF)

Before building APIs, we need to configure Django REST Framework properly in your Django project.

---

## ✅ 1. Install DRF

Install Django REST Framework via pip:

```bash
pip install djangorestframework
```

---

## 🏗 2. Add `'rest_framework'` to `INSTALLED_APPS`

Open your `settings.py` and add:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## ⚙️ 3. Optional: DRF Configuration Settings

You can customize how DRF works by adding the `REST_FRAMEWORK` setting in `settings.py`.

Here's a simple example:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # API responses in JSON
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',  # Accept JSON input
    ],
}
```

You can later update this to include:

* Pagination
* Authentication methods
* Permission classes
* Throttling

But for now, keep it simple.

---

## 🧪 4. Run Migrations (if needed)

Some DRF extensions use Django models (e.g., token authentication), so be sure to run migrations:

```bash
python manage.py migrate
```

---

## 📁 5. Recommended Project Structure

```
myproject/
├── manage.py
├── myproject/
│   └── settings.py
├── books/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
```

---

## 🧪 6. Test with a Simple API

Try creating a simple view using `@api_view` to confirm DRF is working (as we did in the last example).

Visit the endpoint in the browser — DRF will automatically generate a browsable API UI if you didn’t disable the HTML renderer.

---

## 🧠 Summary

| Step | Description                                    |
| ---- | ---------------------------------------------- |
| 1    | Install `djangorestframework`                  |
| 2    | Add `'rest_framework'` to `INSTALLED_APPS`     |
| 3    | (Optional) Configure `REST_FRAMEWORK` settings |
| 4    | Run `migrate`                                  |
| 5    | Create serializers, views, and routes          |
