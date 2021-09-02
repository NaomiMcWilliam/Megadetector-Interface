# Megadetector-Interface
## Introduction
When camera trap studies are conducted there are usually a large number of empty images that are present. The Megadetector was developed by Microsoft in order to classify images into either containing an animal/human/vehicle, or being empty, to reduce time sorting through the images manually. Further information can be found here:
https://github.com/microsoft/CameraTraps/blob/master/megadetector.md


I have created a GUI (graphical user interface) for the Megadetector, as a part of my internship at ZSL. Downloading the megadetector and using it can be quite complicated, the GUI has made it a much simpler, and more user friendly experience.
It allows users to create a JSON file for their images, visually annotate their images with bounding boxes of animals, and sort their images into folders based on if they are empty / contain an animal etc. It will never alter the original images, it creates copies.


The download instructions can be found below.

This GUI is only compatible with Windows.
The application is around 4GB after installation.

Megadetector works best with a computer with a Graphics card installed, otherwise it can be quite slow. Typical speeds with a good graphics card are 1 second per image to create the JSON file (other features are much faster). Notes on future modifications to make the process faster on machines without powerful graphics cards are mentioned in the future improvements section below.


Any additional suggestions are welcome, and please contact me if there are any issues with installation / runnning and I will do my best to help. :)

## Installation

If you have any issues during the installation process, scroll down for help.

Download SetupMD.exe to download the interface. 
You will have to click a few boxes, to allow the application to install.


For example:

![image](https://user-images.githubusercontent.com/86857625/130882537-44bdb91d-a6dc-435f-9ed1-40b57e821ca3.png)

Click on 'Don't Run'

![image](https://user-images.githubusercontent.com/86857625/130882565-4846868d-bcca-481f-8248-c07592745045.png)

Click on 'Run anyway'


Then, you can click Next and choose where to put the folder. The current path is the recommended place to put this application.
After this installation, another window should pop up with the words 'Installer'. This is installing additional folders, and can take some time (around 10-20 minutes).
### How it should look after installation
![image](https://user-images.githubusercontent.com/86857625/131496885-a099e9f5-55f5-4d13-a66a-6650019392cf.png)
![image](https://user-images.githubusercontent.com/86857625/131496905-8d4e4c41-5781-4b35-ac0a-5a9ef5f6d4fd.png)

Installation folder

![image](https://user-images.githubusercontent.com/86857625/131496929-ed863598-0e44-4d31-8859-856259f91786.png)

Programs folder

![image](https://user-images.githubusercontent.com/86857625/131497002-f9b098c0-8979-4485-9d43-68751669da12.png)

Resources folder

![image](https://user-images.githubusercontent.com/86857625/131497021-cef3768c-f770-45cd-95a4-2ed0978eece0.png)


### Help
### No RUN_GUI
On some machines it does not install 'RUN_GUI.exe', there will be no file with a flamingo icon. If this is the case, you can just click on 'GUI' in the same folder, which is a batch file and it will do the same thing as RUN_GUI.


#### Virtual Machine help
If you are running it through a Windows Virtual machine, at first it will install it to your downloads, but due to running it in a virtual machine the path to downloads can be quite complex. You will need to move the SetupMD.exe directly to the C: drive for example, and run it from there.


#### Older Windows help
You will need to install curl if you are running on anything other than Windows 10 version 1803. You can do this by following the link: 
https://developer.zendesk.com/documentation/developer-tools/getting-started/installing-and-using-curl/#installing-curl


## Running
Once it has finished installing, go to where the folder has been created.
Usually this will be in the C Drive unless the path was changed. Click on 'MegaDetectorGUI', 'Program', 'RUN_GUI' with the flamingo icon. This should open the application, where the process of using the MegaDetector is explained :). 


![image](https://user-images.githubusercontent.com/86857625/130883585-5b9ee069-1586-45f2-9716-84e4758fc7c7.png)




(Currently it will also open the Command Prompt, to enable you to quit the application fully, but this is to be changed in future versions.)

These are currently three different features to choose from. Creating a JSON file, adding annotations to images, and sorting the images into folders. First a JSON file must be created, and then the latter two features can be used, as explained in the GUI. Currently, if you want to do something else after completing one task (such as sorting images into folders after creating the JSON file), you must first close the application and open it again. This should be fixed in later versions.


To close the application, click QUIT on the interface. (You will also need to click 'X' on the Command Prompt that has opened, but this is to be changed in future versions.)

### Example photos of GUI
#### Home tab
![image](https://user-images.githubusercontent.com/86857625/131762022-8cd4492e-b494-4328-97bc-98537088fe04.png)

#### JSON tab
![image](https://user-images.githubusercontent.com/86857625/131762380-77041994-bd86-468e-afd2-1a45c5977991.png)

Console output example when creating a JSON file:
![image](https://user-images.githubusercontent.com/86857625/131762459-a313db2f-c325-4c32-a9d7-9dbc8969b880.png)

#### Annotations tab
![image](https://user-images.githubusercontent.com/86857625/131762056-16884b92-b59c-4e21-868b-00044ce46e56.png)

Console output example when creating annotated imgaes:
![image](https://user-images.githubusercontent.com/86857625/131762731-a7a582a3-172c-494d-b67e-917733d4990c.png)

#### Sorting into folders tab
![image](https://user-images.githubusercontent.com/86857625/131762063-97e87e5a-d19d-4584-b215-1c6659b40dbb.png)

Console output example when creating annotated imgaes:
![image](https://user-images.githubusercontent.com/86857625/131762971-57ee8f6e-713f-4b40-90cf-672b1f1541e3.png)



## Current issues / Future updates
1. Allowing for multiple threads. Currently, if you want to run more than one task, such as making a JSON file and then sorting the images into folders, you have to first close the application and start again as it will say it cannot run more than one thread at once. This will be fixed soon.

2. Ensuring the QUIT button functions properly, so that it closes both the GUI and the command module console that it opens. Currently it only closes the GUI, and you must close the command console manually by pressing the 'X'

3. Incorperating Megadetector v5 into the GUI once it is realeased. Currently, it is using Megadetector v4.1.0

4. Including optimisation features to make running the megadetector faster. Unfortunately, currently it only works well on computers with powerful graphics cards. It still runs on laptops and PC's without this, but can be a lot slower (e.g. 30s/image). There are various ideas to improve upon this, so that it can still run quickly on less powerful machines. 

Members of ZSL are looking into running the application through tensorflowlite, which is a smaller and faster version to tensorflow version 1 and 2, which is what is currently  being used by megadetector v4 and v5.
They are also looking into manually reducing the image size before hand, rather than having the megadetector do this, as doing it manually via image processing applications could be significantly faster.
