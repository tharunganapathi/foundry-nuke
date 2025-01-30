
tracker3 = nuke.toNode("Tracker3")
tracker4 = nuke.createNode("Tracker4")

print tracker4['translate'].value()

# will copy the "translate & center" values from tracket3 to tracker 4
tracker4['translate'].copyAnimations(tracker3['translate'].animations())
tracker4['center'].copyAnimations(tracker3['center'].animations())


# will create "track1" in tracker4 node. 
# this will through you an syntax error, Don't worry, it works fine. 
# have to invest some time to fix the popup error. 
tracker4['add_track'].execute()

# will set expression in "x and y" of tracker4 node
tracker4['tracks'].setExpression('translate.x+center.x',2)
tracker4['tracks'].setExpression('translate.y+center.y',3)




##########################################################################
#####   Additional notes for getting all knob date of tracker node   #####
##########################################################################

for i,j in enumerate(range(100)):
    print i, tracker4['tracks'].fullyQualifiedName(j)
