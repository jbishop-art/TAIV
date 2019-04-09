#Import maya.cmds and abrevaite them to "mc".
import maya.cmds as mc
#Import math
from math import pow,sqrt

#declare global var
jtList = []
jtChainFK = []
swithIKFK = False

#make list based upon selection
jtList = mc.ls(selection=True) 
 
def createHandles():
    x = 0
    while x < len(jtList):
        #create a nurbs circle          
        mc.circle( nr=(0, 0, 1), c=(0, 0, 0) )
        #Rename them as controllers 
        mc.rename( mc.ls (selection = True), jtList[x] + "_Ctl_FK")
        
        x += 1
        
def resizeHandles():
    #resize the handles
    
    #find magnitude between the first and second joint to drive size.
    x = 0
        
    obj1 = mc.xform(jtList[x], q=True, t=True, ws=True)
    obj2 = mc.xform(jtList[x+1], q=True, t=True, ws=True)
    mag = sqrt(pow(obj1[0]-obj2[0],2)+pow(obj1[1]-obj2[1],2)+pow(obj1[2]-obj2[2],2))
    
    while x < len(jtList):
        mc.scale(mag * 0.25,mag * 0.25, mag * 0.25, jtList[x] + "_Ctl_FK")
        
        x += 1            
        
def moveHandles():
    x = 0
    while x < len(jtList):
        #move via parentConstraint then delete constraint
        mc.parentConstraint( jtList[x], jtList[x] + "_Ctl_FK")
        mc.delete(jtList[x] + "_Ctl_FK" + "_parentConstraint1")
        
        #delete history and freeze transforms
        mc.delete(jtList[x] + "_Ctl_FK", ch = True)
        mc.makeIdentity(jtList[x] + "_Ctl_FK", apply=True, t=1, r=1, s=1, n=0)
        
        #parent the joint to the handle
        mc.parentConstraint(jtList[x] + "_Ctl_FK", jtList[x], mo = True, w = 1, st=["x", "y", "z"])
          
        x += 1 
    #parent the handles to each other in the corect order.
    y = len(jtList)
    y -= 1   
    while y > 0:
        mc.parent(jtList[y] + "_Ctl_FK", jtList[y-1] + "_Ctl_FK")
        y -= 1
        
def renameJointChain():
    #select the Joint Chain for the leg
    mc.select(jtList[0], hi = True)
    
    #creat List contating selection
    tempList = mc.ls(selection=True)
    print tempList
                
    #makes list for FK Joint Chain Constraints.
    fkJointChainContraints = [s for s in tempList if "Constraint1" in s]
    
    #deslect the constraints
    x = 0
    while x < len(fkJointChainContraints):
        mc.select(fkJointChainContraints[x], d = True)
        x += 1
        
    #Make list of just the FK Joint Chain
    jtChainFK = mc.ls(selection=True)
    
    #rename the joints to Joint[x]_FK
    x = 0
    while x < len(jtChainFK):
        mc.select(jtChainFK[x])
        mc.rename( mc.ls (selection = True), "Joint_" + str(x+1) + "_FK")
        x += 1
    
def renameFKContraints():
    #select the Joint Chain for the leg
    mc.select("Joint_1_FK", hi = True)
    
    #creat List contating selection
    tempList = mc.ls(selection=True)
                
    #makes list for FK Joint Chain Constraints.
    fkJointChainContraints = [s for s in tempList if "Constraint1" in s]
    
    #rename the fkContraints
    x = 0
    y = len(fkJointChainContraints)
    while x < len(fkJointChainContraints):
        mc.select(fkJointChainContraints[x])
        mc.rename( mc.ls (selection = True), "Joint_" + str(y) + "_FK_Constraint")
        x += 1
        y -= 1  
        
def dupeJointChain():
    #select the Joint Chain for the leg
    mc.select("Joint_1_FK", hi = True)
    
    #creat List contating selection
    tempList = mc.ls(selection=True)
                
    #makes list for FK Joint Chain Constraints.
    fkJointChainContraints = [s for s in tempList if "Constraint" in s]
    
    #deslect the constraints
    x = 0
    while x < len(fkJointChainContraints):
        mc.select(fkJointChainContraints[x], d = True)
        x += 1
        
    #Make list of just the FK Joint Chain
    jtChainFK = mc.ls(selection=True)
    
    #dupe the chain
    mc.duplicate()
    
    #cleanup the dupe
    #select the dupe hi
    mc.select("Joint_1_FK1", hi = True)                          
    #creat List contating selection
    tempList = mc.ls(selection=True)
    
    #makes list for FK Joint Chain Constraints.
    dupeJointChainContraints = [s for s in tempList if "Constraint" in s]
    
    x = 0 
    while x < len(dupeJointChainContraints):
        mc.select(dupeJointChainContraints[x])
        mc.delete()
        x += 1

    #select the dupe hi
    mc.select("Joint_1_FK1", hi = True)                          
    #creat List contating selection
    tempList = []
    tempList = mc.ls(selection=True)
    print tempList
    print len(tempList)
    
    #rename dupe joint chaint to Joint_[x]_Orig
    x = len(tempList)
    print x
    while x > 0:
        mc.select(tempList[x-1])
        mc.rename(mc.ls (selection = True), "Joint_" + str(x) + "_Orig")
        x -= 1

    #dupe the Orig joint chain
    mc.select("Joint_1_Orig", hi = True)
    mc.duplicate()
                           
    #creat List contating selection
    tempList = []
    tempList = mc.ls(selection=True)
    print tempList
    print len(tempList)
    
    #rename dupe joint chaint to Joint_[x]_IK
    x = len(tempList)
    print x
    while x > 0:
        mc.select(tempList[x-1])
        mc.rename(mc.ls (selection = True), "Joint_" + str(x) + "_IK")
        x -= 1
        
