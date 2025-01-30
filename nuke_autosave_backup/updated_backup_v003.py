#1. fix when you have multilple autosave file
#2. fix when there is no autosave file everytime when this script is running
#3. Implement timer module



import os
import shutil



try:
    nk_workfile = nuke.scriptName()
except:
    nk_workfile = r'C:\Users\TharunG\Documents\shows\writer\WR_054_SHOT_002\mid\comp\TharunG\workfile\nuke\WR_054_SHOT_002_b002_v002.nk'

nk_workfile = nk_workfile.replace('\\','/')



#########################################################################################
################################        src_file         ################################
#########################################################################################

src_file = os.path.basename(nk_workfile) + '.autosave'
print ("src_file = " + src_file)



#########################################################################################
################################     src_file_path       ################################
#########################################################################################

src_file_path = os.path.dirname(nk_workfile)
print ("src_file_path = " + src_file_path)


src_file_fullPath = (os.path.join(src_file_path,src_file))
print ("src_file_fullPath = ",src_file_fullPath)

#########################################################################################
################################     dst_file_path       ################################
#########################################################################################

showName_index = src_file_path.split('/').index('shows')
showName = (src_file_path.split('/')[showName_index+1])
shotName = (src_file_path.split('/')[showName_index+2])
# print ("showname = " + showName)
# print ("shotname = " + shotName)
user = (os.path.expanduser('~'))     
dst_file_path = os.path.join('C:','Users',user,'Documents','nuke','workfile_backup','shows',showName,shotName)
print ("dst_file_path = " + dst_file_path)



#########################################################################################
############################        src_file_tocopy         #############################
#########################################################################################
print ('\n'*2)
#____when there is autosave

if (os.path.exists(src_file_fullPath)):
    src_file_tocopy = src_file_fullPath
    print("src_file_tocopy = ",src_file_tocopy)
else:
    src_file_tocopy = nk_workfile
    print("src_file_tocopy = ",src_file_tocopy)

dst_file_nameonly = os.path.splitext(os.path.splitext(src_file)[0])[0]



#########################################################################################
############################        check for bkp_v01        ############################
#########################################################################################


v01_backup = (os.path.join(dst_file_path,dst_file_nameonly + '_backup_v001.nk'))
backuplist = []

if os.path.exists(v01_backup):
    for i in os.listdir(dst_file_path):
        if i.startswith(dst_file_nameonly):
            backuplist.append(i)

    maxima = (max(backuplist))
    version = maxima[-6:-3]

    version_up = int(version) + 1
    newversion = "{:03d}".format(version_up)
    version = newversion

    upgraded_version = os.path.join(dst_file_path,dst_file_nameonly + "_backup_v" + version + '.nk')
    print ("upgraded_version = ",upgraded_version)
    shutil.copy2(src_file_tocopy, os.path.join(dst_file_path,upgraded_version))


else:
    try:
        os.makedirs(dst_file_path)
        shutil.copy2(src_file_tocopy, os.path.join(dst_file_path,v01_backup))
    except:
        pass
        shutil.copy2(src_file_tocopy, os.path.join(dst_file_path,v01_backup))



