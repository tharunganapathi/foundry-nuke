def postagestamp():
    n = nuke.createNode('PostageStamp')
    n.setInput(0,nuke.toNode('Read1'))
    n.knob('hide_input').setValue(1)

nuke.menu('Nodes').addCommand('PostageStamp  P',postagestamp, icon = 'PostageStamp.png', index = -1)
