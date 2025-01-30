

import shutil
src = r'C:\Users\THARUN\.nuke'
nuke12 = r'C:\Users\THARUN\.nuke\nuke_12'
nuke13 = r'C:\Users\THARUN\.nuke\nuke_13'






nuke12_list  = (list(nuke12))
nuke12_renaming = []
for i in nuke12_list:
    replaced = i.replace('\\','/')
    nuke12_renaming.append(replaced)
nuke12_renamed =  ''.join((nuke12_renaming))





nuke13_list  = (list(nuke13))
nuke13_renaming = []
for i in nuke13_list:
    replaced = i.replace('\\','/')
    nuke13_renaming.append(replaced)
nuke13_renamed =  ''.join((nuke13_renaming))


print (nuke12_renamed)
print (nuke13_renamed)


lists = ['/ScriptEditorHistory.xml','/recent_files','preferences12.2.nk','preferences13.0.nk']
for i in lists:
    try:
        shutil.copy(src+i,nuke12)
        shutil.copy(src+i,nuke13)
    except:
        None

