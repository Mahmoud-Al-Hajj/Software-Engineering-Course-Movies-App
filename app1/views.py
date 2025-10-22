from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreateStudentForm,CreateCourseForm,GPAForm,CreateMovieForm
from .models import Student,Course_Taken
from .models import Movie
from django.shortcuts import get_object_or_404, redirect


def index(request):
	return render(request,'index.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, Movie_id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            movie_data = form.cleaned_data
            movie_id = movie_data['Movie_id']
            movie_name = movie_data['Movie_name']
            movie_genre = movie_data['Movie_genre']
            movie_description = movie_data['Movie_description']
            release_year = movie_data['Release_year']
            movie_rating = movie_data['Movie_rating']
            Movie.objects.create(Movie_id=movie_id, Movie_name=movie_name, Movie_genre=movie_genre, Movie_description=movie_description, Release_year=release_year, Movie_rating=movie_rating)
            return render(request, 'index.html')
    else:
        form = CreateMovieForm()
    S = Movie.objects.all()
    return render(request, 'add_movie.html', {'form': form, 'S': S})

def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, Movie_id=movie_id)
    if request.method == 'POST':
        form = CreateMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = CreateMovieForm(instance=movie)
    return render(request, 'update_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, Movie_id=movie_id)
    movie.delete()
    return redirect('movie_list')



def add_student(request):
	if request.method == 'POST':
		form = CreateStudentForm(request.POST)
		if form.is_valid():
			studentform = form.cleaned_data
			first = studentform['Student_id']
			last = studentform['Student_name']
			Student.objects.create(Student_id=first,Student_name=last)
			return render(request, 'index.html')
	else:
		form = CreateStudentForm()
	S=Student.objects.all()
	return render(request, 'add_student.html', {'form': form,'S':S})


def add_course(request):
	if request.method == 'POST':
		form = CreateCourseForm(request.POST)
		if form.is_valid():
			courseform = form.cleaned_data
			Student_id = courseform['Student_id']
			Course_id = courseform['Course_id']
			Semester = courseform['Semester']
			Number_of_credits = courseform['Number_of_credits']
			Grade = courseform['Grade']
			Course_Taken.objects.create(Student_id=Student_id,Course_id=Course_id,Semester=Semester,Number_of_credits=Number_of_credits,Grade=Grade)

			listing = Course_Taken.objects.filter(Student_id=Student_id)
			summ = 0.0
			credits = 0
			for l in listing:
				summ =summ+ l.Grade * l.Number_of_credits
				credits =credits+ l.Number_of_credits
			avg = summ / credits
			for e in Student.objects.all():
				if e.Student_id==Student_id:
					e.object.set(gpa=avg)
			return render(request, 'index.html')
	else:
		form = CreateCourseForm()
	S=Course_Taken.objects.all()
	return render(request, 'add_course.html', {'form': form,'S':S})

def report(request):
	if request.method == 'POST':
		form = GPAForm(request.POST)

		if form.is_valid():
			courseform = form.cleaned_data
			Student_id = courseform['Student_id']

			for e in Student.objects.all():
				if e.Student_id==Student_id:
					A=e
			return render(request, 'report_student.html', { 'form': form,'A':A})
		
	else:
		form= GPAForm()
	return render(request,'report_student.html',{'form':form})