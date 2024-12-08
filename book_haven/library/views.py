from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import TeamMember, Book, FreeBook, PurchaseBook, Review, ContactSubmission
from .forms import TeamMemberForm, BookForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def home(request):
    reviews = Review.objects.order_by('-created_at')  # Get all reviews
    context = {
        # Your existing context variables
        'reviews': reviews
    }
    return render(request, 'home.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace with your home URL or dashboard
        else:
            # Handle login failure
            pass

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, auto login the user after sign-up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or dashboard
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

class TeamMemberListView(ListView):
    """
    View to list all team members.
    """
    model = TeamMember
    template_name = 'team/team_list.html'
    context_object_name = 'team_members'

class TeamMemberCreateView(CreateView):
    """
    View to create a new team member record.
    """
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team/team_form.html'
    success_url = reverse_lazy('team_list')

class TeamMemberUpdateView(UpdateView):
    """
    View to update an existing team member record.
    """
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team/team_form.html'
    success_url = reverse_lazy('team_list')

class TeamMemberDeleteView(DeleteView):
    """
    View to delete a team member record.
    """
    model = TeamMember
    template_name = 'team/team_confirm_delete.html'
    success_url = reverse_lazy('team_list')

def books_view(request):
    books = Book.objects.all()
    return render(request, 'books.html', 'books', {'books': books})

def book_list(request):
    books = Book.objects.all()
    search_query = request.GET.get('search', '')

    # If there's a search query, filter the books
    if search_query:
        books = Book.objects.filter(
            # Use __icontains for case-insensitive partial matching
            # Search across title and author fields
            Q(title__icontains=search_query) | Q(author__icontains=search_query)
        )
    else:
        # If no search query, return all books
        books = Book.objects.all()

    return render(request, 'books.html', {'books': books, 'search_query': search_query})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})

def read_ebook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.ebook_file:
        messages.error(request, "No ebook file available for this book.")
        return redirect('book_list')
    return render(request, 'read_ebook.html', {'book': book})

def free_books(request):
    free_books = FreeBook.objects.all()
    context = {
        'free_books': free_books
    }
    return render(request, 'free_books.html', context)


def purchase_books(request):
    purchase_books = PurchaseBook.objects.all()

    # Get unique genres for the genre filter
    genres = purchase_books.values_list('genre', flat=True).distinct()

    context = {
        'purchase_books': purchase_books,
        'genres': [genre for genre in genres if genre]  # Remove empty genres
    }
    return render(request, 'purchase_books.html', context)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('home')  # Redirect back to home page
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Optional: Add a check to ensure only the review owner or an admin can delete
    if request.user.is_staff or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Review deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this review.')

    return redirect('home')


def user_reviews(request):
    # Fetch all reviews from the database
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'user_reviews.html', {'reviews': reviews})


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message', '')

        # Validate input
        if not name or not email:
            return JsonResponse({'success': False, 'error': 'Name and email are required.'}, status=400)

        # Save submission to database
        submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )

        return JsonResponse({'success': True, 'message': 'Thank you for your submission!'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)
