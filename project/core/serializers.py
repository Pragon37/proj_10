from rest_framework import serializers

from core.models import Projects, Contributors, Issues, Comments
from users.models import Users

class ProjectsListSerializer(serializers.ModelSerializer):
    author_user = serializers.SlugRelatedField(slug_field="user_name", queryset=Users.objects.all())

    class Meta:
        model = Projects
        fields = [
        'id',
        'title',
        'description',
        'type',
        'author_user',
        ]

class ContributorsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = [
        'id',
        'user',
        'project',
        ]

class IssuesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = [
        'id',
        'title',
        'tag',
        'project',
        'status',
        'author_user',
        'assignee_user',
        ]

class CommentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = [
        'id',
        'description',
        'author_user',
        'issue',
        ]