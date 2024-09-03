from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task, Comment, Category

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control', 'id': 'floatingInput', 'size':30})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control', 'id': 'floatingInput'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control ', 'id': 'floatingInput'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'confirm your password',
            'class': 'form-control ',
            'id': 'floatingInput',
            })
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control', 'id': 'floatingInput', 'size':30})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control ', 'id': 'floatingInput'})
    )
    class Meta:
        model = User
        fields = ['username', 'password']

class CategoryForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter category name', 'class': 'form-control', 'id': 'floatingInput', 'size':30})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter category description', 'class': 'form-control', 'id': 'floatingTextarea2', 'size':30, 'style':'height:200px;'})
    )

    class Meta:
        model = Category
        fields = ['name', 'description', 'user']



class TaskForm(forms.ModelForm):

    CHOICES = [
        ('IN PROGRESS', 'IN PROGRESS'),
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
    ]

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter task name', 'class': 'form-control', 'id': 'floatingInput', 'size':30})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter task description', 'class': 'form-control', 'id': 'floatingTextarea2', 'size':30, 'style':'height:200px;'})#noor
    )

    start_date = forms.DateField(input_formats=['%Y-%m-%d'])
    end_date = forms.DateField(input_formats=['%Y-%m-%d'])

    CATEGORIES = [(category.id, category) for category in Category.objects.all()]

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget = forms.Select(attrs={'class':'form-control pb-2'}),
        empty_label=None,
    ) 

    status = forms.ChoiceField(
        choices=CHOICES,
        widget = forms.Select(attrs={'class':'form-control pb-2'}),
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'start_date', 'end_date', 'category', 'user']