from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class OfficeStaffDb(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Post = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)    
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField(null=True, blank=True)
    UserNaMe = models.CharField(max_length=100, null=True, blank=True)
    PassWoRd = models.CharField(max_length=100, null=True, blank=True)

class LibrarianDb(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Post = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)    
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField(null=True, blank=True)
    UserNaMe = models.CharField(max_length=100, null=True, blank=True)
    PassWoRd = models.CharField(max_length=100, null=True, blank=True)
 
class StudentDb(models.Model):
    UserNaMe = models.CharField(max_length=100, null=True, blank=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Class_Name = models.CharField(max_length=50)    
    Email = models.CharField(max_length=100)
    DOB = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class BookDb(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]
    
    student = models.ForeignKey(StudentDb, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')  # Added status field
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.book_title

class FeesDb(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit', 'Credit'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Online Payment', 'Online Payment'),
    ]

    FEES_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Paid Partially', 'Paid Partially'),
    ]

    student = models.ForeignKey(StudentDb, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES) 
    fees_status = models.CharField(max_length=20, choices=FEES_STATUS_CHOICES)  

    def __str__(self):
        return f"Fees for {self.student}"
       
    
