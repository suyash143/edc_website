from django.db import models


class LinkStorage(models.Model):
    date_time=models.DateTimeField(null=True,blank=True)
    link=models.URLField(null=True,blank=True,max_length=400)
    name = models.CharField(null=True,blank=True,max_length=400)
    key=models.CharField(unique=True,null=True,blank=True,max_length=400)
    converted_link=models.URLField(null=True,blank=True,max_length=400)
    count=models.IntegerField(null=True,blank=True,default=0)


class Event(models.Model):
    created=models.DateTimeField(null=True,blank=True)
    title=models.CharField(null=True,blank=True,max_length=300)
    short_description=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    registration_link=models.URLField(null=True,blank=True)
    last_date=models.DateField(null=True,blank=True)
    cover_image=models.ImageField(upload_to='event',null=True,blank=True)
    completed=models.BooleanField(blank=True,null=True)

    def __str__(self):
        return f'{self.title} {self.created}'


class Index(models.Model):
    heading_bold=models.TextField(null=True,blank=True)
    heading_sub=models.TextField(null=True,blank=True)
    about_us_1=models.TextField(null=True,blank=True)
    about_us_2=models.TextField(null=True,blank=True)
    event_heading = models.TextField(null=True, blank=True)
    vertical_heading = models.TextField(null=True, blank=True)
    testimonial_heading=models.TextField(null=True,blank=True)
    gallery_heading=models.TextField(null=True,blank=True)
    team_heading = models.TextField(null=True, blank=True)
    contact_heading=models.TextField(null=True,blank=True)
    contact_description=models.TextField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)


class Skill(models.Model):
    title=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    svg=models.TextField(null=True,blank=True)


class Vertical(models.Model):
    title=models.CharField(max_length=400,null=True,blank=True)
    image=models.ImageField(upload_to='vertical',null=True,blank=True)


class Testimonial(models.Model):
    title=models.CharField(null=True,blank=True,max_length=400)
    image=models.ImageField(upload_to='testimonial',null=True,blank=True)
    name=models.CharField(max_length=300,null=True,blank=True)
    post=models.CharField(max_length=300,null=True,blank=True)
    quote=models.TextField(null=True,blank=True)


class Gallery(models.Model):
    title = models.CharField(null=True, blank=True,max_length=400)
    year=models.IntegerField(null=True,blank=True)
    event=models.ForeignKey(Event,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)


class Team(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    title=models.CharField(null=True,blank=True,max_length=200)
    image=models.ImageField(upload_to='team',null=True,blank=True)
    facebook_url=models.URLField(null=True,blank=True)
    instagram_url=models.URLField(null=True,blank=True)
    linkedin_url=models.URLField(null=True,blank=True)
    number=models.PositiveIntegerField(null=True,blank=True)


class Contact(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    number=models.PositiveIntegerField(null=True,blank=True)
    subject=models.TextField(null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    created=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=300,null=True,blank=True)