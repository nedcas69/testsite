from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class":"form-control", 'autocomplete' : "off"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-control", 'autofocus' : None}))
    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class":"form-control", 'autocomplete' : "off"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-control", 'autofocus' : None}))
    password2 = forms.CharField(label='Подтверждения пароля', widget=forms.PasswordInput(attrs={"class":"form-control", 'autofocus' : None}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class":"form-control", 'autocomplete' : "off"}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label='Название', widget=forms.TextInput(attrs={"class":"form-control"}))
    # content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={"class":"form-control", "rows":5}))
    # is_published = forms.BooleanField(label='Опубликовать', initial=True , widget=forms.CheckboxInput(attrs={"class":"form-check-input", "type":"checkbox"}))
    # category = forms.ModelChoiceField(empty_label='Выберите категорию',queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={"class":"form-select"}))
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'content': forms.Textarea(attrs={"class":"form-control", "rows":5}),
            'is_published': forms.CheckboxInput(attrs={"class":"form-check-input", "type":"checkbox"}),
            'category': forms.Select(attrs={"class":"form-select"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинатся с цифры')
        return title
