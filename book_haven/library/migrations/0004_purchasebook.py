# Generated by Django 5.1.3 on 2024-12-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_freebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='purchase_books_covers/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('is_bestseller', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Purchase Books',
            },
        ),
    ]
