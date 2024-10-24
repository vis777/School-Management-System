from Backend import views
from django.urls import path
from . import views 

urlpatterns = [
    path('adminpage/', views.AdminPageView.as_view(), name='adminpage'),
    path('admin_login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('admin_logout/', views.AdminLogoutView.as_view(), name='admin_logout'),

    path('officestaff/add/', views.OfficeStaffCreateView.as_view(), name='add_officestaff'),
    path('officestaff/manage/', views.OfficeStaffListView.as_view(), name='manage_officestaff'),
    path('officestaff/edit/<int:pk>/', views.OfficeStaffUpdateView.as_view(), name='edit_officestaff'),
    path('officestaff/delete/<int:pk>/', views.OfficeStaffDeleteView.as_view(), name='delete_officestaff'),
    path('officestaff/update/<int:pk>/', views.OfficeStaffUpdateView.as_view(), name='updateofficestaff'),

    path('librarian/add/', views.LibrarianCreateView.as_view(), name='add_librarian'),
    path('librarian/manage/', views.LibrarianListView.as_view(), name='manage_librarian'),
    path('librarian/edit/<int:pk>/', views.LibrarianUpdateView.as_view(), name='edit_librarian'),
    path('librarian/delete/<int:pk>/', views.LibrarianDeleteView.as_view(), name='delete_librarian'),
    path('librarian/update/<int:pk>/', views.LibrarianUpdateView.as_view(), name='updatelibrarian'),

    path('student/add/', views.StudentCreateView.as_view(), name='add_student'),
    path('student/manage/', views.StudentListView.as_view(), name='manage_student'),
    path('student/edit/<int:pk>/', views.StudentUpdateView.as_view(), name='edit_student'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='updatestudent'),

    path('book/add/', views.BookCreateView.as_view(), name='add_book'),
    path('books/manage/', views.BookListView.as_view(), name='manage_books'),
    path('books/edit/<int:pk>/', views.BookUpdateView.as_view(), name='edit_book'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),

    path('fee/add/', views.FeesCreateView.as_view(), name='add_fee'),
    path('fees/manage/', views.FeesListView.as_view(), name='manage_fees'),
    path('fees/edit/<int:pk>/', views.FeesUpdateView.as_view(), name='edit_fee'),
    path('fees/delete/<int:pk>/', views.FeesDeleteView.as_view(), name='delete_fee'),

]
