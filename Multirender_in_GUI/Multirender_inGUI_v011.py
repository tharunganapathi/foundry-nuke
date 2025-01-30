import nuke
render_information = []
def showChannels():
    global render_information
    return '\n'.join(render_information)







def checkRenders():

    nuke.root()['first_frame'].setValue('1')
    nuke.root()['last_frame'].setValue('1')

    for i in nuke.allNodes('Write'):
        i['use_limit'].setValue(False)

       
    global render_information
    render_information = []
    
    def showChannels():
        global render_information
        return '\n'.join(render_information)
    
    
    # function defintions for rendering, from Global or framerange in write node
    def check_global_or_range_first():
        if i.knob('use_limit').getValue()==1.0:
            return int(i.knob('first').getValue())
        else:
            return int(nuke.Root().knob('first_frame').value())
    
    def check_global_or_range_last():
        if i.knob('use_limit').getValue()==1.0:
            return int(i.knob('last').getValue())
        else:
            return int(nuke.Root().knob('last_frame').value())
    
    
    
    node = nuke.toNode('Write1') #Just for avoiding error. It will not use while running the code
    
    
    if len(nuke.selectedNodes())!=0:
        #nuke.display('showChannels()', node, 'Render_Information')
        for i in nuke.selectedNodes():
            
            if i.Class()=='Write':
                shotname_list = i.knob('file').getValue()
                shotname = shotname_list.split('/')[-1]
                nodes =  ('"' +  shotname.ljust(40, " ") + '"  ' + '(' + i.name() + ')'  + '   =    ('+str(check_global_or_range_first()) +'-'+  str(check_global_or_range_last()) +') Frames     Rendering.....')
                render_information.append(nodes)
                nuke.display('showChannels()', node, 'Render_Information')
                #nuke.execute(i,int(nuke.Root().knob('first_frame').value()),int(nuke.Root().knob('last_frame').value()))
                #'''
                try:
                    nuke.execute(i,check_global_or_range_first(),check_global_or_range_last())
                except:
                    nodes =  ('"' +  shotname.ljust(40, " ") + '"  ' + '(' + i.name() + ')'  + '   =    ('+str(check_global_or_range_first()) +'-'+  str(check_global_or_range_last()) +') Frames     Error')
                    render_information.pop(-1)
                    render_information.append(nodes)
                    nuke.display('showChannels()', node, 'Render_Information')
                    #nuke.message('<b><b><font color="red">Render Cancelled by the User</font></b></b>')
                    continue
                #'''
                nodes =  ('"' +  shotname.ljust(40, " ") + '"  ' + '(' + i.name() + ')'  + '   =    ('+str(check_global_or_range_first()) +'-'+  str(check_global_or_range_last()) +') Frames     Completed')
                render_information.pop(-1)
                render_information.append(nodes)
                nuke.display('showChannels()', node, 'Render_Information')
        #nuke.message('Render Completed')
            #else:
                #if len(nuke.selectedNodes()) == len(nuke.selectedNodes('Write'))  :
                    #nuke.message('Please select the <b><b><font color="red">Write</font></b></b> nodes')
        
        else:
            if len(nuke.selectedNodes('Write'))==0 :
                nuke.message('Please select the <b><b><font color="red">Write</font></b></b> nodes')
        
    
    else:
        nuke.message('Please select the nodes you want to render')








