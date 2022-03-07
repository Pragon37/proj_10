
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

 
from core.models import Projects, Contributors, Issues, Comments
from core.serializers import ProjectsListSerializer, ContributorsListSerializer, IssuesListSerializer, ReadCommentsListSerializer, WriteCommentsListSerializer
from core.permissions import AllowContributorsOnly, AllowContributorsEdit, AllowAuthorEditOrReadOnly
 
class ProjectsViewset(ModelViewSet):
    """WET, not DRY : IsAuthenticated must be set in view to avoid Internal Server Error when not authenticated.
       Having it only in settings provokes an Internal Server Error !! Issue is not 100% though"""
    serializer_class = ProjectsListSerializer
    permission_classes = [IsAuthenticated, AllowContributorsOnly,]

 
    def get_queryset(self):
        return Projects.objects.all()

class ContributorsViewset(ModelViewSet):
 
    serializer_class = ContributorsListSerializer
    permission_classes = [IsAuthenticated, AllowContributorsEdit, AllowContributorsOnly ]

    def get_queryset(self):
        return Contributors.objects.filter(project=self.kwargs['project_pk'])

class IssuesViewset(ModelViewSet):
 
    serializer_class = IssuesListSerializer
    permission_classes = [IsAuthenticated, AllowContributorsOnly, AllowAuthorEditOrReadOnly,]

 
    def get_queryset(self):
        return Issues.objects.filter(project=self.kwargs['project_pk'])


class CommentsViewset(ModelViewSet):
 
    permission_classes = [IsAuthenticated, AllowContributorsOnly, AllowAuthorEditOrReadOnly]
 
    def get_queryset(self):
        return Comments.objects.filter(issue=self.kwargs['issue_pk'], issue__project__pk=self.kwargs['project_pk'])

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadCommentsListSerializer
        return WriteCommentsListSerializer

