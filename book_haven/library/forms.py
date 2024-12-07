from django import forms
from .models import TeamMember, Book
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