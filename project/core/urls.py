from cgitb import lookup
from django.contrib import admin
from django.urls import path, include
#from rest_framework import routers
from rest_framework_nested import routers

from core.views import ProjectsViewset, ContributorsViewset, IssuesViewset, CommentsViewset
 
router = routers.SimpleRouter()

router.register('projects', ProjectsViewset, basename='projects')
projects_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('contributors', ContributorsViewset, basename='project-contributors')
projects_router.register('issues', IssuesViewset, basename='project-issues')
issues_router = routers.NestedSimpleRouter(projects_router, 'issues', lookup='issue')
issues_router.register('comments', CommentsViewset, basename='projects-issues-comments')


urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
]

"""
router = routers.SimpleRouter()
router.register(r'domains', DomainViewSet)

domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
domains_router.register(r'nameservers', NameserverViewSet, basename='domain-nameservers')

from rest_framework_nested import routers
router = SimpleRouter()
router.register('libraries', views.LibraryViewSet)
book_router = routers.NestedSimpleRouter(router, r'libraries', lookup='library')
book_router.register(r'books', views.BookViewSet, basename='library-book')
app_name = 'library'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
]
"""