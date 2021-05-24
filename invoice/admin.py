from django.contrib import admin

# Register your models here.


from .models import Product, Organisation, Order, OrderProduct, User, PdfUplaod


admin.site.register(Order)
admin.site.register(Organisation)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(User)
admin.site.register(PdfUplaod)

