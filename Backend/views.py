from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import AdminLoginForm
from .models import OfficeStaffDb, LibrarianDb, StudentDb, BookDb, FeesDb

# Create your views here.
class AdminPageView(TemplateView):
    template_name = "adminindex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Count the number of Office Staff, Librarians, and Students
        context['staff_count'] = OfficeStaffDb.objects.count()
        context['librarian_count'] = LibrarianDb.objects.count()
        context['student_count'] = StudentDb.objects.count()
        return context

class AdminLoginView(FormView):
    template_name = "AdminLogin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy('adminpage')

    def form_valid(self, form):
        un = form.cleaned_data['user_name']
        pwd = form.cleaned_data['pass_word']
        user = User.objects.filter(username__contains=un).exists()
        if user:
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(self.request, x)
                self.request.session['username'] = un
                self.request.session['password'] = pwd
                messages.success(self.request, "Login successful")
                return super().form_valid(form)
            else:
                messages.error(self.request, "Invalid Username or Password")
        else:
            messages.error(self.request, "Invalid Username or Password")
        return redirect('admin_login')

class AdminLogoutView(View):
    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            del request.session['username']
        messages.success(request, "Logout successful")
        return redirect('admin_login')

class OfficeStaffCreateView(SuccessMessageMixin, CreateView):
    model = OfficeStaffDb
    template_name = "admin/Add Officestaff.html"
    fields = ['First_Name', 'Last_Name', 'Place', 'Post', 'Pin', 'Email', 'Phone', 'UserNaMe', 'PassWoRd']
    success_url = reverse_lazy('add_officestaff')
    success_message = "Staff added successfully!"

class OfficeStaffListView(ListView):
    model = OfficeStaffDb
    template_name = 'admin/Add and Manage Officestaff.html'
    context_object_name = 'off'

class OfficeStaffUpdateView(SuccessMessageMixin, UpdateView):
    model = OfficeStaffDb
    template_name = "admin/Edit Officestaff.html"
    fields = ['First_Name', 'Last_Name', 'Place', 'Post', 'Pin', 'Email', 'Phone']
    success_url = reverse_lazy('manage_officestaff')
    success_message = "Office staff updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offi'] = self.get_object()  
        return context


class OfficeStaffDeleteView(DeleteView):
    model = OfficeStaffDb
    template_name = "admin/Delete Confirmation.html"
    success_url = reverse_lazy('manage_officestaff')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class LibrarianCreateView(SuccessMessageMixin, CreateView):
    model = LibrarianDb
    template_name = "admin/Add Librarian.html"
    fields = ['First_Name', 'Last_Name', 'Place', 'Post', 'Pin', 'Email', 'Phone', 'UserNaMe', 'PassWoRd']
    success_url = reverse_lazy('add_librarian')
    success_message = "Librarian added successfully!"

class LibrarianListView(ListView):
    model = LibrarianDb
    template_name = 'admin/Add and Manage Librarian.html'
    context_object_name = 'off'

class LibrarianUpdateView(SuccessMessageMixin, UpdateView):
    model = LibrarianDb
    template_name = "admin/Edit Librarian.html"
    fields = ['First_Name', 'Last_Name', 'Place', 'Post', 'Pin', 'Email', 'Phone']
    success_url = reverse_lazy('manage_librarian')
    success_message = "librarian updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lib'] = self.get_object()  
        return context


class LibrarianDeleteView(DeleteView):
    model = LibrarianDb
    template_name = "admin/Delete Confirmation.html"
    success_url = reverse_lazy('manage_officestaff')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = StudentDb
    template_name = "admin/Add Student.html"
    fields = ['UserNaMe', 'First_Name', 'Last_Name', 'Class_Name', 'Email', 'DOB'] 
    success_url = reverse_lazy('add_student')
    success_message = "Student added successfully!"

class StudentListView(ListView):
    model = StudentDb
    template_name = 'admin/Add and Manage Student.html'
    context_object_name = 'stu'

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = StudentDb
    template_name = "admin/Edit Student.html"
    fields = ['UserNaMe', 'First_Name', 'Last_Name', 'Class_Name', 'Email', 'DOB']
    success_url = reverse_lazy('manage_student')
    success_message = "student updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stud'] = self.get_object()  
        return context


class StudentDeleteView(DeleteView):
    model = StudentDb
    template_name = "admin/Delete Confirmation.html"
    success_url = reverse_lazy('manage_student')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class BookCreateView(SuccessMessageMixin, CreateView):
    model = BookDb
    template_name = "admin/Add Book.html"
    fields = ['student', 'book_title', 'status', 'borrow_date', 'return_date'] 
    success_url = reverse_lazy('add_book')
    success_message = "Book added successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all()  
        return context

class BookListView(ListView):
    model = BookDb
    template_name = 'admin/Add and Manage Book.html'
    context_object_name = 'books'

class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = BookDb
    template_name = 'admin/Edit Book.html'
    fields = ['student', 'book_title', 'status', 'borrow_date', 'return_date']
    success_url = reverse_lazy('manage_books')
    success_message = "Book updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all() 
        return context

class BookDeleteView(DeleteView):
    model = BookDb
    template_name = 'admin/confirm_delete.html' 
    success_url = reverse_lazy('manage_books')
    success_message = "Book deleted successfully!"

class FeesCreateView(SuccessMessageMixin, CreateView):
    model = FeesDb
    template_name = "admin/Add Fees.html"
    fields = ['student', 'amount_paid', 'due_amount', 'payment_date', 'payment_method', 'fees_status'] 
    success_url = reverse_lazy('add_fee')
    success_message = "Fees added successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all()
        return context

class FeesListView(ListView):
    model = FeesDb
    template_name = 'admin/Add and Manage Fees.html'
    context_object_name = 'fee'

class FeesUpdateView(SuccessMessageMixin, UpdateView):
    model = FeesDb
    template_name = 'admin/Edit Fees.html'
    fields = ['student', 'amount_paid', 'due_amount', 'payment_date', 'payment_method', 'fees_status']
    success_url = reverse_lazy('manage_fees')
    success_message = "Fees updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all() 
        return context

class FeesDeleteView(DeleteView):
    model = FeesDb
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('manage_fees')
    success_message = "Fees deleted successfully!"