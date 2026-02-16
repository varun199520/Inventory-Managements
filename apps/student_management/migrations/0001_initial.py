# Generated manually to match Student model

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=55, verbose_name='first name')),
                ('last_name', models.CharField(max_length=55, verbose_name='last name')),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=55, verbose_name='gender')),
                ('current_academic_level', models.CharField(choices=[('p1', 'Primary 1'), ('p2', 'Primary 2'), ('p3', 'Primary 3'), ('p4', 'Primary 4'), ('p5', 'Primary 5'), ('p6', 'Primary 6')], default='p1', max_length=55, verbose_name='current academic level')),
                ('enrolled_status', models.CharField(choices=[('Active', 'Active'), ('dismissed', 'Dismissed'), ('transferred', 'Transferred'), ('graduated', 'Graduated'), ('other', 'Other')], default='Active', max_length=55, verbose_name='enrolled status')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students/photos', verbose_name='photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
    ]
