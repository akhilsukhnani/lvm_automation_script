#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time


# In[2]:


def intro():

    print("""
   Press 1 => To Create a Logical Volume
   Press 2 => To Check all the existing block devices
   Press 3 => To diplay all the logical volumes 
   Press 4 => To display all Volume Groups
   Press 5 => To create a Volume Group
   Press 6 => To display all the Physical Volumes
   Press 7 => To create a Physical Volumes
   Press 8 => To extend the size of a partition
   Press 9 => To decrease the size of partition
   Press 10 => To create a Volume Group 
   Press 11 => EXIT
   """)


# In[4]:


def check_all_block_devices():
    print( os.system("lsblk && fdisk -l") )
    
def display_VolumeGroups():
    os.system("vgdisplay")

def display_PhysicalVolumes():
    print(os.system("pvdisplay"))
    
def display_LogicalVolumes():
    print(os.system("lvdisplay"))
        


# In[ ]:


def create_VolumeGroups(): 
    print(os.system("figlet -c VOLUME GROUPS && vgdisplay "))
    
    create_VolumeGroups.choice_vg_name = input("Please enter a name which you want to dedicate to the volume group")
    choice_vg_devices = input("Enter physical Volumes which you want to contribute in Volume Group (separated by space)")
    vgcreate_command = "vgcreate " + create_VolumeGroups.choice_vg_name +" " +choice_vg_devices
    print(os.system(vgcreate_command))
    
    display_vg_after_creation ="figlet -c VOLUME GROUP CREATED && vgdisplay " + create_VolumeGroups.choice_vg_name
    print( os.system(display_vg_after_creation) )


# In[ ]:


def create_PhysicalVolume():
    print(os.system(" figlet -c HARD DRIVES && fdisk -l  && figlet -c PHYSICAL VOLUMES && pvs "))
    choice_pv = input("Enter block device names which you want to convert in Physical Volume (separated by space)")
    
    
    #creating physical_volume
    pv_creation_cmd = "echo y |pvcreate " + choice_pv
    print(os.system(pv_creation_cmd) )
    
    display_pv_after_creation ="figlet -c PHYSICAL VOLUME CREATED && pvdisplay " + choice_pv
    print( os.system(display_pv_after_creation) )
    


# In[ ]:


def create_logical_volume():
    #creating physical_volume
    create_PhysicalVolume()
    
    
    #creating volume groups 
    create_VolumeGroups()
    
    #creating logical volume
    print(os.system("figlet -c LOGICAL VOLUMES && lvdisplay "))
    
    choice_lv_size = input("Enter the size for logical volume in GBs") + "G"
    choice_lv_name =  input ("Enter name by which logical volume would be created")
    
    lvcreate_command = "lvcreate --size "+ choice_lv_size + " --name " + choice_lv_name +" "+ create_VolumeGroups.choice_vg_name
    print(os.system(lvcreate_command))
    display_lv_after_creation = "figlet -c Logical Volume Created && lvdisplay /dev/" +  create_VolumeGroups.choice_vg_name + "/" + choice_lv_name    


# In[ ]:


def extend_SizeOfVolume():
    print(os.system("lvdisplay"))
    name_of_volume = input("Enter the logical volume name for which the size is to be extended")
    size_extend = input("Enter the size in GBs by which you want to extend") + "G"
    size_current = input("Enter the current size in GBs")
    effective_size = size_extend + size_current
        
    extend_cmd="lvextend --size +" + size_extend + "G" + " " + name_of_volume + "&& resize2fs " + name_of_volume +" "+ effective_size+"G"
    print(os.system(extend_cmd))
    print(os.system("lvdisplay"))


# In[ ]:
def decrease_SizeOfVolume():
    print(os.system("lvdisplay"))
    name_of_volume = input("Enter the logical volume name for which the size is to be decreased")
    size_decrease = int(input("Enter the size in GBs by which you want to decrease"))
    size_current = int(input("Enter the current size in GBs"))
    effective_size = str(size_current - size_decrease)
    decrease_cmd="lvreduce --size -" +str(size_decrease) + "G" + " " + name_of_volume + "&& resize2fs " + name_of_volume +" "+ effective_size+"G"
    print(os.system(decrease_cmd))
    print(os.system("lvdisplay"))

 


# In[5]:


while True:
    print(os.system("figlet -c LVM AUTOMATION"))
    intro()
    choice = input()
    if choice == "1" :
        create_logical_volume()
    elif choice == "2":
        check_all_block_devices()
    elif choice == "3":
        display_LogicalVolumes()
    elif choice == "4":
        display_VolumeGroups()
    elif choice == "5":
        create_VolumeGroups()
    elif choice == "6":
        display_PhysicalVolumes()
    elif choice == "7":
        create_PhysicalVolume()
    elif choice == "8":
        extend_SizeOfVolume()
    elif choice == "9":
        decrease_SizeOfVolume()
    elif choice == "10":
         create_VolumeGroups()
    elif choice == "11":
        break
    else:
        print("Wrong INPUT")


# In[ ]:




