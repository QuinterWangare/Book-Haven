from django import forms
from .models import TeamMember, Book, Review, ContactSubmission
class TeamMemberForm(forms.ModelForm):
    """
    Form for creating and updating team member records.
    """
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'profile_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'})
        }

class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = ['title', 'author', 'description', 'publication_date', 'status']
            widgets = {
                'ebook_file': forms.FileInput(attrs={'class': 'form-control-file'})
            }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'reviewer_name', 'reviewer_image']
        widgets = {
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your experience...',
                'rows': 4
            }),
            'reviewer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'reviewer_image': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }

class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message.strip():
            raise forms.ValidationError("Message is required.")
        return message