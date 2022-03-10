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
    user = serializers.SlugRelatedField(slug_field="user_name", queryset=Users.objects.all())
    project = serializers.SlugRelatedField(slug_field="title", queryset=Projects.objects.all())

    class Meta:
        model = Contributors
        fields = [
                  'id',
                  'user',
                  'project',
                  'role',
                  'permission',
                 ]


class IssuesListSerializer(serializers.ModelSerializer):
    author_user = serializers.SlugRelatedField(slug_field="user_name", queryset=Users.objects.all())
    assignee_user = serializers.SlugRelatedField(slug_field="user_name", queryset=Users.objects.all())
    project = serializers.SlugRelatedField(slug_field="title", queryset=Projects.objects.all())

    class Meta:
        model = Issues
        fields = [
                  'id',
                  'title',
                  'description',
                  'tag',
                  'project',
                  'status',
                  'author_user',
                  'assignee_user',
                 ]


class ReadCommentsListSerializer(serializers.ModelSerializer):
    author_user = serializers.SlugRelatedField(slug_field="user_name", queryset=Users.objects.all())
    issue = serializers.SlugRelatedField(slug_field="title", queryset=Issues.objects.all())
    projects = ProjectsListSerializer(source='issue.project')

    class Meta:
        model = Comments
        fields = [
                  'id',
                  'description',
                  'author_user',
                  'issue',
                  'projects',
                 ]


class WriteCommentsListSerializer(serializers.ModelSerializer):
    author_user = serializers.SlugRelatedField(slug_field="user_name", queryset=Users.objects.all())
    issue = serializers.SlugRelatedField(slug_field="title", queryset=Issues.objects.all())

    class Meta:
        model = Comments
        fields = [
                  'id',
                  'description',
                  'author_user',
                  'issue',
                 ]
