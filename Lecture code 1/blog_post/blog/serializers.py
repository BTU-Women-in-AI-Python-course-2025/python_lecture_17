from rest_framework import serializers
from rest_framework.serializers import Serializer

from blog.choices import BLOG_POST_CATEGORY_CHOICES
from blog.models import BlogPost, BannerImage


class BlogPostListSerializer(Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    active = serializers.BooleanField()
    category = serializers.ChoiceField(BLOG_POST_CATEGORY_CHOICES)


class BlogPostCreateSerializer(BlogPostListSerializer):
    image = serializers.ImageField()

    def save(self):
        image = self.data.pop('image')
        blog_post = BlogPost.objects.create(**self.data)
        BannerImage.objects.create(blog_post=blog_post, image=image)
        return blog_post


# class BlogPostCreateSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(write_only=True)
#
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'text', 'active', 'category', 'image']
#
#     def create(self, validated_data):
#         image = validated_data.pop('image', None)
#         blog_post = BlogPost.objects.create(**validated_data)
#         BannerImage.objects.create(blog_post=blog_post, image=image)
#         return blog_post
