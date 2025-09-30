from rest_framework import serializers

from blog.choices import CATEGORY_CHOICES
from blog.models import BlogPost


class BlogPostListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=200)
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)


class BlogPostDetailUpdateCreateSerializer(BlogPostListSerializer):
    text = serializers.CharField()
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        blog_post = BlogPost.objects.create(**self.validated_data)
        return blog_post
