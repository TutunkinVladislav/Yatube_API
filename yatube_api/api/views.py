from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)

from posts.models import Group, Post, User
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        follow = get_object_or_404(User, username=self.request.user.username)
        return follow.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
