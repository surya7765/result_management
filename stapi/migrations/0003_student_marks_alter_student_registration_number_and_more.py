# Generated by Django 4.1.2 on 2022-10-22 10:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stapi', '0002_remove_subject_subject_code_alter_submarks_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.ManyToManyField(through='stapi.SubMarks', to='stapi.subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='submarks',
            name='obtained_marks',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='submarks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submarks', to='stapi.student'),
        ),
        migrations.AlterField(
            model_name='submarks',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='stapi.subject'),
        ),
        migrations.AlterField(
            model_name='submarks',
            name='total_marks',
            field=models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
