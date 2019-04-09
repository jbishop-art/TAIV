

#Transform & Shape nodes
import maya.cmds as mc

#create cubes


sp = mc.polySphere()
print sp
print type(sp)

spShape = sp[1]
print spShape
print type(spShape)

#Capturing polySphere into a string variable
#Unlike Mel, backtics are not required
rad = mc.polySphere(spShape, q = True, radius = True)
print rad

mc.polySphere(spShape, e = True, radius = rad* 2)
print rad

loc = mc.spaceLocator()[0];
print loc
print type(loc)

#Set locator scale x to 3.5
mc.setAttr(loc + '.scaleX', 3.5)

#Capture scale X
sx = mc.getAttr(loc + '.scaleX')
print(sx)
print type(sx)

sx *= 2 #Double sx value
mc.setAttr(loc + '.scaleY', sx)  #Scales in the Y axis
print(sx)

#move xyz, object, flags
mc.move(5, 10, 5, loc, r = True)

#xform object, flags
mc.xform(loc, t = (2, 4, 3))

mc.setAttr(loc + '.translate', 1, 5, 3)

sp = mc.polySphere()[0]
cb = mc.polyCube()[]
print(sp)
print type(sp)

#connectAttr command
mc.connectAttr(sp + '.ry', cb + '.tx') #sphere drives cube
#disconnectAttr command
mc.disconnectAttr(sp + '.ry', cb + '.tx')

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

mc.setAttr(sp + '.roate', 0, 0, 0)
mc.setAttr(sp + '.translate', 0, 0, 0)

mc.setAttr(cb + '.roate', 0, 0, 0)
mc.setAttr(cb + '.translate', 0, 0, 0)

thing = 512987
print (type(thing))
#<type 'int'>  vs <type 'long'>  depends on length of number.

#Format Strings
cube = 6
pi = 3.141592654
#Convert value of cube to string str(cube) with cataination.
print("There are " + str(cube) + " sides to a cube, and " + str(2 * pi) + "raidians in a .....")

#Pythonic Strings Format  ...mmm Pythonic, so sexy!
cube = 6
pi = 3.141592654
print("There are %s sides to a cube, and %.8f raidians in a circle"(cube, 2 * pi))
# %.8f = 8 decimal points

# d Signed integer
# i Signed integer Truncates decimal numbers
# e Scientific notation
# f Floating point
# g Mixed floating point.  Uses scentific notation if number is very small or very large.
# s String.  Same as using str() function with object.

#Query
locPos mc.xform(loc, q=True, t=True)
print(locPos)










