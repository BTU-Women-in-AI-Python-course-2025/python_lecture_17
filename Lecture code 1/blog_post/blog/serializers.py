from rest_framework import serializers
from rest_framework.serializers import Serializer

from blog.choices import BLOG_POST_CATEGORY_CHOICES


class BlogPostSerializer(Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    active = serializers.BooleanField()
    category = serializers.ChoiceField(BLOG_POST_CATEGORY_CHOICES)
