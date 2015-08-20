"""
This class overlays lines on top of the image stacks. 
Unlike the sparsepoints ingredient, multiple lines associated 
with the same ingredient will likely have to be different plot 
items. See: 
https://groups.google.com/forum/?fromgroups=#!topic/pyqtgraph/h0PNUV2ToKg
"""

from __future__ import division
import numpy as np
import os
import pyqtgraph as pg
from  lasagna_ingredient import lasagna_ingredient 
from PyQt4 import QtGui, QtCore
import lasagna_helperFunctions as lasHelp


class lines(lasagna_ingredient):
    def __init__(self, parent=None, data=None, fnameAbsPath='', enable=True, objectName=''):
        super(lines,self).__init__(parent, data, fnameAbsPath, enable, objectName,
                                        pgObject='PlotDataItem'
                                        )

        
        #Choose symbols from preferences file. TODO: in future could increment through so successive ingredients have different symbols and colors
        self.symbol = lasHelp.readPreference('symbolOrder')[0]
        self.pen = None
        self.symbolSize = lasHelp.readPreference('defaultSymbolSize')
        self.alpha = lasHelp.readPreference('defaultSymbolOpacity')
        self.color = lasHelp.readPreference('colorOrder')[0]
        

        #Add to the imageStackLayers_model which is associated with the points QTreeView
        name = QtGui.QStandardItem(objectName)
        name.setEditable(False)

        #Add checkbox
        thing = QtGui.QStandardItem()
        thing.setFlags(QtCore.Qt.ItemIsEnabled  | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsUserCheckable)
        thing.setCheckState(QtCore.Qt.Checked)

        #self.modelItems=(name,thing) #Remove this for now because I have NO CLUE how to get access to the checkbox state
        self.modelItems=name
        self.model = self.parent.points_Model


        self.addToList()


       
    def data(self,axisToPlot=0):
        """
        lines data are an n by 3 array where each row defines the location
        of a single point in x, y, and z
        """
        data = np.delete(self._data,axisToPlot,1)
        if axisToPlot==2:
            data = np.fliplr(data)

        return data

    def plotIngredient(self,pyqtObject,axisToPlot=0,sliceToPlot=0):
        """
        Plots the ingredient onto pyqtObject along axisAxisToPlot,
        onto the object with which it is associated
        """
        z = np.round(self._data[:,axisToPlot])

        data = self.data(axisToPlot)

        #Find points within this z-plane +/- a certain region
        zRange = self.parent.viewZ_spinBoxes[axisToPlot].value()-1
        fromLayer = sliceToPlot-zRange
        toLayer = sliceToPlot+zRange
        data = data[(z>=fromLayer) * (z<=toLayer),:]

        if self.pen == True:            
            pen = self.symbolBrush()
        else:
            pen = self.pen


        pyqtObject.setData(x=data[:,0], y=data[:,1], 
                        symbol=self.symbol, 
                        pen=pen, 
                        symbolSize=self.symbolSize, 
                        symbolBrush=self.symbolBrush()
                        )




    def addToList(self):
        """
        Add to list and then set UI elements
        """
        super(lines,self).addToList()
        self.parent.markerSize_spinBox.setValue(self.symbolSize)
        self.parent.markerAlpha_spinBox.setValue(self.alpha)
        if self.pen == None:
            self.parent.addLines_checkBox.setCheckState(False)
        else:
            self.parent.addLines_checkBox.setCheckState(True)
            

    def symbolBrush(self):
        if isinstance(self.color,str):
            return tuple(self.colorName2value(self.color, alpha=self.alpha))
        elif isinstance(self.color,list):
            return tuple(self.color + [self.alpha])
        else:
            print "lines.color can not cope with type " + type(self.color)


    #---------------------------------------------------------------
    #Getters and setters

    def get_symbolSize(self):
        return self._symbolSize
    def set_symbolSize(self,symbolSize):
        self._symbolSize = symbolSize
    symbolSize = property(get_symbolSize,set_symbolSize)


    def get_symbol(self):
        return self._symbol
    def set_symbol(self,symbol):
        self._symbol = symbol
    symbol = property(get_symbol,set_symbol)


    def get_color(self):
        return self._color
    def set_color(self,color):
        self._color = color
    color = property(get_color,set_color)


    def get_alpha(self):
        return self._alpha
    def set_alpha(self,alpha):
        self._alpha = alpha        
    alpha = property(get_alpha,set_alpha)


   