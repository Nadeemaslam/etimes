from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.core.files.storage import FileSystemStorage

from django.db import models
from ckeditor.fields import RichTextField

fs = FileSystemStorage(location='/tmp')
blogimage  =  FileSystemStorage(location='/tmp')
CHOICES = (
        ('nse_dividend', 'Nse Dividend Report'),
        ('nse_gold', 'Nse Gold Report'),
        ('nse_penny', 'Nse Penny Report'),
        ('nse_resources', 'Nse Resources Report'),
        ('nse_health', 'Nse Health Care Report'),
        ('nse_platinum', 'Nse Platinum Report'),
        ('nse_technical', 'NseTechnical Analysis'),
        ('nse_american', 'Nse American Tech Report'),
        ('nse_ipo', 'Nse IPO Report'),
        ('bse_dividend', 'Bse Dividend Report'),
        ('bse_gold', 'Bse Gold Report'),
        ('bse_penny', 'Bse Penny Report'),
        ('bse_resources', 'Bse Resources Report'),
        ('bse_health', 'Bse Health Care Report'),
        ('bse_platinum', 'Bse Platinum Report'),
        ('bse_technical', 'BseTechnical Analysis'),
        ('bse_american', 'Bse American Tech Report'),
        ('bse_ipo', 'Bse IPO Report'),
        ('nyse_dividend', 'NYse Dividend Report'),
        ('nyse_gold', 'NYse Gold Report'),
        ('nyse_penny', 'NYse Penny Report'),
        ('nyse_resources', 'NYse Resources Report'),
        ('nyse_health', 'NYse Health Care Report'),
        ('nyse_platinum', 'NYse Platinum Report'),
        ('nyse_technical', 'NYseTechnical Analysis'),
        ('nyse_american', 'NYse American Tech Report'),
        ('nyse_ipo', 'NYse IPO Report'),
        ('nasdaq_dividend', 'Nasdaq Dividend Report'),
        ('nasdaq_gold', 'Nasdaq Gold Report'),
        ('nasdaq_penny', 'Nasdaq Penny Report'),
        ('nasdaq_resources', 'Nasdaq Resources Report'),
        ('nasdaq_health', 'Nasdaq Health Care Report'),
        ('nasdaq_platinum', 'Nasdaq Platinum Report'),
        ('nasdaq_technical', 'Nasdaq Technical Analysis'),
        ('nasdaq_american', 'Nasdaq American Tech Report'),
        ('nasdaq_ipo', 'Nasdaq IPO Report'),
        ('tsx_dividend', 'Tsx Dividend Report'),
        ('tsx_gold', 'Tsx Gold Report'),
        ('tsx_penny', 'Tsx Penny Report'),
        ('tsx_resources', 'Tsx Resources Report'),
        ('tsx_health', 'Tsx Health Care Report'),
        ('tsx_platinum', 'Tsx Platinum Report'),
        ('tsx_technical', 'Tsx Technical Analysis'),
        ('tsx_american', 'Tsx American Tech Report'),
        ('tsx_ipo', 'Tsx IPO Report'),
    )

class report(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default=None, unique=True)
    exchange = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CHOICES, default=None, blank=True, null=True)
    file = models.FileField(storage=fs)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField()
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = models.FileField(default=None,null=True, storage=blogimage)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Tsx_losers(models.Model):
    symbol = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    change = models.CharField(max_length=200, blank=True)
    percent = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Tsx_gainers(models.Model):
    symbol = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    change = models.CharField(max_length=200, blank=True)
    percent = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Nyse_gainers(models.Model):
    symbol = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    change = models.CharField(max_length=200, blank=True)
    percent = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Nyse_losers(models.Model):
    symbol = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    change = models.CharField(max_length=200, blank=True)
    percent = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Nasdaq_gainers(models.Model):
    symbol = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    change = models.CharField(max_length=200, blank=True)
    percent = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Nasdaq_losers(models.Model):
    symbol = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    change = models.CharField(max_length=200, blank=True)
    percent = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


