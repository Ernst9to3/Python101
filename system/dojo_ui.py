import maya.cmds as mc
import data.character_parts as character_parts
import json
import trArmRig as AR
# UI Class
class RDojo_UI:

    '''
    RDojo UI __Init__ function
    '''
    def __init__(self,*args):
        # Create UIElements dictionary in __init__ making it global
        self.UIElements={}
        # Define common window variables
        self.window="tr_rigginToolWindow"
        self.title="Rigging Tool"
        self.size=(110,100)


    def ui(self,*args):
        # Check to see if window exists
        if mc.window(self.window,exists=True):
            mc.deleteUI(self.window,window=True)
        # create window
        self.UIElements["window"]=mc.window(self.window,title=self.title,widthHeight=self.size,sizeable=False)
        buttonHeight=30
        buttonWidth=100
        # create default form layout
        self.UIElements["formLayout1"]=mc.formLayout(numberOfDivisions=100)
        self.UIElements["layout_Button"]=mc.button(label="Layout Button",width=buttonWidth,height=buttonHeight,parent=self.UIElements["formLayout1"],command=AR.createJoints)

        mc.formLayout(self.UIElements["formLayout1"],edit=True,
            attachForm=[(self.UIElements["layout_Button"],"bottom",5),(self.UIElements["layout_Button"],"left",5),(self.UIElements["layout_Button"],"right",5)],
            attachControl=[],
            attachPosition=[],
            attachNone=[(self.UIElements["layout_Button"],"top")],
            )
        # Show Window
        mc.showWindow(self.window)



