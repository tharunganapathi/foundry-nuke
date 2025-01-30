extension_alone = nuke.getInput('Type the extension of Write node : ')
extension = '.'+extension_alone
print extension
print '\n'
writenodes = []
for i in nuke.allNodes('Write'):
    file = i['file'].value()
    if file.endswith(extension.lower()) or file.endswith(extension.upper()):
        print i.name()
        i.setSelected(True)