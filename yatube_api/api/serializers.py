from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
import datetime as dt
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault())
    pub_date = serializers.DateTimeField(
        default=dt.datetime.now())

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post
        read_only_fields = ('author', 'pub_date')

        validators = [
            UniqueTogetherValidator(
                queryset=Post.objects.all(),
                fields=('text', 'author')
            )
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault())
    created = serializers.DateTimeField(default=dt.datetime.now())

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post', 'created')
