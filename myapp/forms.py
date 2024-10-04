from django import forms

from myapp.models import Task

from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    class Meta:

        model=Task

        # fields="__all__"

        exclude=("created_date",
                 "status",
                 "updated_date")
        
        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "description":forms.Textarea(attrs={"class":"form-control"}),

            "due_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),

            "category":forms.Select(attrs={"class":"form_control"}),

            "user":forms.TextInput(attrs={"class":"form-control"}),


        }

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["first_name","last_name","username","email","password"]

        widgets={

            "first_name":forms.TextInput(attrs={"class":"form-control"}),

            "last_name":forms.TextInput(attrs={"class":"form-control"}),

            "email":forms.EmailInput(attrs={"class":"form-control"}),

            "username":forms.TextInput(attrs={"class":"form-control"}),

            "password":forms.TextInput(attrs={"class":"form_control"}),

            }

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

    widgets={

        "username":forms.TextInput(attrs={"class":"form-control"}),

        "password":forms.TextInput(attrs={"class":"form_control"}),

    }

