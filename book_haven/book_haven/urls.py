"""
URL configuration for book_haven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from library import views
from library.views import books_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('team/', views.TeamMemberListView.as_view(), name='team_list'),
    path('team/new/', views.TeamMemberCreateView.as_view(), name='team_create'),
    path('team/<int:pk>/edit/', views.TeamMemberUpdateView.as_view(), name='team_update'),
    path('team/<int:pk>/delete/', views.TeamMemberDeleteView.as_view(), name='team_delete'),
    path('books/', views.book_list, name='books'),
    path('book_list/', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('read_ebook/<int:book_id>/', views.read_ebook, name='read_ebook'),
    path('free-books/', views.free_books, name='free_books'),
    path('purchase-books/', views.purchase_books, name='purchase_books'),
    path('reviews/', views.user_reviews, name='user_reviews'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('reviews/submit/', views.submit_review, name='submit_review'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)