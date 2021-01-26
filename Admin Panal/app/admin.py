from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from django.contrib import admin
from .models import Customer, Product, RAWM, Supplier, Department, Employee, Order, OrderProduct, OrderRAWM

admin.site.site_header = 'Global Solution Package Admin'


class OrderAdmin(admin.ModelAdmin):
    def complete(self, request, queryset):
        queryset.update(status='Complete')

    def pending(self, request, queryset):
        queryset.update(status='Pending')

    complete.short_description = "Mark selected Orders are Complete"
    pending.short_description = "Mark selected Customers are Pending"
    list_display = ('customer', 'buy_date', 'price', 'status')
    list_filter = ('buy_date', 'status')
    actions = [complete, pending]


class CustomerAdmin(admin.ModelAdmin):
    def make_loyalty(self, request, queryset):
        queryset.update(status='Verified Loyalty')

    def not_good(self, request, queryset):
        queryset.update(status='Bad Transaction')

    def normal(self, request, queryset):
        queryset.update(status='Normal')

    make_loyalty.short_description = "Mark selected Customers are Verified Loyalty"
    normal.short_description = "Mark selected Customers are Normal"
    not_good.short_description = "Mark selected Customers are Bad For Transaction"
    list_display = ('first_Name', 'last_Name', 'contact', 'email', 'out_standing', 'status')
    list_filter = ('status',)
    actions = [make_loyalty, not_good, normal]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'location')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'gusset', 'width', 'gauge', 'wast', 'unit_price', 'raw_for_unit')


class RAWMAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'quantity')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_Name', 'last_Name', 'email', 'contact_Number', 'nic', 'gender', 'bank_Account_Number',
                    'hire_Date', 'DOB', 'department_Name')
    list_filter = ('department_Name',)


class SupplierAdmin(admin.ModelAdmin):
    def Amount_paid(self, request, queryset):
        queryset.update(to_pay=0.00)

    list_display = ('first_name', 'contact', 'email', 'address', 'ACCN', 'to_pay')


class OrderProductadmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')


class OrderRAWMadmin(admin.ModelAdmin):
    def Order_pending(self, request, queryset):
        queryset.update(status='Order Pending')

    def Order_received(self, request, queryset):
        queryset.update(status='Order Received')

    Order_pending.short_description = 'Mark selected Orders are Pending'
    Order_received.short_description = 'Mark selected Orders are Received'
    list_display = ('supplier_id', 'price', 'quantity', 'orderrawm_date', 'status')
    list_filter = ('status', 'orderrawm_date')
    actions = [Order_pending, Order_received, ]


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RAWM, RAWMAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductadmin)
admin.site.register(OrderRAWM, OrderRAWMadmin)

# admin.site.register(ProductOrder)

# customize
