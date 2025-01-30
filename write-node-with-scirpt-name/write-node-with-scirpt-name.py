scriptname = nuke.root().name()
script_version = scriptname.split('/')[-1]
#print script_version
version_name = (script_version.split('.')[0]).split('_')[-1]
#print version_name

write = nuke.toNode('Write1').knob('file').getValue()
shotname_list = write.split('/')
#print shotname_list
shotname_withExtension = shotname_list.pop(-1)
print shotname_withExtension


extension = shotname_withExtension.split('.')[-1]
print extension
new_shotname_folder = '/'.join(shotname_list) + '/' + version_name + '/' + shotname_withExtension
print new_shotname_folder
