anycluster (POSTGIS version)
============================

anycluster provides Server-Side clustering of map markers for Geodjango. It is suitable for large amounts of markers. 
Depending on your server and personal feeling, it works very well with 200.000 to 500.000 markers.

The postgis version is recommended. There is a mysql version with limited functionality: https://github.com/biodiv/anycluster-mysql


ChangeLog
---------
- you now need to add {% csrf_token % } somewhere in your template


Features
--------

This application offers 2 methods of clustering:
- grid-based clustering
- clustering based on geometric density of the points (needs PSQL extension)
- get all elements contained in a cluster

... and has a builtin caching mechanism: if the user pans a map, only the new areas are processed.

And lots of optional customization possibilities:
- works with google maps and OpenLayers
- define what happens if you click on a cluster
- use your own cluster graphics
- define gridsize and other cluster parameters
- apply filters to your clusters
- use different markers if count is 1


Documentation
-------------

http://anycluster.readthedocs.org/en/latest/


Live Example
------------

There's a demo at https://www.anymals.org/nx/bigmap/.

Using the Demo
--------------

To use the demo, follow these steps: 

- install ``Django 1.6`` correctly
- copy the demo folder to your system and include the anycluster folder as a django app.
- modify the database connection in ``settings.py`` according to your setup
- remember to create the kmeans function as described above
- from within the demo folder, run ``python manage.py syncdb``
- from within the demo folder, run ``python manage.py filldemodb 50000`` to fill the database with 50000 points
- be patient, as this process is not very effective
- from within the demo folder, run ``python manage.py runserver 8080``
- open your browser and enter ``localhost:8080``


Performance Tips
----------------

- index your GIS database columns correctly
- usage of a SSD can be 10-20 times faster compared to HDD
