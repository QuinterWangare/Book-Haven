from django.db import models

# Create your models here.
from django.core.validators import FileExtensionValidator

class TeamMember(models.Model):
    """
    Model representing a team member in the organization.
    Stores detailed information about each team member.
    """
    name = models.CharField(
        max_length=100,
        help_text="Full name of the team member"
    )
    position = models.CharField(
        max_length=100,
        help_text="Job title or role in the organization"
    )
    profile_image = models.ImageField(
        upload_to='team_images/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])],
        help_text="Profile image of the team member"
    )

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('borrowed', 'Borrowed')])

    ebook_file = models.FileField(
        upload_to='ebooks/',
        validators=[FileExtensionValidator(['pdf', 'epub', 'mobi'])],
        null=True,
        blank=True,
        help_text="Upload an ebook file (PDF, EPUB, or MOBI)"
    )

    def __str__(self):
        return self.title


class FreeBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='free_books_covers/', blank=True, null=True)
    download_link = models.URLField(blank=True, null=True)
    ebook_file = models.FileField(upload_to='free_books/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Free Books"


class PurchaseBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='purchase_books_covers/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100, blank=True, null=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - ${self.price}"

    class Meta:
        verbose_name_plural = "Purchase Books"

class Review(models.Model):
    name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    reviewer_image = models.ImageField(upload_to='reviewer_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s review of {self.book_title}"