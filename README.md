# Lasagna - Python Volume Visualiser for 3-D data. #

## Concept ##
Lasagna is a lightweight platform for visualising for 3D volume data. Lasagna features
a flexible plugin system, allowing it to be easily extended using Python and PyQt. 
Visualisation is peformed via three linked 2D views. Lasagna was written to explore 
registration accuracy of 3D data, guide registration, and overlay point data onto images. 
It was also written to help explore the Allen Reference Atlas. Lasagna is under heavy 
development but is maturing rapidly. For more information see 
the [website](http://raacampbell13.github.io/lasagna).


## Installation ##
Lasagna runs on Python 2.7, PyQt4, and uses PyQtGraph for the plotting. You'll need the following modules:
* tifffile [for importing LSM files]
* vtk [optional, for faster import of MHD files]
* PyLibTiff
* numpy
* pyqtgraph 9.10
* yaml
* PyQt4
* SIP
