# Generated by Django 5.1.3 on 2024-12-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_rename_name_review_reviewer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
