import maya.cmds as cmds
import random as rnd

def choosenAngle(a):
   global angle
   angle = a

if 'myWin' in globals():
    if cmds.window(myWin, exists=True):
        cmds.deleteUI(myWin, window=True)
        
if 'nextBlockId' not in globals():
    nextBlockId = 1000
        
myWin = cmds.window(title="Lego Blocks", menuBar=True)

cmds.menu(label="Basic Options")
cmds.menuItem(label="New Scene", command=('cmds.file(new=True, force=True)'))
cmds.menuItem(label="Delete Selected", command=('cmds.delete()'))


#Basic Block
cmds.frameLayout(collapsable=True, label="Standard Block", width=475, height=140)
cmds.columnLayout()
cmds.intSliderGrp('blockHeight',l="Height", f=True, min=1, max=20, value=3)
cmds.intSliderGrp('blockWidth', l="Width (Bumps)", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('blockDepth', l="Depth (Bumps)", f=True, min=1, max=20, value=8)

cmds.colorSliderGrp('blockColour', label="Colour", hsv=(1, 1, 1))
cmds.button(label="Basic Block", command=('basicBlock()'))

cmds.setParent( '..' )

cmds.setParent( '..' )

#Wheel/ Hub Block
cmds.frameLayout(collapsable=True, label="Wheel & Hub", width=475, height=140)
cmds.columnLayout()
cmds.colorSliderGrp('wheelColour', label="Colour", hsv=(1, 0, 0.017))
cmds.button(label="Wheel", command=('WheelBlock()'))
cmds.colorSliderGrp('hubColour', label="Colour", hsv=(1.463, 0, 0.193))
cmds.button(label="Hub", command=('HubBlock()'))

cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.showWindow( myWin )

#Round Block
cmds.frameLayout(collapsable=True, label="Round Block", width=475, height=140)
cmds.columnLayout()
cmds.intSliderGrp('roundblockDepth', l="Holes", f=True, min=2, max=20, value=4)

cmds.colorSliderGrp('roundblockColour', label="Colour", hsv=(1, 1, 1))
cmds.button(label="Rounded Block", command=('RoundBlock()'))

cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.showWindow( myWin )

#Hole Block
cmds.frameLayout(collapsable=True, label="Hole Block", width=475, height=140)
cmds.columnLayout()
cmds.intSliderGrp('blockHoleDepth', l="Holes", f=True, min=3, max=20, value=6)

cmds.colorSliderGrp('blockHoleColour', label="Colour", hsv=(2, 1, 1))
cmds.button(label="Block with Hole", command=('HoleBlock()'))

cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.showWindow( myWin )

#Axel
cmds.frameLayout(collapsable=True, label="Axel", width=475, height=140)
cmds.columnLayout()
cmds.intSliderGrp('AxelDepth', l="Length", f=True, min=2, max=20, value=4)

cmds.colorSliderGrp('axelColour', label="Colour", hsv=(1, 1, 1))
cmds.button(label="Axel", command=('AxelBlock()'))

cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.showWindow( myWin )

#Round Angled Block
cmds.frameLayout(collapsable=True, label="Angle Block", width=475, height=140)
cmds.optionMenu(label="Angle", changeCommand=choosenAngle)
cmds.menuItem( label='90')
#cmds.menuItem( label='45')
cmds.columnLayout()
cmds.intSliderGrp('angleblockDepth', l="Horizontal Holes", f=True, min=4, max=20, value=6)


cmds.colorSliderGrp('angleblockColour', label="Colour", hsv=(1, 1, 1))
cmds.button(label="Angled Block", command=('AngleBlock()'))

cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.showWindow( myWin )



#-----------------------------WINDOW--------------------------#


######################
##    BASIC BLOCK   ##
######################
def basicBlock():
    blockHeight = cmds.intSliderGrp('blockHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('blockWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('blockDepth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('blockColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "Block" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    for i in range(blockWidth):
        for j in range(blockDepth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
            
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    

######################
##       WHEEL      ##
######################   
def WheelBlock():
    rgb = cmds.colorSliderGrp('wheelColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "Wheel" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    gear1 = cmds.polyGear( h = 2, go = 0.5 ,r = 4, ir = 2)
    cmds.move((2/2.0), moveY=True)
    
    gear2 = cmds.polyGear( h = 2, go = 0.5 ,r = 4, ir = 2)
    cmds.move(((4/2.0)+1), moveY=True)
    cmds.rotate(0,11,0)
   
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    wheel = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.scale(0.5,0.5,0.5)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    
    
######################
##       HUBS       ##
###################### 
def HubBlock():  
    rgb = cmds.colorSliderGrp('hubColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "obj1" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    
    cylin2 = cmds.polyCylinder(r=1.8, h=1)
    cmds.move((1/2.0), moveY=True)
    
    cylin3 = cmds.polyCylinder(r=1.8, h=1)
    cmds.move((3.5), moveY=True)
    
    cylinders = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    cylin1 = cmds.polyCylinder(r=2, h=4)
    cmds.move((4/2.0), moveY=True)
    
    cmds.select(clear=True)
    cmds.select(cylin1, add=True)
    cmds.select(cylinders, add=True)
    cube = cmds.polyCBoolOp(op=2)
    cmds.scale(0.5,0.5,0.5)
    cmds.delete(ch=True)
   
    
    
    
    c1 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434)
    cmds.move( 0.36 , moveX=True)
    cmds.move( -0.26 , moveZ=True)
    cmds.move( 2.44 , moveY=True)
    c2 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434, n = 'c2')
    cmds.move( -0.067 , moveX=True)
    cmds.move( -0.415 , moveZ=True)
    cmds.move( 2.44 , moveY=True)
    c3 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434)
    cmds.move( -0.436 , moveX=True)
    cmds.move( -0.13 , moveZ=True)
    cmds.move( 2.44 , moveY=True)
    c4 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434)
    cmds.move(-0.388 , moveX=True)
    cmds.move( 0.328 , moveZ=True)
    cmds.move( 2.44 , moveY=True)
    c5 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434, n = 'c6')
    cmds.move( 0.032 , moveX=True)
    cmds.move( 0.466 , moveZ=True)
    cmds.move( 2.44 , moveY=True)
    c6 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434, n = 'c5')
    cmds.move( 0.416 , moveX=True)
    cmds.move( 0.193 , moveZ=True)
    cmds.move( 2.44 , moveY=True)
    
    c1 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434)
    cmds.move( 0.36 , moveX=True)
    cmds.move( -0.26 , moveZ=True)
    cmds.move( 1.504 , moveY=True)
    c2 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434, n = 'c2')
    cmds.move( -0.067 , moveX=True)
    cmds.move( -0.415 , moveZ=True)
    cmds.move( 1.504 , moveY=True)
    c3 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434)
    cmds.move( -0.436 , moveX=True)
    cmds.move( -0.13 , moveZ=True)
    cmds.move( 1.504 , moveY=True)
    c4 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434)
    cmds.move(-0.388 , moveX=True)
    cmds.move( 0.328 , moveZ=True)
    cmds.move( 1.504 , moveY=True)
    c5 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434, n = 'c6')
    cmds.move( 0.032 , moveX=True)
    cmds.move( 0.466 , moveZ=True)
    cmds.move( 1.504 , moveY=True)
    c6 = cmds.polyPipe(r=0.2, t=0.04, h=0.9434, n = 'c5')
    cmds.move( 0.416 , moveX=True)
    cmds.move( 0.193 , moveZ=True)
    cmds.move( 1.504 , moveY=True) 
    
    
    
   
            
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    

    
   
   
   
   
   
    
############################
##       ROUND BLOCK      ##
############################   
def RoundBlock():
    blockHeight = 3
    blockWidth = 1
    blockDepth = cmds.intSliderGrp('roundblockDepth', q=True, v=True)
    blockDepth =  blockDepth - 1
    
    
    rgb = cmds.colorSliderGrp('roundblockColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "obj1" + str(nextBlockId)
    nsTmp2 = "obj2" + str(nextBlockId)
    nsTmp3 = "HoleBlock" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cylinderSizeR = cubeSizeY/2
    cylinderSizeY = cubeSizeX
    
    
    cyl1 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    cyl2 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    
    cylinders = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    cube1 = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    cmds.select(clear=True)
    cmds.select(cube1, add=True)
    cmds.select(cylinders, add=True)
    cube = cmds.polyCBoolOp(op=2)
    
    cyl3 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    cyl4 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)    
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    roundCube = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp2)
    cmds.namespace(set=nsTmp2)
    
    new = blockDepth
    
    for i in range(1):
        for j in range(new):
            cylinderDepth = blockDepth + (blockDepth * 0.3);
            cmds.polyCylinder(r=0.25, h=cylinderDepth)
            cmds.move((cubeSizeY /2), moveY=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.8), moveZ=True, a=True)
            cmds.rotate(90,90,0)


    cyli1 = cmds.polyCylinder(r=0.25, h=cylinderDepth)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cylinders = cmds.polyUnite((nsTmp2+":*"), n = nsTmp2 , ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    
   
    
    cmds.select(clear=True)
    cmds.select(roundCube, add=True)
    cmds.select(cylinders, add=True)
    cube = cmds.polyCBoolOp(op=2)
    
    cmds.delete( ch=True )
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    cmds.namespace(removeNamespace=":"+nsTmp2,mergeNamespaceWithParent=True)
    cmds.namespace(removeNamespace=":"+nsTmp3,mergeNamespaceWithParent=True)
    
            
    
    
    
      
    
######################
##    HOLE BLOCK    ##
######################    
def HoleBlock():
    
    blockHeight = 3
    blockWidth = 2
    blockDepth = cmds.intSliderGrp('blockHoleDepth', q=True, v=True)
    blockDepth = blockDepth + 1
    
    
    rgb = cmds.colorSliderGrp('blockHoleColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "obj" + str(nextBlockId)
    nsTmp2 = "HoleBlock" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.4
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    
    cmds.polyCube(n='cubeBlock',h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    
    
    for i in range(1):
        for j in range(blockDepth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cube = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp2)
    cmds.namespace(set=nsTmp2)
    
    
    for i in range(1):
        for j in range(blockDepth-1):
            cylinderDepth = blockDepth + (blockDepth * 0.3);
            cmds.polyCylinder(r=0.25, h=cylinderDepth)
            cmds.move((cubeSizeY /2), moveY=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.8), moveZ=True, a=True)
            cmds.rotate(90,90,0)


    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cylinders = cmds.polyUnite((nsTmp2+":*"), n = nsTmp2 , ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
   
    
    cmds.select(clear=True)
    cmds.select(cube, add=True)
    cmds.select(cylinders, add=True)
    cube = cmds.polyCBoolOp(op=2)
    
    cmds.delete( ch=True )
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True) 
    cmds.namespace(removeNamespace=":"+nsTmp2,mergeNamespaceWithParent=True) 
    
    
######################
##    ANGLE BLOCK   ##
######################    
def AngleBlock():
    blockHeight = 3
    blockWidth = 1
    blockDepth = cmds.intSliderGrp('angleblockDepth', q=True, v=True)
    blockDepth = blockDepth - 1
    blockDepth2 = blockDepth - 2
    
 ##    CREATE SECOND BLOCK  ##     
    rgb = cmds.colorSliderGrp('angleblockColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "obj1" + str(nextBlockId)
    nsTmp2 = "obj2" + str(nextBlockId)
    nsTmp3 = "HoleBlock" + str(nextBlockId)
    nsTmp4 = "MoveBlock" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth2 * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cylinderSizeR = cubeSizeY/2
    cylinderSizeY = cubeSizeX
    
    
    cyl1 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    cyl2 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    
    cylinders = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    cube1 = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    cmds.select(clear=True)
    cmds.select(cube1, add=True)
    cmds.select(cylinders, add=True)
    cube = cmds.polyCBoolOp(op=2)
    
    cyl3 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    cyl4 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)    
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    block1 = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp2)
    cmds.namespace(set=nsTmp2)
    
    
    new = blockDepth2
    
    for i in range(1):
        for j in range(new):
            cylinderDepth = blockDepth2 + (blockDepth2 * 0.3);
            cmds.polyCylinder(r=0.25, h=cylinderDepth)
            cmds.move((cubeSizeY /2), moveY=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.8), moveZ=True, a=True)
            cmds.rotate(90,90,0)


    cyli1 = cmds.polyCylinder(r=0.25, h=cylinderDepth)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cylinders = cmds.polyUnite((nsTmp2+":*"), n = nsTmp2 , ch=False)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    
   
    
    cmds.select(clear=True)
    cmds.select(block1, add=True)
    cmds.select(cylinders, add=True)
    newcube2 = cmds.polyCBoolOp(op=2, n= 'newcube2')
    
     ##    MOVE SECOND BLOCK  ## 
    movement = ((blockDepth2 * 1.2)/3)
     
    cmds.select(clear=True)
    cmds.select(newcube2, add=True)
    cmds.rotate(90, 0 ,0)
    cmds.move((movement), moveY=True)
    cmds.move(((cubeSizeZ/2)+ 0.79), moveZ=True)
    cmds.delete( ch=True )
    
    cmds.namespace(removeNamespace=":"+nsTmp2,mergeNamespaceWithParent=True) 
    
 ##    CREATE FIRST BLOCK  ## 
 
    rgb = cmds.colorSliderGrp('angleblockColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "obj1" + str(nextBlockId)
    nsTmp2 = "obj2" + str(nextBlockId)
    nsTmp3 = "HoleBlock" + str(nextBlockId)
    nsTmp4 = "MoveBlock" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cylinderSizeR = cubeSizeY/2
    cylinderSizeY = cubeSizeX
    
    
    cyl1 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    cyl2 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    
    cylinders = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    cube1 = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    cmds.select(clear=True)
    cmds.select(cube1, add=True)
    cmds.select(cylinders, add=True)
    cube = cmds.polyCBoolOp(op=2)
    
    cyl3 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    cyl4 = cmds.polyCylinder(r=cylinderSizeR, h=cylinderSizeY)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)    
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    block1 = cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp2)
    cmds.namespace(set=nsTmp2)
    
    
    new = blockDepth
    
    for i in range(1):
        for j in range(new):
            cylinderDepth = blockDepth + (blockDepth * 0.3);
            cmds.polyCylinder(r=0.25, h=cylinderDepth)
            cmds.move((cubeSizeY /2), moveY=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.8), moveZ=True, a=True)
            cmds.rotate(90,90,0)


    cyli1 = cmds.polyCylinder(r=0.25, h=cylinderDepth)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move(-(cubeSizeZ/2), moveZ=True)
    cmds.rotate(90,90,0)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cylinders = cmds.polyUnite((nsTmp2+":*"), n = nsTmp2 , ch=False)
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
   
   
    
    cmds.select(clear=True)
    cmds.select(block1, add=True)
    cmds.select(cylinders, add=True)
    newcube = cmds.polyCBoolOp(op=2, n ='newcube')
    cmds.delete( ch=True )
    
    cmds.namespace(removeNamespace=":"+nsTmp2,mergeNamespaceWithParent=True)
    
    cmds.select(clear=True)
    cmds.select(newcube, add=True)
    cmds.select(newcube2, add=True)
    newcube = cmds.polyUnite(ch=False, n ='newcube')
    cmds.delete( ch=True )

    cmds.select(clear=True)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp2)
    cmds.namespace(set=nsTmp2)
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp2+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    angledblock90 = cmds.polyUnite((nsTmp2+":*"), n=nsTmp2, ch=False)
    
    cmds.hyperShade(assign=(nsTmp2+":blckMat"))
    
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True) 
    cmds.namespace(removeNamespace=":"+nsTmp2,mergeNamespaceWithParent=True) 
    cmds.namespace(removeNamespace=":"+nsTmp3,mergeNamespaceWithParent=True) 
    cmds.namespace(removeNamespace=":"+nsTmp4,mergeNamespaceWithParent=True) 
    cmds.delete(ch=True)
    
    
   
    
 
 
