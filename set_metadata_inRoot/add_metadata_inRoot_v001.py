metadata_list = []
for i,j in nuke.selectedNode().metadata().iteritems():

    metadata_list.append(('{}:{}'.format(i,j)))

metadata = ''.join(a)
nuke.message(metadata)
print metadata



#nuke.root().addKnob(nuke.Multiline_Eval_String_Knob('metadata','Meta Data'))

nuke.root()['metadata'].setValue(metadataa)
nuke.root()['metadata'].setEnabled(False)
