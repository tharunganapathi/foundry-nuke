

for i in node.allKnobs():
    print i.name()
    try:
        node.removeKnob(node[i.name()])
    except:
        pass