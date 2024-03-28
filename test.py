from osgeo import gdal
from osgeo import ogr
from osgeo import osr
from osgeo import gdal_array
from osgeo import gdalconst
# from QGIS.python.qgis.core import QgsProcessing

import subprocess

command = "gdal_rasterize -l new_layer -a id -ts 1.0 1.0 -a_nodata 0.0 -ot Float32 -of GTiff D:/CodingProject/customed-pyqgis/QGIS/data/new_layer.shp D:/CodingProject/customed-pyqgis/QGIS/data/test3.tif"
subprocess.call(command, shell=True)

processing.run("native:mergevectorlayers", {'LAYERS':['D:/CodingProject/customed-pyqgis/QGIS/data/new_layer.shp'],'CRS':QgsCoordinateReferenceSystem('EPSG:4326'),'OUTPUT':'D:/CodingProject/customed-pyqgis/QGIS/data/2.shp'})

qgis_process run native:mergevectorlayers --distance_units=meters --area_units=m2 --ellipsoid=EPSG:7030 --LAYERS='D:/CodingProject/customed-pyqgis/QGIS/data/new_layer.shp' --CRS='EPSG:4326' --OUTPUT='D:/CodingProject/customed-pyqgis/QGIS/data/2.shp'
{
  "area_units": "m2",
  "distance_units": "meters",
  "ellipsoid": "EPSG:7030",
  "inputs": {
    "CRS": "EPSG:4326",
    "LAYERS": [
      "D:/CodingProject/customed-pyqgis/QGIS/data/new_layer.shp"
    ],
    "OUTPUT": "D:/CodingProject/customed-pyqgis/QGIS/data/2.shp"
  }
}

def gdal_rasterize(parameters):
    parameters={
        "input_layer":"new_layer2",
    }
    string=""
    string+=parameters.get("input_layer")
    
    return "gdal_rasterize -l new_layer -a id -ts 1.0 1.0 -a_nodata 0.0 -ot Float32 -of GTiff D:/CodingProject/customed-pyqgis/QGIS/data/new_layer.shp C:/Users/PC/AppData/Local/Temp/processing_cvAyTW/11b25f9cd3d44fdf958064aae4f8410c/OUTPUT.tif"