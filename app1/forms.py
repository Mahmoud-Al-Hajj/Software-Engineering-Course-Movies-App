from django.forms import ModelForm
from .models import Student,Course_Taken,Movie
from django import forms


class CreateStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['Student_id', 'Student_name', 'gpa']

class CreateCourseForm(ModelForm):
	class Meta:
		model = Course_Taken
		fields = ['Student_id', 'Course_id', 'Semester','Number_of_credits','Grade']

class GPAForm(forms.Form):
	Student_id = forms.IntegerField()

class CreateMovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ['Movie_id', 'Movie_name', 'Movie_genre', 'Movie_description', 'Release_year', 'Movie_rating']
