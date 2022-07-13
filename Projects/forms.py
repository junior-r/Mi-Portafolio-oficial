from django import forms
from Projects.models import Project


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


class ProjectForm(forms.ModelForm):
    img = forms.ImageField(label='Imágen del Proyecto', required=False, widget=forms.FileInput())
    title = forms.CharField(label='Título del Proyecto', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Descripción del Proyecto', required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    url = forms.CharField(label='URL del repositorio', required=True, widget=forms.URLInput(attrs={'class': 'form-control'}))
    logo1 = forms.ChoiceField(label='Logo 1 del proyecto', required=True, choices=icons, widget=forms.Select(attrs={'class': 'form-control'}))
    logo2 = forms.ChoiceField(label='Logo 2 del proyecto', required=False, choices=icons, widget=forms.Select(attrs={'class': 'form-control'}))
    logo3 = forms.ChoiceField(label='Logo 3 del proyecto', required=False, choices=icons, widget=forms.Select(attrs={'class': 'form-control'}))
    logo4 = forms.ChoiceField(label='Logo 4 del proyecto', required=False, choices=icons, widget=forms.Select(attrs={'class': 'form-control'}))
    logo5 = forms.ChoiceField(label='Logo 5 del proyecto', required=False, choices=icons, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Project
        fields = ['img', 'title', 'description', 'url', 'logo1', 'logo2', 'logo3', 'logo4', 'logo5']
