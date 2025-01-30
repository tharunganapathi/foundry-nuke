import nuke

def projectsetting_read():

    i = nuke.selectedNode()
    if i == None:
        nuke.message('Please select the read node')
    i.knob('frame_mode').setValue('start at')
    i.knob('frame').setValue('1')
    #i.knob('colorspace').setValue('sRGB')

    original_range_first = i.knob('origfirst').getValue()
    print original_range_first

    original_range_last = i.knob('origlast').getValue()
    print original_range_last

    lastframe = (original_range_last - original_range_first) + 1
    print lastframe



    nuke.root().knob('first_frame').setValue(1)
    nuke.root().knob('last_frame').setValue(lastframe)
    nukescripts.connect_selected_to_viewer(0)




nuke.menu('Nodes').addCommand('Set Project from read node', projectsetting_read, icon = 'Read.png')


'''
for i in nuke.allNodes('Read'):
    i['frame_mode'].setValue('start at')
    i.knob('frame').setValue('1')
    i['auto_alpha'].setValue(True)
'''