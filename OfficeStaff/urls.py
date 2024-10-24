from django.urls import path
from . import views 
urlpatterns = [
    path('officestaffpage/', views.OfficeStaffView.as_view(), name='officestaffpage'),
    path('officestaff_login/', views.OfficeStaffLoginView.as_view(), name='officestaff_login'),
    path('officestaff_logout/', views.OfficeStaffLogoutView.as_view(), name='officestaff_logout'),

    path('student/add/', views.StudentCreateView.as_view(), name='addstudent'),
    path('manage-students/', views.StudentListView.as_view(), name='managestudents'),
    path('student/edit/<int:pk>/', views.StudentUpdateView.as_view(), name='editstudent'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='deletestudent'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),


    path('manage-books/', views.BookListView.as_view(), name='managebook'),

    path('add-fee/', views.FeesCreateView.as_view(), name='addfee'),
    path('manage-fees/', views.FeesListView.as_view(), name='managefees'),
    path('edit-fee/<int:pk>/', views.FeesUpdateView.as_view(), name='editfee'),
    path('delete-fee/<int:pk>/', views.FeesDeleteView.as_view(), name='deletefee'), 
]