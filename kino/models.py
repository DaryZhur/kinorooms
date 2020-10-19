# from django.db import models
#
#
# # Create your models here.
# class Actor(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()
#
#     def __unicode__(self):
#         return self.name
#
#
# class Film(models.Model):
#     title = models.CharField(max_length=100)
#     actors = models.ManyToManyField(Actor)
#     publication_date = models.DateField()
#
#     def __unicode__(self):
#         return self.title
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     films = models.ManyToOneRel(Film)
#     website = models.URLField()
#
#     def __unicode__(self):
#         return self.name
