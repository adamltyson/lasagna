"""
load an overlay image stack that will be placed on top of the base stack to
create a red/green overlay. If an overlay is added the base stack changes 
color (e.g. to red). 
"""

from PyQt4 import QtGui
import os
from lasagna_plugin import lasagna_plugin

class loadOverlayImageStack(lasagna_plugin):
    def __init__(self,lasagna):
        super(loadOverlayImageStack,self).__init__(lasagna)

        self.lasagna = lasagna
        self.objectName = 'load_overlay' #Can be uased as an optional way of finding the object later


        #Construct the QActions and other stuff required to integrate the load dialog into the menu
        
        # - - - - - - - - - - - - - - - - - - - - 
        #1. The menu action
        
        self.loadAction = QtGui.QAction(self.lasagna) #Instantiate the menu action

        #TODO: Test of a base stack exists and if so enable. This isn't too important. It'll
        #probably only be problem if the user loads a base image from the command line
        self.loadAction.setEnabled(False)  

        #Add an icon to the action
        iconLoadOverlay = QtGui.QIcon()
        iconLoadOverlay.addPixmap(QtGui.QPixmap(":/actions/icons/overlay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadAction.setIcon(iconLoadOverlay)

        #Insert the action into the menu
        self.loadAction.setObjectName("loadOverlayImageStack")
        self.lasagna.menuLoad_ingredient.addAction(self.loadAction)
        self.loadAction.setText("Load overlay stack")

        self.loadAction.triggered.connect(self.showLoadDialog) #Link the action to the slot


        # - - - - - - - - - - - - - - - - - - - - 
        #2. The toolbar action
        self.actionRemoveOverlay = QtGui.QAction(self.lasagna) #Instantiate the menu action
        self.actionRemoveOverlay.setEnabled(False) 

        #Add an icon to the action
        iconRemoveOverlay = QtGui.QIcon()
        iconRemoveOverlay.addPixmap(QtGui.QPixmap(":/actions/icons/removeoverlay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveOverlay.setIcon(iconRemoveOverlay)

        #Insert the action into the menu
        self.actionRemoveOverlay.setObjectName("actionRemoveOverlay")
        self.lasagna.toolBar.addAction(self.actionRemoveOverlay)  
        self.actionRemoveOverlay.setToolTip("Remove overlay")

        self.actionRemoveOverlay.triggered.connect(self.removeOverlay) #Link the action to the slot


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    #main load method
    def load(self,fnameToLoad):
        """
        The load method does all of the things necessary for loading the overlay
        and displaying it correctly
        """

        #Get the existing base image stack so we can ensure that our overlay is the same size
        baseStack = self.lasagna.returnIngredientByName('baseImage') 

        if  baseStack == False:
            self.lasgna.actionLoadOverlay.setEnabled(False) #TODO: will need to be changed as we detach this from core application
            return

        #Use method from lasagna to load imagestack
        loadedImageStack = self.lasagna.loadImageStack(fnameToLoad) 

        #Do not proceed with adding overlay if it's of a different size
        existingSize = baseStack.data().shape
        overlaySize = loadedImageStack.shape

        #Ensure that overlay is the same size as the base image stack
        if not existingSize == overlaySize:
            msg = '*** Overlay is not the same size as the loaded image ***'
            print msg
            self.lasagna.statusBar.showMessage(msg)

            print "Base image:"
            print existingSize
            print "Overlay image:"
            print overlaySize

            from alert import alert
            self.lasagna.alert = alert(self.lasagna,alertText="This stack is a different size to the loaded base stack.<br>Aborting load. ")
            return


        #TODO: this is mostly duplicated code from loadBaseImageStack. Maybe this can be reduced somewhat?
        objName='overlayImage'
        self.lasagna.addIngredient(objectName=objName       , 
                                   kind='imagestack'        , 
                                   data=loadedImageStack    , 
                                   fname=fnameToLoad)

        #set colormaps for the two stacks
        self.lasagna.returnIngredientByName('baseImage').lut='red'
        self.lasagna.returnIngredientByName('overlayImage').lut='green'
        
        #Add plot items to axes so that they become available for plotting
        [axis.addItemToPlotWidget(self.lasagna.returnIngredientByName(objName)) for axis in self.lasagna.axes2D]

        #TODO: Both of the following lines need to be changed. They call hard-coded stuff in lasagna.py 
        #and doing this is no longer an option
        self.overlayEnableActions()


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    #Plugin hooks to modify the behavior of the main GUI. Specifically, want to only allow overlays
    #to be loaded when a base stack is already present.
    def hook_loadBaseImageStack_End(self):
        self.overlayEnableActions()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    #Slots follow
    def showLoadDialog(self):
        """
        This slot brings up the load dialog and retrieves the file name.
        If the file name is valid, it loads the base stack using the load method.
        We split things up to make it easier to load the base stack pragmatically,
        such as from a plugin, without going via the load dialog. 
        """
        print "IN SLOT"
        fname = self.lasagna.showFileLoadDialog()
        if fname == None:
            return

        if os.path.isfile(fname): 
            self.load(str(fname)) 
            self.lasagna.initialiseAxes()
        else:
            self.lasagna.statusBar.showMessage("Unable to find " + str(fname))


    def removeOverlay(self):
        """
        Remove overlay from an imageStack        
        """
        objectName = 'overlayImage'
        print "removing " + objectName

        #Remove item from axes
        [axis.removeItemFromPlotWidget(objectName) for axis in self.lasagna.axes2D]

        self.lasagna.removeIngredientByName(objectName)

        #Set baseImage to gray-scale once more
        self.lasagna.returnIngredientByName('baseImage').lut='gray'

        self.lasagna.initialiseAxes()
        self.actionRemoveOverlay.setEnabled(False) #Disable the button once the overlay has been removed

        self.lasagna.updateDisplayText()


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    #The following methods define modifications to the GUI that need to take place when it becomes
    #possible to overlay an image stack.
    def overlayEnableActions(self):
        """
        Actions that need to be performed on the GUI when an overlay can be added
        """
        self.loadAction.setEnabled(True)
        self.actionRemoveOverlay.setEnabled(True)


    def overlayDisableActions(self):
        """
        Actions that need to be performed on the GUI when an overlay can not be added
        """
        #self.actionRemoveOverlay.setEnabled(False)