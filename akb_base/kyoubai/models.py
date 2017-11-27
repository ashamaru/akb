from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    c_id = models.BigAutoField('Customer Id', primary_key=True)
    c_name = models.CharField(max_length=40)
    c_first_name = models.CharField(max_length=40)
    c_email = models.CharField(max_length=40)
    c_date_joined = models.DateTimeField()
    c_user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.c_id.value_to_string() + self.c_name


class Auction(models.Model):
    au_id = models.AutoField("Auction Id", primary_key=True)
    au_name = models.CharField(max_length=40)
    au_desc = models.TextField()
    au_start_dt = models.DateTimeField()
    au_end_dt = models.DateTimeField()

    def __str__(self):
        return self.au_id.value_to_string() + self.au_name

class Article(models.Model):
    a_id = models.BigAutoField('Article Id', primary_key=True)
    a_name = models.CharField(max_length=100)
    a_desc = models.TextField()
    a_min = models.DecimalField(max_digits=15, decimal_places=2)
    price_growth = models.DecimalField(max_digits=15, decimal_places=2)
    price_start = models.DecimalField(max_digits=15, decimal_places=2)
    a_time_start = models.DateTimeField()
    a_time_end = models.DateTimeField()
    a_state = models.CharField(max_length=100, default='used')
    a_picture_url = models.CharField(max_length=100, default='prototyp')
    a_auction_ref = models.ForeignKey(Auction)

    def __str__(self):
        return self.a_id.value_to_string() + self.pos_name

class Bid(models.Model):
    b_id = models.BigAutoField('Bid Id', primary_key=True)
    b_amount = models.DecimalField(max_digits=15, decimal_places=2)
    b_customer = models.ForeignKey(Customer)
    b_article = models.ForeignKey(Article)

    def __str__(self):
        return self.b_id.value_to_string()

class LimitBid(models.Model):
    lb_id = models.BigAutoField('Bid Id', primary_key=True)
    lb_amount = models.DecimalField(max_digits=15, decimal_places=2)
    lb_customer = models.ForeignKey(Customer)
    lb_article = models.ForeignKey(Article)

    def __str__(self):
        return self.lb_id.value_to_string()

class DelegateLock(models.Model):
    d_id = models.AutoField('DelegateLock Id', primary_key=True)
    d_lockval = models.IntegerField('Lock Value')

    def __str__(self):
        return self.d_id.value_to_string()


