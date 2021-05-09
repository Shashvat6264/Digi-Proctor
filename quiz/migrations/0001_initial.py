# Generated by Django 3.2.2 on 2021-05-08 19:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('questionName', models.CharField(max_length=200, verbose_name='Question Name: ')),
                ('questionDesc', models.CharField(max_length=400, verbose_name='Question Decription: ')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('quizName', models.CharField(max_length=20, verbose_name='Quiz Name: ')),
                ('noOfQns', models.IntegerField(verbose_name='Number of Questions: ')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseQuiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('response', models.CharField(max_length=500)),
                ('windowChange', models.IntegerField()),
                ('windowAwayTime', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('responseQuiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.responsequiz')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionQuiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz', verbose_name='Quiz: '),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.CharField(choices=[('Prof', 'Prof'), ('STUDENT', 'Student')], default='STUDENT', max_length=50, verbose_name='Type')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name of User')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('quiz.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('quiz.user',),
        ),
        migrations.AddField(
            model_name='responsequiz',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.student'),
        ),
    ]
