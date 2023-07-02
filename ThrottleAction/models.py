from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from .helpers import *
from django.utils.timezone import now
from  django.urls import reverse

Vehicle_type= (('car','Car'),('bike','Bike'))
Bike_category= (('1','Bike'),('2','Gears'))
Status= (('active','Active'),('inactive','InActive'))

class Author(models.Model):
    Name = models.CharField(max_length=1000,blank=True)
    ProflePic = models.ImageField(null=True, blank=True, upload_to="Author/ProfilePic")
    position = models.CharField(max_length=5000,blank=True)
    description = models.CharField(max_length=50000,blank=True)
    def __str__(self):
        return self.Name

class Mailletter(models.Model):
    mail = models.EmailField(max_length=255,blank=True)

    def __str__(self):
        return self.mail
    

class Contact(models.Model):
    Name = models.CharField(max_length=255,blank=True)
    Mobile = models.CharField(max_length=255,blank=True)
    Email = models.EmailField(max_length=255,blank=True)
    Question = models.CharField(max_length=2555555555,blank=True, null=True)
    def __str__(self):
        return self.Name

class Bikes(models.Model):
    Name = models.CharField(max_length=255,blank=True)
    Category = models.CharField(choices=Bike_category,max_length=255)
    Company = models.CharField(max_length=255,blank=True)
    Hightlight_Topic_1 = models.CharField(max_length=255,blank=True)
    Hightlight_Answer_1 = models.CharField(max_length=255,blank=True)
    Hightlight_Topic_2 = models.CharField(max_length=255,blank=True)
    Hightlight_Answer_2 = models.CharField(max_length=255,blank=True)
    Hightlight_Topic_3 = models.CharField(max_length=255,blank=True)
    Hightlight_Answer_3 = models.CharField(max_length=255,blank=True)
    Hightlight_Topic_4 = models.CharField(max_length=255,blank=True)
    Hightlight_Answer_4 = models.CharField(max_length=255,blank=True)
    Hightlight_Topic_5 = models.CharField(max_length=255,blank=True)
    Hightlight_Answer_5 = models.CharField(max_length=255,blank=True)
    Hightlight_Topic_6 = models.CharField(max_length=255,blank=True)
    Hightlight_Answer_6 = models.CharField(max_length=255,blank=True)
    Good1 = models.CharField(max_length=255,blank=True)
    Good2 = models.CharField(max_length=255,blank=True)
    Good3 = models.CharField(max_length=255,blank=True)
    Good4 = models.CharField(max_length=255,blank=True)
    Good5 = models.CharField(max_length=255,blank=True)
    Good6 = models.CharField(max_length=255,blank=True)
    Bad1 = models.CharField(max_length=255,blank=True)
    Bad2 = models.CharField(max_length=255,blank=True)
    Bad3 = models.CharField(max_length=255,blank=True)
    Bad4 = models.CharField(max_length=255,blank=True)
    Bad5 = models.CharField(max_length=255,blank=True)
    Bad6 = models.CharField(max_length=255,blank=True)
    GA1 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_1 = models.CharField(max_length=255,blank=True)
    GA2 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_2 = models.CharField(max_length=255,blank=True)
    GA3 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_3 = models.CharField(max_length=255,blank=True)
    GA4 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_4 = models.CharField(max_length=255,blank=True)
    GA5 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_5 = models.CharField(max_length=255,blank=True)
    GA6 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_6 = models.CharField(max_length=255,blank=True)
    GA7 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_7 = models.CharField(max_length=255,blank=True)
    GA8 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_8 = models.CharField(max_length=255,blank=True)
    GA9 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_9 = models.CharField(max_length=255,blank=True)
    GA10 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_10 = models.CharField(max_length=255,blank=True)
    GA11 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_11 = models.CharField(max_length=255,blank=True)
    GA12 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_12 = models.CharField(max_length=255,blank=True)
    GA13 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_13 = models.CharField(max_length=255,blank=True)
    GA14 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_14 = models.CharField(max_length=255,blank=True)
    GA15 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_15 = models.CharField(max_length=255,blank=True)
    GA16 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_16 = models.CharField(max_length=255,blank=True)
    GA17 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_17 = models.CharField(max_length=255,blank=True)
    GA18 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_18 = models.CharField(max_length=255,blank=True)
    GA19 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_19 = models.CharField(max_length=255,blank=True)
    GA20 = models.ImageField(null=True, blank=True, upload_to="Gallery/Bike")
    Alt_20 = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.Name

class Reviews(models.Model):
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(max_length=255, unique=True,null=True,blank=True)
    Status_article = models.CharField(choices=Status,max_length=255)
    created_on = models.DateTimeField()
    Product = models.ForeignKey(Bikes,on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="Reviews/thumbnail")
    banner = models.ImageField(null=True, blank=True, upload_to="Reviews/Banner")
    SEO_description = RichTextField(blank=True,null= True)
    SEO_keywords = RichTextField(blank=True,null= True)
    likes =  models.ManyToManyField(User,related_name='reviews_post', blank=True,)
    content = RichTextField(blank=True,null= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("showreview", args={self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Reviews, self).save(*args, **kwargs)

class Exclusive(models.Model):
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(max_length=255, unique=True,null=True,blank=True)
    Status_article = models.CharField(choices=Status,max_length=255)
    created_on = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="Exclusive/thumbnail")
    banner = models.ImageField(null=True, blank=True, upload_to="Exclusive/Banner")
    SEO_description = RichTextField(blank=True,null= True)
    SEO_keywords = RichTextField(blank=True,null= True)
    likes =  models.ManyToManyField(User,related_name='exclusive_post', blank=True,)
    content = RichTextField(blank=True,null= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("showexclusive", args={self.pk})
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Exclusive, self).save(*args, **kwargs)


class reviewsComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user = models.CharField(max_length=20000,blank=True)
    post=models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user
    
class exclusiveComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user = models.CharField(max_length=20000,blank=True)
    emailid = models.EmailField(blank=True)
    post=models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user