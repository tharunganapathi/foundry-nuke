def python_test():
    nuke.createNode('CheckerBoard2')
    nuke.createNode('Grade').knob('postage_stamp').setValue(True)
    nuke.selectedNode().knob('white').setValue([0.702374, 0.131828, 1.0, 1.0])
    nuke.createNode('Write').knob('file').setValue('C:/Users/USER/3D Objects/test_####.jpg')


nuke.menu('Nodes').addCommand('Python test', python_test, icon = 'Primatte.png')