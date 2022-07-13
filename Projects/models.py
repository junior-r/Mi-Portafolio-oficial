from django.db import models


icons = [
    ('', ''),
    ('icon-python', 'Python'),
    ('icon-data', 'SQLite'),
    ('icon-mysql', 'MySQL'),
    ('icon-git', 'GIT'),
    ('icon-github', 'GitHub'),
    ('icon-django', 'Django'),
    ('icon-css3', 'CSS'),
    ('icon-html5', 'HTML'),
]


class Project(models.Model):
    img = models.FileField(upload_to='Projects/', default='placeholder-image.png')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    url = models.URLField(max_length=250)
    logo1 = models.CharField(max_length=150, choices=icons)
    logo2 = models.CharField(max_length=150, choices=icons)
    logo3 = models.CharField(max_length=150, choices=icons)
    logo4 = models.CharField(max_length=150, choices=icons)
    logo5 = models.CharField(max_length=150, choices=icons)

    def __str__(self):
        return self.title