##############
##   AXEL   ##
############## 
def AxelBlock():
    
    
    sizeY = cmds.intSliderGrp('AxelDepth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('axelColour', q=True, rgbValue=True)
    global nextBlockId
    nsTmp = "axel1" + str(nextBlockId)
    nsTmp2 = "axel2" + str(nextBlockId)
    nextBlockId = nextBlockId + 1
    
    cmds.select(clear=False)
    cmds.namespace(set=":")
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    

    axel = cmds.polyCube(w=0.5, h=sizeY, d=0.2)
    tmp = cmds.polyCube(w=0.2, h=sizeY, d=0.5)

    axel = cmds.polyCBoolOp(axel[0], tmp[0], op=1, ch=False)
    
    cylin = cmds.polyCylinder(r=0.25, h=sizeY-0.25)
    
    tmp = cmds.polySphere(r=0.25)
    cmds.scale(0.5, scaleY=True, a=True)
    cmds.move((sizeY-0.25)*0.5, moveY=True, a=True)
    cylin = cmds.polyCBoolOp(cylin[0], tmp[0], op=1, ch=False)

    tmp = cmds.polySphere(r=0.25)
    cmds.scale(0.5, scaleY=True, a=True)
    cmds.move(-(sizeY-0.25)*0.5, moveY=True, a=True)
    cylin = cmds.polyCBoolOp(cylin[0], tmp[0], op=1, ch=False)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    axel = cmds.polyCBoolOp(axel[0], cylin[0], op=3, ch=False)
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(nsTmp+":blckMat")) 
    
    
    cmds.rotate(90,90,0)
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    cmds.namespace(removeNamespace=":"+nsTmp2,mergeNamespaceWithParent=True) 
   
 
 
