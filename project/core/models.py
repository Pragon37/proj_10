from django.conf import settings
from django.db import models

#class Users(models.Model):
#    first_name = models.CharField(max_length=32)
#    last_name = models.CharField(max_length=32)
#    email = models.EmailField(max_length=128)
#    password = models.CharField(max_length=32)
#
#    def __str__(self):
#        return f'{self.first_name} {self.last_name}'
    
class Projects(models.Model):
    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    TYPE_CHOICES = [
        (BACKEND, 'Backend'),
        (FRONTEND, 'Frontend'),
        (IOS, 'Ios'),
        (ANDROID, 'Android'),
    ]
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=BACKEND, )
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT , related_name='projects')

    def __str__(self):
        return self.title

class Issues(models.Model):
    BUG = 'BUG'
    IMPROVMENT = 'IMPROVMENT'
    TASK = 'TASK'
    TAG_CHOICES = [
        (BUG, 'Bug'),
        (IMPROVMENT, 'Improvment'),
        (TASK, 'Task'),
     ]
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]        
    TODO = 'TODO'
    ONGOING = 'ONGOING'
    DONE = 'DONE'

    STATUS_CHOICES = [
        (TODO, 'Todo'),
        (ONGOING, 'Ongoing'),
        (DONE, 'Done'),
    ]     

       
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES, default=BUG, )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW, )
    project = models.ForeignKey(Projects, on_delete=models.PROTECT , related_name='issues')    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO, )
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT , related_name='author_issues')
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT , related_name='assignee_issues', blank=True)
    created_time =  models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
      if not hasattr(self, 'assignee_user'):
        self.assignee_user = self.author_user
      super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.project} {self.author_user} {self.assignee_user}'



class Comments(models.Model):
    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT , related_name='comments')
    issue = models.ForeignKey(Issues, on_delete=models.PROTECT , related_name='comments')
    created_time =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description} {self.author_user} {self.issue}'

class Contributors(models.Model):
    READ = 'READ'
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    PERMISSION_CHOICES = [
        (READ, 'Read'),
        (CREATE, 'Create'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
     ]

    AUTHOR = 'AUTHOR'
    OWNER = 'OWNER'
    REVIEWER = 'REVIEWER'
    ROLE_CHOICES = [
        (AUTHOR, 'Author'),
        (OWNER, 'Owner'),
        (REVIEWER, 'Reviewer'),
     ]
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT , related_name='contributors')
    project = models.ForeignKey(Projects, on_delete=models.PROTECT , related_name='contributors')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=REVIEWER, )
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default=READ, )

    def __str__(self):
        return f'{self.user} {self.role} {self.project}'