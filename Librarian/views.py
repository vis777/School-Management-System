from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView, View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Backend.models import LibrarianDb, StudentDb, BookDb, FeesDb
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LibrarianLoginForm  

# Create your views here.
class LibrarianView(TemplateView):
    template_name = "Librarian.html"

class LibrarianLoginView(FormView):
    template_name = "Logreg1.html"  
    form_class = LibrarianLoginForm  # Updated form class
    success_url = reverse_lazy('librarianpage')  

    def form_valid(self, form):
        un = form.cleaned_data['librarian_user_name']  # Updated cleaned data field
        pwd = form.cleaned_data['librarian_pass_word']  # Updated cleaned data field
        librarian = LibrarianDb.objects.filter(UserNaMe=un, PassWoRd=pwd).first()  # Updated model

        if librarian:
            # Set session values
            self.request.session['LoginId'] = librarian.id
            self.request.session['LibrarianName'] = librarian.First_Name + " " + librarian.Last_Name
            messages.success(self.request, "Login successful")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username or password")
            return redirect('librarian_login')  # Updated redirect URL

    def form_invalid(self, form):
        messages.error(self.request, "Form validation failed")
        return redirect('librarian_login')  # Updated redirect URL

class LibrarianLogoutView(View):
    def get(self, request, *args, **kwargs):
        if 'LoginId' in request.session:
            del request.session['LoginId']
        if 'LibrarianName' in request.session:
            del request.session['LibrarianName']

        messages.success(request, "Logout successful")
        return redirect('librarian_login')  # Updated redirect URL

class StudentListView(ListView):
    model = StudentDb
    template_name = 'StudentManage.html' 
    context_object_name = 'stu'

class BookCreateView(SuccessMessageMixin, CreateView):
    model = BookDb
    template_name = "Book.html"
    fields = ['student', 'book_title', 'status', 'borrow_date', 'return_date'] 
    success_url = reverse_lazy('managebooks')
    success_message = "Book added successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all()  
        return context


class BookListView(ListView):
    model = BookDb
    template_name = 'LibrarianManage.html'
    context_object_name = 'books'

class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = BookDb
    template_name = 'Bookedit.html'
    fields = ['student', 'book_title', 'status', 'borrow_date', 'return_date']
    success_url = reverse_lazy('managebooks')
    success_message = "Book updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all() 
        return context

class BookDeleteView(DeleteView):
    model = BookDb
    template_name = 'confirm_delete.html' 
    success_url = reverse_lazy('managebooks')
    success_message = "Book deleted successfully!"

class FeesListView(ListView):
    model = FeesDb
    template_name = 'FeeManage.html'
    context_object_name = 'fees'