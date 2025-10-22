from django.db import models
import django.core.validators as validators


class Student(models.Model):
    Student_id= models.IntegerField(primary_key=True)
    Student_name = models.CharField(max_length=30)
    gpa = models.IntegerField(default=0)


class Course_Taken(models.Model):
    Student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    Course_id= models.IntegerField()
    Semester=models.CharField(max_length=100)
    Number_of_credits= models.IntegerField()
    Grade = models.IntegerField()
    
class Movie(models.Model):
    Movie_id = models.IntegerField()
    Movie_name = models.CharField(max_length=100)
    Movie_genre = models.CharField(max_length=100)
    Movie_description = models.CharField(max_length=300)
    Release_year = models.IntegerField(validators=[validators.MinValueValidator(1900)])
    Movie_rating = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)])