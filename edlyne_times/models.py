from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.core.files.storage import FileSystemStorage

from django.db import models
fs = FileSystemStorage(location='/tmp')
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

    def __str__(self):
        return self.name