from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


@api_view(['POST'])
def create_blog_post(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        # For now, we’ll just return the validated data
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        books = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostListCreateView(APIView):
    def get(self, request):
        books = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)