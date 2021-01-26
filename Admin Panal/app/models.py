from datetime import datetime, time
from django.core.mail import send_mail
from django.db import models


#
# # Create your models here.
#

class Department(models.Model):
    """" Department """
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)

    def __str__(self):
        """" return representation of the model """
        return self.name


class Employee(models.Model):
    """" Employee model """
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    email = models.EmailField()
    contact_Number = models.CharField(max_length=10)
    nic = models.PositiveIntegerField()
    gender = models.CharField(max_length=1)
    bank_Account_Number = models.PositiveIntegerField()
    hire_Date = models.DateTimeField(auto_now_add=True)
    DOB = models.DateField()
    department_Name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        """" return representation of the model """
        return self.first_Name


STATUS_CHOICES = [
    ('v', 'Verified Loyalty'),
    ('b', 'Best for Loyalty'),
    ('n', 'Bad'),
]


class Customer(models.Model):
    """" Customer model """
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    contact = models.PositiveIntegerField()
    out_standing = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    email = models.EmailField(default='@email.com')
    status = models.CharField(default='Normal', max_length=20)

    def __str__(self):
        """" return representation of the model """
        return self.first_Name


class RAWM(models.Model):
    """ Raw material """
    name = models.CharField(max_length=10)
    color = models.CharField(default='white', max_length=10)
    quantity = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Details about Product """
    name = models.CharField(max_length=10)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    gusset = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    gauge = models.DecimalField(max_digits=10, decimal_places=2)
    wast = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    raw_for_unit = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    RAWM_id = models.ForeignKey(RAWM, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    buy_date = models.DateTimeField()
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    status = models.CharField(default='Pending', max_length=20)


class OrderProduct(models.Model):
    """" Order model """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Supplier(models.Model):
    """" Details about Order """
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    email = models.EmailField(default='@email.com')
    address = models.CharField(max_length=20)
    ACCN = models.PositiveIntegerField()
    to_pay = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        """" return representation of the model """
        return self.first_name


class OrderRAWM(models.Model):
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # raw_id = models.ForeignKey(RAWM, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    orderrawm_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='Order Pending', max_length=20)

    def __int__(self):
        return self.supplier_id
