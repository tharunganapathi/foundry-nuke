print '\n'
import os
directory = nuke.getInput('location')
extension = nuke.getInput('enter extension')
a = []
for folder,subfolders,files in os.walk(directory):
    lists = []
    for i in files:
        if i.endswith(extension):
            lists.append(i)
    if len(lists)!=0:
        #print len(lists)
        a.append(len(lists))

print a
#for i,j in enumerate(count,1):
#   print str(i) + ' - ' + str(j)
for i in a:
    print i
result = "\n".join('{}'.format(i) for i in a)
enumerate_result = "\n".join(['{} - {}'.format(i,j) for i,j in enumerate(a,1)])

nuke.message(result)
nuke.message(enumerate_result)
