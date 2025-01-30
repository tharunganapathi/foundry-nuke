
node = nuke.root()
# node.removeKnob(node['knob_name'])

def delAllKnobs():
    for i in range(2):
        for i in node.allKnobs():
            print (i.name())
            try:
                node.removeKnob(node[i.name()])
            except:
                pass
    
delAllKnobs()