def RenderMultipleNodes():
    # Create Backdrop while importing the script - button.
    # And set footage name for all the backdrops.
    # Allign text
    # Render_Information pannel button
    # Show all write nodes in render pannel
    # Render custom write nodes
    # Set frame range for all write nodes
    # Go to Custom Write node.
    # Number of Write Nodes.
    # Set color for completed Write Nodes    
            #color = nuke.getColor()
            #print color
            #nuke.selectedNode().knob('tile_color').setValue(3941384703)
    # Rendered Frames
    # Render Order        
    
    
    
    global render_information
    render_information = []
    
    def showChannels():
        global render_information
        return '\n'.join(render_information)
    
    
    # function defintions for rendering, from Global or framerange in write node
    def check_global_or_range_first():
        if i.knob('use_limit').getValue()==1.0:
            return int(i.knob('first').getValue())
        else:
            return int(nuke.Root().knob('first_frame').value())
    
    def check_global_or_range_last():
        if i.knob('use_limit').getValue()==1.0:
            return int(i.knob('last').getValue())
        else:
            return int(nuke.Root().knob('last_frame').value())
    
    
    
    node = nuke.toNode('Write1') #Just for avoiding error. It will not use while running the code
    
    
    if len(nuke.selectedNodes())!=0:
        #nuke.display('showChannels()', node, 'Render_Information')
        for i in nuke.selectedNodes():
            
            if i.Class()=='Write':
                shotname_list = i.knob('file').getValue()
                shotname = shotname_list.split('/')[-1]
                nodes =  ('"' +  shotname.ljust(40, " ") + '"  ' + '(' + i.name() + ')'  + '   =    ('+str(check_global_or_range_first()) +'-'+  str(check_global_or_range_last()) +') Frames     Rendering.....')
                render_information.append(nodes)
                nuke.display('showChannels()', node, 'Render_Information')
                #nuke.execute(i,int(nuke.Root().knob('first_frame').value()),int(nuke.Root().knob('last_frame').value()))
                #'''
                try:
                    nuke.execute(i,check_global_or_range_first(),check_global_or_range_last())
                except:
                    nodes =  ('"' +  shotname.ljust(40, " ") + '"  ' + '(' + i.name() + ')'  + '   =    ('+str(check_global_or_range_first()) +'-'+  str(check_global_or_range_last()) +') Frames     Cancelled')
                    render_information.pop(-1)
                    render_information.append(nodes)
                    nuke.display('showChannels()', node, 'Render_Information')
                    nuke.message('<b><b><font color="red">Render Cancelled by the User</font></b></b>')
                    break
                #'''
                nodes =  ('"' +  shotname.ljust(40, " ") + '"  ' + '(' + i.name() + ')'  + '   =    ('+str(check_global_or_range_first()) +'-'+  str(check_global_or_range_last()) +') Frames     Completed')
                render_information.pop(-1)
                render_information.append(nodes)
                nuke.display('showChannels()', node, 'Render_Information')
        #nuke.message('Render Completed')
            #else:
                #if len(nuke.selectedNodes()) == len(nuke.selectedNodes('Write'))  :
                    #nuke.message('Please select the <b><b><font color="red">Write</font></b></b> nodes')
        
        else:
            if len(nuke.selectedNodes('Write'))==0 :
                nuke.message('Please select the <b><b><font color="red">Write</font></b></b> nodes')
        
    
    else:
        nuke.message('Please select the nodes you want to render')




def select_All_Writenodes():
    for i in nuke.allNodes('Write'):
        i.setSelected(True)    


def setFrameRange():
    for i in nuke.allNodes('Write'):
        frameRange = i.frameRange()
        firstFrame = frameRange.first()
        lastFrame = frameRange.last()
        print i.name()
        print firstFrame
        print lastFrame
        i.knob('use_limit').setValue(True)
        i.knob('first').setValue(firstFrame)
        i.knob('last').setValue(lastFrame)
        print '\n'



nuke.menu('Nodes').addMenu('RenderMultipleNodes',icon = 'Render.png').addCommand('check the renders', checkRenders, icon = 'Shuffle.png')
nuke.menu('Nodes').addMenu('RenderMultipleNodes',icon = 'Render.png').addCommand('Set Frame Range', setFrameRange, icon = 'FrameRange.png')
nuke.menu('Nodes').addMenu('RenderMultipleNodes',icon = 'Render.png').addCommand('Select all Write nodes', select_All_Writenodes,icon = 'Write.png')
nuke.menu('Nodes').addMenu('RenderMultipleNodes',icon = 'Render.png').addCommand('Render selected Write nodes', RenderMultipleNodes, icon = 'ProjectionSolver.png')
