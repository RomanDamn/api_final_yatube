from rest_framework import serializers

from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False,
                                          read_only=True,
                                          slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False,
                                          read_only=True,
                                          slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def validate(self, data):
        following = data['following']
        user = data['user']
        follow = Follow.objects.filter(user=user, following=following)
        if follow.exists():
            raise serializers.ValidationError('Not Allowed')
        return data
