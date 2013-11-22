from django.db import models
from django.contrib.auth.models import User
from django.db import DataError
import string
import random


class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'organizations'
        ordering = ['name']


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'keywords'
        ordering =['name']


class Author(models.Model):
    uid = models.CharField(max_length=16, unique=True, primary_key=True)
    user = models.ForeignKey(User)
    initial = models.CharField(max_length=10, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    #email = models.EmailField()
    country = models.CharField(max_length=50, null=False, blank=False)
    organization = models.ForeignKey(Organization)
    #paper = models.ManyToManyField(Paper, blank=True)

    def __unicode__(self):
        return "%s %s %s." % (self.initial, self.last_name, self.first_name[0])

    def id_generate(self, size=16, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def save(self, *args, **kwargs):
        tmp_author = Author.objects.filter(first_name=self.first_name, last_name=self.last_name)
        if not tmp_author:
            self.uid = self.id_generate()
            super(Author, self).save(*args, **kwargs)
        else:
            raise DataError

    class Meta:
        db_table = 'authors'
        ordering = ['last_name', 'first_name', 'country', 'organization']


class Paper(models.Model):
    id = models.CharField(max_length=16, unique=True, primary_key=True)
    title = models.CharField(max_length=500, null=False, blank=False)
    abstract = models.TextField(null=False, blank=False)
    keyword = models.ManyToManyField(Keyword)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.id

    def id_generate(self, size=16, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def save(self, *args, **kwargs):
        self.id = self.id_generate()
        super(Paper, self).save(*args, **kwargs)

    class Meta:
        db_table = 'papers'
        ordering = ['title']


