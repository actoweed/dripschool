from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Announcement, Assignment, Material
from django import forms
from .models import Course, Student

class AnnouncementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['description'].label = ''

    class Meta:
        model = Announcement
        fields = ['description']
        widgets = {
            'description': FroalaEditor(),
        }


class AssignmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ''
        self.fields['file'].required = False

    class Meta:
        model = Assignment
        fields = ('title', 'description', 'deadline', 'marks', 'file')
        widgets = {
            'description': FroalaEditor(),
            'title': forms.TextInput(attrs={'class': 'form-control mt-1', 'id': 'title', 'name': 'title', 'placeholder': 'Title'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control mt-1', 'id': 'deadline', 'name': 'deadline', 'type': 'datetime-local'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control mt-1', 'id': 'marks', 'name': 'marks', 'placeholder': 'Marks'}),
            'file': forms.FileInput(attrs={'class': 'form-control mt-1', 'id': 'file', 'name': 'file', 'aria-describedby': 'file', 'aria-label': 'Upload'}),
        }


class MaterialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ""
        self.fields['file'].required = False

    class Meta:
        model = Material
        fields = ('description', 'file')
        widgets = {
            'description': FroalaEditor(),
            'file': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'name': 'file', 'aria-describedby': 'file', 'aria-label': 'Upload'}),
        }


class CourseCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ""
        self.fields['facultyKey'].widget.attrs.update({'placeholder': 'Faculty Key'})
        self.fields['studentKey'].widget.attrs.update({'placeholder': 'Student Key'})

    class Meta:
        model = Course
        fields = ['name', 'department', 'studentKey', 'facultyKey']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'studentKey': forms.NumberInput(attrs={'class': 'form-control'}),
            'facultyKey': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ""
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})

    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password', 'department']
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }