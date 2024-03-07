from django.db import models
from django.core.exceptions import ValidationError
import os
from django_ckeditor_5.fields import CKEditor5Field


gender =(
    ('Male', 'Male'),
    ('Female', 'Female')
)
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.giff']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def user_directory_path(request, filename):
    return '/'.join(['content', request.contact, filename])


# Create your models here.
class Person(models.Model): 
    first_name = models.CharField(max_length=30) # String
    last_name = models.CharField(max_length=120) # String
    gender = models.CharField(max_length=7, choices=gender) # String 
    dob = models.DateField()
    avatar = models.FileField(blank=True, upload_to=user_directory_path,  validators=[validate_file_extension])
    contact = models.CharField(max_length=150, blank=True, null=True)
    active = models.BooleanField(default=True)
    description = CKEditor5Field('Text', config_name='extends', blank=True, null=True)
    def __str__(self) -> str:
        return str(self.first_name)+' '+str(self.last_name)

class Course(models.Model): 
    title = models.CharField(max_length=120)
    activate = models.BooleanField(default=True)
    def __str__(self) -> str:
        return str(self.title)

class Score(models.Model): 
    title = models.CharField(max_length=120)
    person = models.ForeignKey(Person, related_name='person_score', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='course_score', on_delete = models.CASCADE)
    activate = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title
    
class Province(models.Model):
    pass 
class District(models.Model): 
    pass 
   