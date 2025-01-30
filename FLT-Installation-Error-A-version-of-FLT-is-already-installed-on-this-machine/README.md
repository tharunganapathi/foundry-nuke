# FLT-Installation-Error-A-version-of-FLT-is-already-installed-on-this-machine
<br>

![no](https://user-images.githubusercontent.com/65713157/132124051-98ae23eb-863c-416e-be30-dd1b69ea6cae.jpg)



Here, I have explained how to fix the installation error when it shows "A version of FLT is already installed on this machine". 
This method will work for all FLT problems, when you delete those registry files in "Registry Editor"

1. open registry editor by going to run command (Win+R)
2. Then type "regedit"
3. Navigate to the following path. 

##   1. Computer\HKEY_LOCAL_MACHINE\SOFTWARE\FLEXlm License Manager
     Then delete "FLEXlm License Manager"
 ![1  FLEXlm License Manager](https://user-images.githubusercontent.com/65713157/132123519-da556ac5-4bff-4735-a7b1-1933f55febfd.jpg)
<br><br><br>



 
##   2. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Foundry FLEXlm Server
     Then delete "Foundry FLEXlm Server"
     
![2  Foundry FLEXlm Server](https://user-images.githubusercontent.com/65713157/132123721-9d559ec3-b63b-47ba-b109-ea8699a44641.jpg)
<br>

##   3. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Foundry License Server
     Then delete "Foundry License Server"
![3  Foundry License Server](https://user-images.githubusercontent.com/65713157/132123723-097b9f86-c619-4720-9113-612d3bdbbf19.jpg)
<br><br><br>

####  
     Note:
     The above method will definitely work for you, if that doesnt work, also try deleting the following registry key

<br><br><br>

##   4. Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\FLT 7.1v1_is1
     Then delete "FLT 7.1v1_is1"
![4  FLT 7 1v1_is1](https://user-images.githubusercontent.com/65713157/132123728-423d2777-c49d-42c9-9ee9-ba63398b096c.jpg)

<br>
   I hope you understand the above instructions, and also I have made a video for this, please do watch that incase if you cant understand. 

 #  Link :
 ###  https://www.youtube.com/watch?v=PQNsz2aWdAk/channel=THARUNGANAPATHI
<br> 

![FLT Error](https://user-images.githubusercontent.com/65713157/132124150-0ec623b1-a0f9-4ae4-af92-951be7130436.jpg)


