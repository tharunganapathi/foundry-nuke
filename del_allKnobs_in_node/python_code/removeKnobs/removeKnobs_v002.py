
node = nuke.selectedNode()
# node.removeKnob(node['knob_name'])

count = 0
while count < 2:
    for i in node.allKnobs():
        print i.name()
        count = count + 1
        try:
            node.removeKnob(node[i.name()])
        except:
            pass