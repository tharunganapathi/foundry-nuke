
import nuke
import nukescripts


def openscript():
    nuke.scriptClear()
    nukescripts.import_script()

    for i in nuke.allNodes():
        i.knob("selected").setValue(False)

    for i in nuke.allNodes():
        i.setSelected(True)
        nukescripts.toggle("disable") 
        i.setSelected(False)

def toggle_all_nodes():

    if len(nuke.selectedNodes()) == 0:
        nuke.message("Please select the nodes")

    else:
        for i in nuke.selectedNodes():
            try:
                #print i.name()
                    
                if i['disable'].value() == True:
                    i['disable'].setValue(False)
                else:
                    i['disable'].setValue(True)
            except:
                pass

            
nuke.menu('Nuke').addMenu('Tharun').addCommand('Openscript', openscript)
nuke.menu('Nuke').addMenu('Tharun').addCommand('Toggle all Nodes', toggle_all_nodes, 'Shift+D')