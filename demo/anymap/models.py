from django.db import models
from django.contrib.gis.db import models

from django.utils.translation import ugettext_lazy as _

'''
    in this demo, the column "style" will be used as the pincolumn of anycluster

    the columns "rating","free_entrance" and "last_renewal" will be used to demonstrate filtering
'''

GARDEN_STYLES = (
    ('imperial', _('imperial')),
    ('japanese', _('japanese')),
    ('stone', _('stone')),
    ('flower', _('flower')),
    ('other', _('other')),
)

class Gardens(models.Model):
    connection_name="default"
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=20, choices=GARDEN_STYLES)
    rating = models.PositiveIntegerField()
    free_entrance = models.BooleanField(default=False)
    last_renewal = models.DateTimeField()
    coordinates = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return u'%s (%s)' % (self.name,self.style)
    
    
    
