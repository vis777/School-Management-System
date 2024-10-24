from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView, View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Backend.models import OfficeStaffDb, StudentDb, LibrarianDb, FeesDb, BookDb
from .forms import OfficeStaffLoginForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class OfficeStaffView(TemplateView):
    template_name = "Officestaff.html"

class OfficeStaffLoginView(FormView):
    template_name = "Logreg.html"  
    form_class = OfficeStaffLoginForm
    success_url = reverse_lazy('officestaffpage')  

    def form_valid(self, form):
        un = form.cleaned_data['officestaff_user_name']
        pwd = form.cleaned_data['officestaff_pass_word']
        officestaff = OfficeStaffDb.objects.filter(UserNaMe=un, PassWoRd=pwd).first()

        if officestaff:
            # Set session values
            self.request.session['LoginId'] = officestaff.id
            self.request.session['OffStaffName'] = officestaff.First_Name + " " + officestaff.Last_Name
            messages.success(self.request, "Login successful")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username or password")
            return redirect('officestaff_login')

    def form_invalid(self, form):
        messages.error(self.request, "Form validation failed")
        return redirect('officestaff_login')

class OfficeStaffLogoutView(View):
    def get(self, request, *args, **kwargs):
        if 'LoginId' in request.session:
            del request.session['LoginId']
        if 'OffStaffName' in request.session:
            del request.session['OffStaffName']

        messages.success(request, "Logout successful")
        return redirect('officestaff_login')

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = StudentDb
    template_name = "Student.html"
    fields = ['UserNaMe', 'First_Name', 'Last_Name', 'Class_Name', 'Email', 'DOB'] 
    success_url = reverse_lazy('managestudents')
    success_message = "Student added successfully!"

class StudentListView(ListView):
    model = StudentDb
    template_name = 'ManageStudents.html' 
    context_object_name = 'stu'

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = StudentDb
    template_name = "Studentedit.html"
    fields = ['UserNaMe', 'First_Name', 'Last_Name', 'Class_Name', 'Email', 'DOB']
    success_url = reverse_lazy('managestudents')
    success_message = "student updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stud'] = self.get_object()  
        return context


class StudentDeleteView(DeleteView):
    model = StudentDb
    template_name = "Officestaff/Delete Confirmation.html"
    success_url = reverse_lazy('managestudents')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class BookListView(ListView):
    model = BookDb
    template_name = 'ManageLibrarian.html'
    context_object_name = 'books'

class FeesCreateView(SuccessMessageMixin, CreateView):
    model = FeesDb
    template_name = "Fees.html"  
    fields = ['student', 'amount_paid', 'due_amount', 'payment_date', 'payment_method', 'fees_status'] 
    success_url = reverse_lazy('managefees')  
    success_message = "Fees added successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all() 
        return context

class FeesListView(ListView):
    model = FeesDb
    template_name = 'ManageFees.html'
    context_object_name = 'fees'

class FeesUpdateView(SuccessMessageMixin, UpdateView):
    model = FeesDb
    template_name = 'Feesedit.html' 
    fields = ['student', 'amount_paid', 'due_amount', 'payment_date', 'payment_method', 'fees_status']
    success_url = reverse_lazy('managefees')
    success_message = "Fees updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = StudentDb.objects.all()  
        return context

class FeesDeleteView(SuccessMessageMixin, DeleteView):
    model = FeesDb
    template_name = 'Officestaff/confirm_delete.html'  
    success_url = reverse_lazy('managefees')
    success_message = "Fees deleted successfully!"


