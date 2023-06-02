from django.db import models

# Vendor model

class Vendor(models.Model):
    full_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='vendor/')
    address=models.TextField()
    mobile=models.CharField(max_length=15)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '1. Vendors'

    def __str__(self):
        return self.full_name

# Unit model
class Unit(models.Model):
    title=models.CharField(max_length=50)
    short_name=models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = '2. Units'

    def __str__(self):
        return self.title

# Product model
class Product(models.Model):
    title=models.CharField(max_length=50)
    detail=models.TextField()
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="product/")
    
    class Meta:
        verbose_name_plural = '3. Products'

    def __str__(self):
        return self.title

# Purchase model
class Purchase(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    qty=models.FloatField()
    price=models.FloatField()
    total_amount=models.FloatField()
    purchase_date=models.DateTimeField(auto_now_add=True)
        
    class Meta:
        verbose_name_plural = '4. Purchases'

    # def __str__(self):
    #     return self.product

# Sale model
class Sale(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.FloatField()
    price=models.FloatField()
    total_amount=models.FloatField()
    sale_date=models.DateTimeField(auto_now_add=True)
    customer_name=models.CharField(max_length=50,blank=True)
    customer_mobile=models.CharField(max_length=15, blank=False)
    customer_address=models.TextField()

    class Meta:
        verbose_name_plural = '5. Sales'

# Inventory model
class Inventory(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchase, on_delete=models.CASCADE, default=0)
    sale=models.ForeignKey(Sale, on_delete=models.CASCADE, default=0)
    purchase_qty=models.FloatField(default=0)
    sale_qty=models.FloatField(default=0)
    total_balance_qty=models.FloatField()

    class Meta:
        verbose_name_plural = '6. Inventory'