def clearDupeHis():   
    mc.select("Joint_1_Orig", hi = True)
    mc.delete(ch = True)
    
    mc.select("Joint_1_IK", hi = True) 
    mc.delete(ch = True)    
        
def groupTogether():
    mc.select("Joint_1_Orig")
    mc.group(mc.ls (selection = True), n = "Original Joint Chain")
    
    mc.select("Joint_1_FK", "joint1_Ctl_FK")
    mc.group(mc.ls (selection = True), n = "FK Joint Chain")
            
    mc.select("Joint_1_IK")
    mc.group(mc.ls (selection = True), n = "IK Joint Chain")
    
def createIK():          
    mc.circle( nr=(0, 0, 1), c=(0, 0, 0) )
    #Rename them as controllers 
    mc.rename( mc.ls (selection = True), "Leg_Ctl_IK")
     
    #resize the handles
    #find magnitude between the first and second joint to drive size.
    obj1 = mc.xform("Joint_1_IK", q=True, t=True, ws=True)
    obj2 = mc.xform("Joint_2_IK", q=True, t=True, ws=True)
    mag = sqrt(pow(obj1[0]-obj2[0],2)+pow(obj1[1]-obj2[1],2)+pow(obj1[2]-obj2[2],2))
    mc.scale(mag * 0.75,mag * 0.75, mag * 0.75, "Leg_Ctl_IK")
    
    #move via parentConstraint then delete constraint
    mc.parentConstraint( "Joint_4_IK", "Leg_Ctl_IK")
    mc.delete("Leg_Ctl_IK" + "_parentConstraint1")
    
    mc.rotate(0, 0, "90deg", r = True)  #####shit is borked yo####
      
    #delete history and freeze transforms
    mc.delete("Leg_Ctl_IK", ch = True)
    mc.makeIdentity("Leg_Ctl_IK", apply=True, t=1, r=1, s=1, n=0)
    
    #create ikHandle
    mc.ikHandle(sj = "Joint_1_IK", ee = "Joint_3_IK")
    #rename the ikHandle to the "Leg_ikHandle"
    mc.rename("ikHandle1", "Leg_ikHandle")
    
    #parent contraint the ikHandle to the ikControler
    mc.parentConstraint("Leg_Ctl_IK", "Leg_ikHandle", mo = True, w = 1)
    
    
def groupIK():
    mc.select("Leg_ikHandle", "Leg_Ctl_IK")
    mc.parent(mc.ls (selection = True), "IK_Joint_Chain")
    
def fixRot():  #to fix issue above.
    mc.select("Joint_4_IK")
    mc.rotate(0, "-90deg", 0, r=True)
    
    mc.select("Joint_4_Orig")
    mc.rotate(0, "-90deg", 0, r=True)
    
def creatIKFKSwitch():   
    mc.circle( nr=(0, 0, 1), c=(0, 0, 0) )
    #rename the switch
    mc.rename(mc.ls (selection = True), "Leg_IKFK_Switch")
    
    #move the switch
    mc.parentConstraint( "Joint_4_Orig", "Leg_IKFK_Switch")
    mc.delete("Leg_IKFK_Switch" + "_parentConstraint1")
    mc.move(0, 0, -5, r=True)
    
    mc.xform(r = True, ro = (0, 90, 0)) 
        
    #delete history and freeze transforms
    mc.delete("Leg_IKFK_Switch", ch = True)
    mc.makeIdentity("Leg_IKFK_Switch", apply=True, t=1, r=1, s=1, n=0)
    
    
    #create additional attr boolean for IKFK switch
    mc.addAttr("Leg_IKFK_Switch", ln = "IKFK_Switch", keyable=True, attributeType='float', min=0.0, max=1.0)
    
    mc.select("Leg_IKFK_Switch")
    mc.parent(mc.ls (selection = True), "Original_Joint_Chain")

def setColors():
    mc.select("Original_Joint_Chain", hi = True) 
    mc.color(mc.ls (selection = True), rgb=(0,1,1))   
    
    mc.select("FK_Joint_Chain", hi = True)
    mc.color(mc.ls (selection = True), rgb=(1,0,1))  
    
    mc.select("IK_Joint_Chain", hi = True)
    mc.color(mc.ls (selection = True), rgb=(1,0,0))   
       
           
        
'''
*********************************************************************
RUN DEFINITIONS
*********************************************************************
'''        
        
#run definitions       
createHandles()
resizeHandles()
moveHandles()
renameJointChain()
renameFKContraints()
dupeJointChain()
clearDupeHis()
groupTogether()
createIK()
fixRot() 
groupIK()
creatIKFKSwitch()
setColors()

          