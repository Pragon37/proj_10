
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

 
from core.models import Projects, Contributors, Issues, Comments
from core.serializers import ProjectsListSerializer, ContributorsListSerializer, IssuesListSerializer, CommentsListSerializer
 
class ProjectsViewset(ModelViewSet):
 
    serializer_class = ProjectsListSerializer
    #permission_classes = [IsAuthenticated]

 
    def get_queryset(self):
        return Projects.objects.all()

class ContributorsViewset(ModelViewSet):
 
    serializer_class = ContributorsListSerializer
 
    def get_queryset(self):
        return Contributors.objects.filter(project=self.kwargs['project_pk'])

class IssuesViewset(ModelViewSet):
 
    serializer_class = IssuesListSerializer
 
    def get_queryset(self):
        return Issues.objects.filter(project=self.kwargs['project_pk'])


class CommentsViewset(ModelViewSet):
 
    serializer_class = CommentsListSerializer
 
    def get_queryset(self):
        print('---', Comments.objects.filter(issue__project__pk=2))
        return Comments.objects.filter(issue=self.kwargs['issue_pk'], issue__project__pk=self.kwargs['project_pk'])