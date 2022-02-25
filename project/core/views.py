
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
        return Contributors.objects.all()

class IssuesViewset(ModelViewSet):
 
    serializer_class = IssuesListSerializer
 
    def get_queryset(self):
        return Issues.objects.all()

class CommentsViewset(ModelViewSet):
 
    serializer_class = CommentsListSerializer
 
    def get_queryset(self):
        return Comments.objects.all()