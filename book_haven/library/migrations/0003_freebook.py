# Generated by Django 5.1.3 on 2024-12-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_ebook_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='free_books_covers/')),
                ('download_link', models.URLField(blank=True, null=True)),
                ('ebook_file', models.FileField(blank=True, null=True, upload_to='free_books/')),
            ],
            options={
                'verbose_name_plural': 'Free Books',
            },
        ),
    ]
