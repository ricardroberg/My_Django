from django.db import models
from django.conf import settings
from stdimage.models import StdImageField

UserLogged = settings.AUTH_USER_MODEL

# Using uuid to allow 'unlimited' file names stored (for pictures and posts)
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Store who created what, when and when/who modified
class Base(models.Model):
    create_by = models.ForeignKey(UserLogged, default=1, null=True, on_delete=models.SET_NULL)
    create = models.DateField('Created', auto_now_add=True)
    last_modified = models.DateField('Last modified', auto_now=True)
    active = models.BooleanField('Active?', default=True)

# Still dont know that this is for
    class Meta:
        abstract = True

# Acquired knowledge that complement the software development
class Knowledge(Base):
    knowledge = models.CharField('Knowledge', max_length=50)
    description = models.TextField('Description', max_length=200)

# this is basicly a getter method
    def __str__(self):
        return self.knowledge

# What im want to and willing to learn
class Learning(Base):
    learning = models.CharField('Learning', max_length=50)
    description = models.TextField('Description', max_length=200)
    date_start = models.DateField('When start', default=None)

    def __str__(self):
        return self.learning


# Me, myself and Irene (Not actualy Irene, which i dont known, but any other user i will allow access
class User(Base):
    name = models.CharField('Name', max_length=100)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb':{'width': 480, 'height':480, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name
