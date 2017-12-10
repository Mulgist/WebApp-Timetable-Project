# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('calendar_id', models.AutoField(primary_key=True, serialize=False, verbose_name='calendar_id')),
                ('date', models.DateField(verbose_name='date')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('start_time', models.TimeField(verbose_name='start_time')),
                ('end_time', models.TimeField(verbose_name='end_time')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False, verbose_name='class_id')),
                ('class_name', models.CharField(max_length=128, verbose_name='class_name')),
                ('professor', models.CharField(max_length=32, verbose_name='professor')),
                ('credit', models.IntegerField(verbose_name='credit')),
            ],
        ),
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('classtime_id', models.AutoField(primary_key=True, serialize=False, verbose_name='classtime_id')),
                ('start_time', models.TimeField(verbose_name='start_time')),
                ('end_time', models.TimeField(verbose_name='end_time')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_id', models.AutoField(primary_key=True, serialize=False, verbose_name='grade_id')),
                ('grade', models.CharField(default='F', max_length=3, verbose_name='grade')),
                ('score', models.FloatField(default=0.0, verbose_name='score')),
                ('is_score', models.BooleanField(default=True, verbose_name='is_score')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('memo_id', models.AutoField(primary_key=True, serialize=False, verbose_name='memo_id')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_time')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='published_date')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('period_id', models.AutoField(primary_key=True, serialize=False, verbose_name='period_id')),
                ('year', models.IntegerField(verbose_name='year')),
                ('start_month', models.IntegerField(verbose_name='start_month')),
                ('week', models.IntegerField(verbose_name='week')),
                ('start_day', models.IntegerField(verbose_name='start_day')),
                ('end_day', models.IntegerField(verbose_name='end_day')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False, verbose_name='semester_id')),
                ('semester_name', models.CharField(max_length=32, unique=True, verbose_name='semester_name')),
                ('start_day', models.DateField(verbose_name='start_day')),
                ('end_day', models.DateField(verbose_name='end_day')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='memo',
            name='period_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Period'),
        ),
        migrations.AddField(
            model_name='class',
            name='semester_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Semester'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Class'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='period_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Period'),
        ),
    ]
