from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser

from core.models import Projects, Contributors, Issues, Comments


class AllowContributorsOnly(BasePermission):

    message = 'Project access is restricted to contributors only.'

    def has_permission(self, request, view):
        print('--------')
        if Contributors.objects.filter(user=request.user).exists():
            return True

class AllowContributorsEdit(BasePermission):
    edit_methods = ("DELETE", "POST", )

    def has_permission(self, request, view):
        if f'{request.user}' == 'AnonymousUser':
            return False
        project = view.kwargs.get('project_pk')
        project_author = Projects.objects.get(pk=project).author_user
        isprojectauthor = request.user == project_author
        iscontributor = Contributors.objects.filter(user=request.user).exists()
        print('--------')
        print('PROJECT : ', project)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS PROJECT_AUTHOR", isprojectauthor)
        print('--------')

        if request.method in self.edit_methods:
            return isprojectauthor
        else:
            return iscontributor


"""class AllowAuthorEditCommentsOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        if f'{request.user}' == 'AnonymousUser':
            return False

        project = obj.issue.project_id
        project_author = Projects.objects.get(pk=project).author_user
        project_contributors = Contributors.objects.filter(project=project).values_list('user__user_name', flat=True)

        isobjectauthor = request.user == obj.author_user
        isprojectauthor = request.user == project_author
        isprojectcontributors = f'{request.user}' in project_contributors

        print('HASATTR_ISSUE = ', hasattr(obj, 'issue'))
        print('HASATTR_PROJECT_ID = ', hasattr(obj, 'project_id'))
        print('OBJECT_AUTHOR : ', obj.author_user)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS PROJECT_AUTHOR", isprojectauthor)
        print("REQUEST_USER IN PROJECT_CONTRIBUTORS", isprojectcontributors)
        print('PROJECT_CONTRIBUTORS` : ', project_contributors)

        if request.method in self.edit_methods:
            return isobjectauthor
        else:
            return isprojectauthor or isprojectcontributors

class AllowAuthorEditIssuesOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        if f'{request.user}' == 'AnonymousUser':
            return False

        project = obj.project_id
        project_author = Projects.objects.get(pk=project).author_user
        project_contributors = Contributors.objects.filter(project=project).values_list('user__user_name', flat=True)

        isobjectauthor = request.user == obj.author_user
        isprojectauthor = request.user == project_author
        isprojectcontributors = f'{request.user}' in project_contributors

        print('HASATTR_ISSUE = ', hasattr(obj, 'issue'))
        print('HASATTR_PROJECT_ID = ', hasattr(obj, 'project_id'))
        print('OBJECT_AUTHOR : ', obj.author_user)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS PROJECT_AUTHOR", isprojectauthor)
        print("REQUEST_USER IN PROJECT_CONTRIBUTORS", isprojectcontributors)
        print('PROJECT_CONTRIBUTORS` : ', project_contributors)

        if request.method in self.edit_methods:
            return isobjectauthor
        else:
            return isprojectauthor or isprojectcontributors
"""

class AllowAuthorEditOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE", )
    create_methods = ("POST", )

    def has_permission(self, request, view):
        if f'{request.user}' == 'AnonymousUser':
            return False
        project = view.kwargs.get('project_pk')
        project_author = Projects.objects.get(pk=project).author_user
        isprojectauthor = request.user == project_author
        iscontributor = Contributors.objects.filter(user=request.user, project_id=project).exists()
        print('--------')
        print('PROJECT : ', project)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS ALLOWED", isprojectauthor or iscontributor)
        print('--------')

        if request.method in self.create_methods:
            return isprojectauthor or iscontributor
        else:
            return True

  

    def has_object_permission(self, request, view, obj):
        if f'{request.user}' == 'AnonymousUser':
            return False

        if hasattr(obj, 'project_id'):
            #This is an issue
            project = obj.project_id
        elif hasattr(obj, 'issue'):
            #This is a comment
            project = obj.issue.project_id

        project_author = Projects.objects.get(pk=project).author_user
        project_contributors = Contributors.objects.filter(project=project).values_list('user__user_name', flat=True)

        isobjectauthor = request.user == obj.author_user
        isprojectauthor = request.user == project_author
        isprojectcontributors = f'{request.user}' in project_contributors

        print('HASATTR_ISSUE = ', hasattr(obj, 'issue'))
        print('HASATTR_PROJECT_ID = ', hasattr(obj, 'project_id'))
        print('OBJECT_AUTHOR : ', obj.author_user)
        print('PROJECT_AUTHOR : ', project_author)
        print("REQUEST_USER   ", f'{request.user}')
        print("REQUEST_USER IS PROJECT_AUTHOR", isprojectauthor)
        print("REQUEST_USER IN PROJECT_CONTRIBUTORS", isprojectcontributors)
        print('PROJECT_CONTRIBUTORS` : ', project_contributors)

        if request.method in self.edit_methods:
            return isobjectauthor
        else:
            return isprojectauthor or isprojectcontributors
