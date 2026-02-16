from django.db import models
from datetime import date
import uuid


class Student(models.Model):

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    current_academic_level_choices = [
        ('p1', 'Primary 1'),
        ('p2', 'Primary 2'),
        ('p3', 'Primary 3'),
        ('p4', 'Primary 4'),
        ('p5', 'Primary 5'),
        ('p6', 'Primary 6'),
    ]

    enrolled_status_choices = [
        ('Active', 'Active'),
        ('dismissed', 'Dismissed'),
        ('transferred', 'Transferred'),
        ('graduated', 'Graduated'),
        ('other', 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField('first name', max_length=55)
    last_name = models.CharField('last name', max_length=55)
    birth_date = models.DateField('birth date')
    gender = models.CharField('gender', max_length=55, choices=gender_choices, default='M')
    current_academic_level = models.CharField('current academic level', max_length=55, choices=current_academic_level_choices, default='p1')
    enrolled_status = models.CharField('enrolled status', max_length=55, choices=enrolled_status_choices, default='Active')
    photo = models.ImageField('photo', upload_to='students/photos', null=True, blank=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    @property
    def age(self):
        if not self.birth_date:
            return None
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

