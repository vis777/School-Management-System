from django.urls import path
from . import views 

urlpatterns = [
    path('librarianpage/', views.LibrarianView.as_view(), name='librarianpage'), 
    path('librarian_login/', views.LibrarianLoginView.as_view(), name='librarian_login'),  
    path('librarian_logout/', views.LibrarianLogoutView.as_view(), name='librarian_logout'),  

    path('manage-students/', views.StudentListView.as_view(), name='managestudent'),

    path('book/add/', views.BookCreateView.as_view(), name='addbook'),
    path('manage-books/', views.BookListView.as_view(), name='managebooks'),
    path('books/edit/<int:pk>/', views.BookUpdateView.as_view(), name='editbook'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='deletebook'),

    path('manage-fees/', views.FeesListView.as_view(), name='managefee'),
]
