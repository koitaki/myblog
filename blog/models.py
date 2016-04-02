from django.db import models
from django.utils.timezone import now

# Create your models here.


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return now()


class Category(models.Model):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200, default='Post Title', help_text='200 characters max')
    slug = models.SlugField(default='', blank=True, max_length=128)
    author = models.CharField(max_length=50, default='admin', null=False, help_text='50 characters max.')
    # author = models.ForeignKey(User)
    post = models.TextField(default='Post', null=False)
    created = models.DateTimeField(default=now)
    updated = AutoDateTimeField(default=now)
    pub_date = models.DateTimeField(verbose_name='Published on', default=now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50, default='Guest', null=False, help_text='50 characters max.')
    post = models.ForeignKey(Post)
    text = models.TextField(default='Comment', null=False)
    created = models.DateTimeField(default=now)

    def __str__(self):
        return '{} {}'.format(self.post, self.text)

