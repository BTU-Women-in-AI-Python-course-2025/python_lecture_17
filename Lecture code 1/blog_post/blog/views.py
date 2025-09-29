from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostCreateSerializer, BlogPostListSerializer


@api_view(['POST'])
def create_blog_post(request):
    serializer = BlogPostCreateSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        blogs = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostListSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostCreateSerializer(data=request.data)
        if serializer.is_valid():
            #BlogPost.objects.create(**serializer.validated_data)
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostListCreateView(APIView):
    def get(self, request):
        books = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostListSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostCreateSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostCreateSerializer
