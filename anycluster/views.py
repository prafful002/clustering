from django.http import HttpResponse
from django.shortcuts import render
from anycluster.MapClusterer import MapClusterer
from django.conf import settings
from django.db.models.loading import get_model
from django.contrib.gis.geos import GEOSGeometry
from anymap.models import Gardens
import json
from datetime import datetime,timedelta
import random
from anymap.models import Gardens, GARDEN_STYLES as G
#load the gis
geoapp, geomodel = settings.ANYCLUSTER_GEODJANGO_MODEL.split('.')
geo_column_str = settings.ANYCLUSTER_COORDINATES_COLUMN
Gis = get_model(geoapp, geomodel)
geo_table = Gis._meta.db_table


def getGrid(request, zoom, gridSize=256):

    clusterer = MapClusterer(zoom, gridSize)

    grid = clusterer.gridCluster(request)
    print 'getGrid'
    return HttpResponse(json.dumps(
        grid
        ), content_type="application/json")


def getPins(request, zoom, gridSize):
    print zoom,request
    clusterer = MapClusterer(zoom, gridSize)

    markers = clusterer.kmeansCluster(request)
    
   
    return HttpResponse(json.dumps(
        markers
        ), content_type="application/json")


def getClusterContent(request, zoom, gridSize):

    clusterer = MapClusterer(zoom, gridSize)

    entries = clusterer.getKmeansClusterContent(request)
    print 'getClusterContent'
    return render(request, 'anycluster/clusterPopup.html', {'entries':entries})



def loadAreaContent(request, zoom=1, gridSize=256):

    clusterer = MapClusterer(zoom, gridSize)

    params = clusterer.loadJson(request)

    filterstring = clusterer.constructFilterstring(params["filters"])

    geojson = params.get("geojson", None)

    geomfilterstring = clusterer.getGeomFilterstring(geojson)


    markers_qryset = Gis.objects.raw(
        '''SELECT * FROM "%s" WHERE %s %s;''' % (geo_table, geomfilterstring, filterstring)
    )
    
    print 'loadAreaContent'
    return markers_qryset
    

def getAreaContent(request, zoom, gridSize):

    markers = loadAreaContent(request, zoom, gridSize)
    print 'getAreaContent'
    return render(request, 'anycluster/clusterPopup.html', {'entries':markers})


def AddressEntry(request):

    
    json_str = request.body.decode(encoding='UTF-8')
    print json_str
    params = json.loads(json_str)
    print params['lat'],params['lng'],params['name']
    lon = params['lng']
    lat = params['lat']
    coords = GEOSGeometry('POINT(%f %f)' % (lon,lat))
    print coords
    rating = random.randint(1,5)
    free_entrance = random.randint(0,1)
            
    garden = Gardens (
               coordinates = coords,
               rating = rating,
               free_entrance = free_entrance,
               last_renewal = random_date(),
               style = random.choice(G)[0],
               name = params['name'],
               )

    garden.save()



    #Gis.objects.raw('''INSERT INTO "%s" VALUES();''' % (geo_table))
    return HttpResponse(json.dumps(
        ''
        ), content_type="application/json")

def random_date():
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    end = datetime.now()

    start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)
