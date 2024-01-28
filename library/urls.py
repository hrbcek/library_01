"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from account.views import SignUpView, profile_view
from viewer.models import Book, Person, Category, Image
from viewer.views import IndexView, CategoryView, BookListView, BookDetailView, borrow_book, return_book

admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Image)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('category/<pk>/', CategoryView.as_view(), name='category'),
    path('book_list/<pk>/', BookListView.as_view(), name='book_list'),
    path('book_detail/<pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:book_id>/borrow/', borrow_book, name='borrow_book'),
    path('book/<int:book_id>/return/', return_book, name='return_book'),

    path('account/login/', LoginView.as_view(), name='login'),  # v djangu už to máme
    path('account/register/', SignUpView.as_view(), name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('account/', include('django.contrib.auth.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
