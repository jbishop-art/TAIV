

#In Python variables are mutable
#Mutability
var = 5

#id of element
print('int id', id( var))

var = str( var); 

#id of element
print(' str id', id( var));

#Transform & Shape nodes

import maya.cmds as mc

sp = mc.polySphere()
print sp

spShape = sp[1]
print spShape

#Capturing polySphere into a string variable
#Unlike Mel, backtics are not required
rad = mc.polySphere(spShape, q = True, radius = True ) 
print rad
#1.0
mc.polySphere(spShape, e = True, radius = rad* 2)

loc = mc.spaceLocator()[0];

sx = mc.getAttr(loc +'.scaleX') 
print(sx)

sx *= 2 #Double sx value
mc.setAttr(loc + '.scaleX', sx)

print mc.xform(loc, q=True, t=True )
#[0.0, 0.0, 0.0] List

mc.xform(loc, t= [0.0, 1.0, 0.0])
#[0.0, 1.0, 0.0] List

print (mc.getAttr(loc + '.translate'))
#[(0.0, 1.0, 0.0)] List contains Tuple

mc.setAttr(loc + '.translate', 1, 5, 3)
#set each value in order

sp = mc.polySphere()[0]
cb = mc.polyCube()[0]

#connectAttr and disconnectAttr commands
mc.connectAttr(sp + '.ry', cb + '.tx')
#sphere drives cube

mc.disconnectAttr(sp + '.ry', cb + '.tx')
#sphere drives cube

#Creating Multiply Divide Nodes
mult = mc.createNode('multiplyDivide')

mc.connectAttr(sp + '.rx', mult + '.input1X')
mc.setAttr(mult + '.input2X', 1.0/10.0)
mc.connectAttr(mult + '.outputX', cb + '.tx')

mc.connectAttr(sp + '.ry', mult + '.input1Y')
mc.setAttr(mult + '.input2Y', 1.0/10.0)
mc.connectAttr(mult + '.outputY', cb + '.ty')

mc.connectAttr(sp + '.rz', mult + '.input1Z')
mc.setAttr(mult + '.input2Z', 1.0/10.0)
mc.connectAttr(mult + '.outputZ', cb + '.tz')

mc.select(mult)
mc.delete(mult)

mc.setAttr(sp + '.rotate', 0, 0, 0) 
mc.setAttr(sp + '.translate', 0, 0, 0)

mc.setAttr(cb + '.rotate', 0, 0, 0) 
mc.setAttr(cb + '.translate', 2, 0, 2)

thing = 512987
print(type(thing))
#<type 'int'>

#Format Strings
cube = 6 
pi = 3.141592654 
print('There are '+ str(cube)+' sides to a cube, and about '+ str( 2* pi) +' radians in a circle.')

cube = 6
pi = 3.141592654 
print('There are %s sides to a cube, and about %.3f radians in a circle'%(cube,2*pi)) 
# %.3f = 3 decimal points

# String Format Patterns

# f Floating point 
# s String Same as using str() function with object

import maya.cmds as mc

#create cubes
for i in range(0, 5):
    mc.polyCube()
    
mc.select('pCube1', 'pCube2', 'pCube3', 'pCube4', 'pCube5')
cubes = mc.ls(sl = True)

print type(cubes)
print cubes

#move cubes
for i in range(len(cubes)):
    mc.move(0, (i *2), cubes[i])
    
#parent cubes
for i in range(1, len(cubes)):
    mc.parent(cubes[i], cubes[i-1])



    
    












