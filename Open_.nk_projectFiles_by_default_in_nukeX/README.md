# Open-.nk-project-files-by-default-in-nukeX
<br>
By default, we cannot able to lauch the nuke's workfile in nukeX.
but we can achieve that through modifying some commands in ""regedit""


# Explanatory video:
##  link : https://www.youtube.com/watch?v=bsccrlIW1U0&t/channel=THARUNGANAPATHI
<br><br><br>

#   1. Goto Startmenu, and search for Nuke12.2v4, then right click and open file location<br>

![1](https://user-images.githubusercontent.com/65713157/132125009-015a85f1-122c-478a-986b-86893b45db9e.jpg)
<br><br><br>

#   2. Then right click on Nuke12.2v4, then click on properites<br>
![2](https://user-images.githubusercontent.com/65713157/132125068-b2b766d8-944d-4d18-96ae-c5053e0a3c87.jpg)
<br><br><br>



#   3. In target, by default you have this command
    "C:\Program Files\Nuke12.2v5\Nuke12.2.exe"
    
<br><br>

#  4. At the end, leave single space add  type the following command
     --nukex "%1"
     
    
###   So then it will look like

    "C:\Program Files\Nuke12.2v5\Nuke12.2.exe"  --nukex "%1"
    
<br><br>
    
 #  5.  Click ok, Then it will ask for admin rights, then click on continue.
  ![3](https://user-images.githubusercontent.com/65713157/132125455-ddbd8191-214e-4491-8213-baff064375a2.jpg)
<br><br><br>

#   6. Then goto "regedit"
#      Right click on "HKEY_CLASSES_ROOT" and create new key as "NukeScript"
       NukeScript
![4](https://user-images.githubusercontent.com/65713157/132125645-8fcd4a6a-f2f3-4c96-b354-f634a6f6123f.jpg)

![5](https://user-images.githubusercontent.com/65713157/132125710-0d016c3d-ca28-469c-8cb3-8424e43683c7.jpg)
<br><br><br><br><br>

##   7. Right click on "NukeScript"   ,   then add new key as "shell"
##      Right click on "shell"        ,   then add new key as "command"

![image](https://user-images.githubusercontent.com/65713157/132125826-56880b01-e5ab-484f-812b-a45f61eb2440.png)
<br><br><br><br><br>

##    After adding the keys it will look like
![image](https://user-images.githubusercontent.com/65713157/132125858-6e263743-0dbb-443b-bca5-cb3ce2e72175.png)




<br>
<br>

Then follow the below video


