# Generated by Django 4.1.1 on 2022-09-05 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=50)),
                ('usecase', models.TextField()),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body_content', models.TextField()),
                ('description', models.TextField(default='Open the post to read more about!')),
                ('publi', models.BooleanField(default=False)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]
