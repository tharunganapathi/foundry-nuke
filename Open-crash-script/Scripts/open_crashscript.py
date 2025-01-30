# import nuke

# def openscript():
#     nuke.scriptClear()
#     nuke.scriptOpen("")
#     #nuke.message('hi')
#     for i in nuke.allNodes():
#         i.setSelected(True)
#         nukescripts.toggle("disable")
#         i.setSelected(False)



# def toggle_all_nodes():
#     for i in nuke.allNodes():
#         i.setSelected(True)
#         nukescripts.toggle("disable")
#         i.setSelected(False)



# nuke.menu('Nuke').addMenu('Tharun').addCommand('Openscript',openscript())
# nuke.menu('Nuke').addMenu('Tharun').addCommand('Toggle all Nodes',toggle_all_nodes())




import nuke
import nukescripts

def open_crashscript():
    nuke.scriptClear()
    nuke.scriptOpen("")
    #nuke.message('hi')
    for i in nuke.allNodes():
        i.setSelected(True)
        nukescripts.toggle("disable")
        i.setSelected(False)



def toggle_all_nodes():
    for i in nuke.allNodes():
        i.setSelected(True)
        nukescripts.toggle("disable")
        i.setSelected(False)

