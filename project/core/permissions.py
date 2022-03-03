from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser

from core.models import Projects, Contributors, Issues, Comments


class AllowContributorsOnly(BasePermission):

    message = 'Project access is restricted to contributors only.'

    def has_permission(self, request, view):
        if Contributors.objects.filter(user=request.user).exists():
            return True

class AllowAuthorEditOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        if f'{request.user}' == 'AnonymousUser':
            return False

        project = obj.issue.project_id
        project_author = Projects.objects.get(pk=project).author_user
        project_contributors = Contributors.objects.filter(project=project).values_list('user__user_name', flat=True)

        IsObjectAuthor = request.user == obj.author_user
        IsProjectAuthor = request.user == project_author
        IsProjectContributors = f'{request.user}' in project_contributors

        print('OBJECT_TYPE = ', obj)
        print('OBJECT_AUTHOR : ', obj.author_user)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS PROJECT_AUTHOR", IsProjectAuthor)
        print("REQUEST_USER IN PROJECT_CONTRIBUTORS", IsProjectContributors)
        print('PROJECT_CONTRIBUTORS` : ', project_contributors)

        if request.method in self.edit_methods:
            return IsObjectAuthor
        else:
            return IsProjectAuthor or IsProjectContributors

class AllowAuthorEditIssuesOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        if f'{request.user}' == 'AnonymousUser':
            return False

        project = obj.project_id
        project_author = Projects.objects.get(pk=project).author_user
        project_contributors = Contributors.objects.filter(project=project).values_list('user__user_name', flat=True)

        IsObjectAuthor = request.user == obj.author_user
        IsProjectAuthor = request.user == project_author
        IsProjectContributors = f'{request.user}' in project_contributors

        print('OBJECT_TYPE = ', obj)
        print('OBJECT_AUTHOR : ', obj.author_user)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS PROJECT_AUTHOR", IsProjectAuthor)
        print("REQUEST_USER IN PROJECT_CONTRIBUTORS", IsProjectContributors)
        print('PROJECT_CONTRIBUTORS` : ', project_contributors)

        if request.method in self.edit_methods:
            return IsObjectAuthor
        else:
            return IsProjectAuthor or IsProjectContributors
