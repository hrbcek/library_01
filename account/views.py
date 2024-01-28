from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from account.forms import SignUpForm
from account.models import Profile
from viewer.models import BorrowedBook


# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        profile = Profile.objects.get(user=self.object)
        profile.op = form.cleaned_data['op']
        profile.title = form.cleaned_data['title']
        profile.gender = form.cleaned_data['gender']
        profile.birth_date = form.cleaned_data['birth_date']
        profile.mobile_number = form.cleaned_data['mobile_number']
        profile.address = form.cleaned_data['address']
        profile.save()
        return response

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    borrowed_books = BorrowedBook.objects.filter(user=request.user)

    context = {
        'profile': profile,
        'borrowed_books': borrowed_books,
    }

    return render(request, 'profile.html', context)

