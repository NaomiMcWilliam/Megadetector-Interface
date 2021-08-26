import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import os
import subprocess
import threading
import re
import ctypes


class MD_GUI(object):
    def __init__(self, window):
        self.windows_scaling()

        self.main_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  #main path, the parent directory MegaDetectorGUI
        self.window = window
        self.get_images()


    def get_images(self):
        #IMAGE FILES
        
        #images of tabs
        self.img_home = PhotoImage(file=f"home.png")
        self.img_json = PhotoImage(file=f"jsonTab.png")
        self.img_annotate = PhotoImage(file=f"annotationsTab.png")
        self.img_sort = PhotoImage(file=f"sortTab.png")
        self.img_quit = PhotoImage(file=f"quit.png")

        #images of commonly used buttons
        self.img_folder_select = PhotoImage(file=f"selectFolder.png")
        self.img_enter_name = PhotoImage(file=f"enter_name.png")
        self.img_enter_small = PhotoImage(file=f"textBox.png")
        self.img_slct_small = PhotoImage(file=f"selectFolder_small.png")

        #background images
        self.menuBackground_img = PhotoImage(file=f"mainBackground.png")
        self.jsonBackground_img = PhotoImage(file=f"jsonBackground.png")
        self.annotationBackground_img = PhotoImage(file=f"annotationBackground.png")
        self.folderBackground_img = PhotoImage(file=f"folderBackground.png")

        
    #set windows awareness
    def windows_scaling(self):
        # Query Dots Per Inch Awareness (Windows 10 and 8) to fix display scaling issues
        awareness = ctypes.c_int()
        errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        # Windows 10 and 8
        errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        # Windows 7 and Vista
        success = ctypes.windll.user32.SetProcessDPIAware()

        # sets working directory to same as script
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    
    def tab_init(self, window):

        tabControl = ttk.Notebook(window)

        # turn off default tabs at top
        style = ttk.Style()
        style.layout('TNotebook.Tab', [])

        # Tabs

        # MENU
        menuTab = ttk.Frame(tabControl)
        jsonTab = ttk.Frame(tabControl)
        annotationTab = ttk.Frame(tabControl)
        folderTab = ttk.Frame(tabControl)

        # Adding tabs to control
        tabControl.add(menuTab, text='Menu')
        tabControl.add(jsonTab, text='JSON')
        tabControl.add(annotationTab, text='Annotations')
        tabControl.add(folderTab, text='Sort into Folders')
        # Initialise tabs

        tabControl.pack(expand=1, fill="both")
        #self.menuTab, self.jsonTab, self.annotationTab, self.tabControl, window = self.tab_init(window)

        return tabControl, style, menuTab, jsonTab, annotationTab, folderTab


    def make_labels(self,menuTab, jsonTab, annotationTab, folderTab):
        menuBackground = Label(menuTab, image=self.menuBackground_img, bd=0, highlightthickness=0, relief='ridge')
        jsonBackground = Label(jsonTab, image=self.jsonBackground_img, bd=0, highlightthickness=0, relief='ridge')
        annotationBackground = Label(annotationTab, image=self.annotationBackground_img, bd=0, highlightthickness=0, relief='ridge')
        folderBackground = Label(folderTab, image=self.folderBackground_img, bd=0, highlightthickness=0, relief='ridge')

        # Place on tabs
        menuBackground.place(x=0, y=0)
        jsonBackground.place(x=0, y=0)
        annotationBackground.place(x=0, y=0)
        folderBackground.place(x=0, y=0)

        return menuTab, jsonTab, annotationTab, folderTab


    def create(self):
        
        self.window.geometry("1920x1080")
        self.window.configure(bg="#ffbaa2")
        self.window.resizable(False, False)
        
        
        # Make tabs
        self.tabControl, style, menuTab, jsonTab, annotationTab, folderTab= self.tab_init(self.window)
        menuTab, jsonTab, annotationTab, folderTab= self.make_labels(menuTab, jsonTab, annotationTab, folderTab)

        menuTab, self.tabControl= MENU_Tab(self.window, menuTab, jsonTab, annotationTab, folderTab, self.tabControl).make_tabs()
        jsonTab, self.tabControl = JSON_Tab(self.window, menuTab, jsonTab, annotationTab,folderTab,  self.tabControl).buttons()
        annotationTab, self.tabControl = ANNOTATE_Tab(self.window, menuTab, jsonTab, annotationTab,folderTab,  self.tabControl).buttons()
        folderTab, self.tabControl = FOLDER_Tab(self.window, menuTab, jsonTab, annotationTab, folderTab, self.tabControl).buttons()
        
        self.window.mainloop()
        
    # functions that change tab
    def openMenuTab(self):
        self.tabControl.select(self.menuTab)
    def openJsonTab(self):
        self.tabControl.select(self.jsonTab)
    def openAnnotationTab(self):
        self.tabControl.select(self.annotationTab)
    def openFolderTab(self):
        self.tabControl.select(self.folderTab)


    def btn_clicked(self):
        print("Button Clicked")


    # Image folder location popup window
    def inputLocation(self):
        inputName = filedialog.askdirectory(initialdir="/", title="Select Image Folder")     #full input directory name, inputted when you click button and select a folder

        # to deal with the fact megadetector code struggle with absolute image path names
        splitName = inputName.split(sep="/")
        self.inputName_dir = ""
        for folder in splitName[0:len(splitName) - 1]:
            self.inputName_dir += folder + "/"
        self.inputName_finalfolder = splitName[len(splitName) - 1]
        self.btn_input['text'] = self.inputName_dir + self.inputName_finalfolder



    #VALID ENTRY CHECKS
        
    # check if between 0 and 1
    def check_01(self,entry):
        try:
            entry=float(entry)
            if entry>=0 and entry<=1:
                return True
            else:
                return False
        except:
            if entry == "":
                return True
            return False

    # check if integer
    def check_int(self,entry):
        try:
            int(entry)
            return True
        except:
            if entry == "":
                return True
            return False


    #ENTRY TABS
    
    # STRING ENTRY (enter name of JSON)
    def entry0_func(self,Tab, entry_img, xpos, ypos):

        entry_bg = Label(Tab, image=entry_img, bg="#FFBAA2")
        entry = Entry(Tab, bd=0, bg="#ffffff", highlightthickness=0, fg="#999eb1", font=("Roboto", 16), justify="center", text="hi")
        entry.place(x=xpos, y=ypos, width=512.0, height=42)
        entry_bg.place(x=xpos-12, y=ypos-10)
        return entry, Tab


    # FLOAT ENTRY (confidence threshold entry)
    def entry1_func(self,Tab, entry_img, xpos, ypos):

        entry_bg = Label(Tab, image=entry_img, bg="#FFBAA2")
        entry = Entry(Tab, bd=0, bg="#ffffff", highlightthickness=0, fg="#999eb1", font=("Roboto", 16), justify='center')
        entry.place(x=xpos, y=ypos, width=100.0, height=40)
        entry_bg.place(x=xpos-16, y=ypos-2)
        reg = Tab.register(self.check_01)
        entry.config(validate="key", validatecommand=(reg, '%P'))
        return entry, Tab

    # INTEGER ENTRY (enter checkpoint frequency, number of cores)
    def entry2_func(self,Tab, entry_img, xpos, ypos):

        entry_bg = Label(Tab, image=entry_img, bg="#FFBAA2")
        entry = Entry(Tab, bd=0, bg="#ffffff", highlightthickness=0, fg="#999eb1", font=("Roboto", 16), justify='center')
        entry.place(x=xpos, y=ypos, width=100.0, height=40)
        entry_bg.place(x=xpos-16, y=ypos-2)
        reg = Tab.register(self.check_int)
        entry.config(validate="key", validatecommand=(reg, '%P'))
        return entry, Tab


    # creates widgets
    def progress_bar(self, Tab):
        # creates progress bar, percentage, image numbers, times and speed in GUI
        bar = ttk.Progressbar(Tab, orient=HORIZONTAL, length=820)
        percentage = Label(Tab, text="0%", bg="#FFBAA2", fg="#FFFFFF", font=("Roboto", 12))
        imageNumber = Label(Tab, text="Processed: 0 of 0", bg="#FFBAA2", fg="#FFFFFF", font=("Roboto", 12))
        duration = Label(Tab, text="Duration: HH:MM:SS", bg="#FFBAA2", fg="#FFFFFF", font=("Roboto", 12))
        estimated = Label(Tab, text="Estimated: HH:MM:SS", bg="#FFBAA2", fg="#FFFFFF", font=("Roboto", 12))
        iterationSpeed = Label(Tab, text="@", bg="#FFBAA2", fg="#FFFFFF", font=("Roboto", 12))

        # places the widgets
        bar.place(x=107, y=936, height=36)
        percentage.place(x=107, y=980)
        imageNumber.place(x=107, y=1000)
        duration.place(x=300, y=980)
        estimated.place(x=300, y=1000)
        iterationSpeed.place(x=300, y=1020)

        return Tab, bar, percentage, imageNumber, duration, estimated, iterationSpeed

       # opens subprocess to run detector script and show progress
    def Run(self):
        # "python -u" forces output to be unbuffered (each line outputted immediately)
        # command used to run detector script

        os.chdir(self.inputName_dir)
        command = self.make_command()

        # opens a subprocess with command while GUI still runs
        process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.myTab, bar, percentage, imageNumber, duration, estimated, iterationSpeed = self.progress_bar(self.myTab)

        # .poll() is used to check if subprocess is outputting data
        while True:
            output = process.stderr.readline()
            # if no output
            if output == '' and process.poll() is not None:
                break
            # if output is detected
            if output:
                # removes all whitespaces from output
                consoleOut = output.strip()
                try:
                    # separate all output into a list format: "[hello, world]"
                    splitUp = consoleOut.split()

                    # extracts the progress percentage to confirm that the script is working
                    percent = re.findall("\d+", splitUp[0])[0]

                    # if a percentage is found, we can output to GUI
                    if int(percent) <= 100:

                        # format is "current/total", so findall is used to look for integers on either side of "/"
                        # extracts the current image number & corrects starting image number 0 to 1
                        currentImage = int((re.findall("(\d+)/", splitUp[2]))[0]) + 1
                        totalImage = int((re.findall("/(\d+)", splitUp[2]))[0])

                        # recalculates the percentage based on the corrected starting image number -> "{0:.1f}" is 1dp
                        percent = float("{0:.1f}".format(float((currentImage/totalImage)*100)))

                        # extracts the current time and estimated time
                        # format is "current<estimated", so findall is used to look for strings on either side of "<"
                        # "[:-1]" removes an unwanted character from the end and "[1:]" omits a character form start
                        finishTime = re.findall("(?<=<).*", splitUp[3][:-1])
                        currentTime = re.findall("(.*?)<", splitUp[3][1:])

                        # iterations per second is extracted ("[:-1]" removes an unwanted character from the end)
                        iterations = splitUp[4][:-1]

                        # widgets are updated with new values
                        bar['value'] = int(percent)
                        percentage['text'] = bar['value'], "%"
                        imageNumber['text'] = "Processed:", currentImage, "of", totalImage
                        duration['text'] = "Duration:", currentTime
                        estimated['text'] = "Estimated:", finishTime
                        iterationSpeed['text'] = "@", iterations

                # if script hasn't started processing images do not output to GUI
                except:
                    print("")





class MENU_Tab(MD_GUI):
    def __init__(self, window, menuTab, jsonTab, annotationTab,folderTab, tabControl):
        MD_GUI.__init__(self, window)
        self.tabControl, self.menuTab, self.jsonTab, self.annotationTab, self.folderTab =tabControl, menuTab, jsonTab, annotationTab, folderTab
        
    def make_tabs(self):
        # MENU TAB Widgets
        # Quit Button
        btn_quit = Button(self.menuTab, image=self.img_quit, borderwidth=0, highlightthickness =0, command=quit, relief="flat")
        btn_quit.place(x=1773, y=23, width=120, height=45)

        # Sort into folders Tab
        btn_sort = Button(self.menuTab, image=self.img_sort, borderwidth=0, highlightthickness=0, command=self.openFolderTab, relief="flat")
        btn_sort.place( x=824, y=-18, width=270, height=67)

        # Annotate Tab
        btn_annotate = Button(self.menuTab, image=self.img_annotate, borderwidth=0, highlightthickness=0, command=self.openAnnotationTab, relief="flat")
        btn_annotate.place( x=517, y=-10, width=270, height=59)

        # Json Tab
        btn_json = Button(self.menuTab, image=self.img_json, borderwidth=0, highlightthickness=0, command=self.openJsonTab, relief="flat")
        btn_json.place( x=209, y=-18, width=270, height=67)

        return self.menuTab, self.tabControl








class JSON_Tab(MD_GUI):      #inherited class
    def __init__(self,window, menuTab, myTab, annotationTab, folderTab, tabControl):
        MD_GUI.__init__(self, window)
        self.tabControl, self.menuTab, self.myTab, self.annotationTab, self.folderTab =tabControl, menuTab, myTab, annotationTab, folderTab

        self.img_create = PhotoImage(file=f"createJson.png")
        
        self.scriptName = "\\Resources\\CameraTraps\\detection\\run_tf_detector_batch.py"                #location of JSON file creation script              
        self.inputName_dir=""               #created later
        self.inputName_finalfolder = ""     #created later
        self.detectorName = "\\Resources\\md_v4.1.0.pb"                  #location of megadetector pb
    
    # JSON TAB Widgets
    def buttons(self):
        
        # get image input location
        self.btn_input = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.inputLocation, text="", compound="center", bg="#FFBAA2", activebackground="#FFBAA2", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_input.place(x=100, y=362, width=528, height=57)

        # get json location
        self.b5 = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.JSONLocation, text="", compound="center", bg="#FFBAA2", activebackground="#FFBAA2", font=("Roboto", 16), fg="#999eb1")
        self.b5.place(x=100, y=505, width=528, height=57)

        # create file button
        self.b6 = Button(self.myTab, image=self.img_create, borderwidth=0, highlightthickness=0, command=threading.Thread(target=self.Run).start, relief="flat", bg="#FFBAA2", activebackground="#FFBAA2")
        self.b6.place(x=100, y=757, width=321, height=67)

        # home tab button
        self.b10 = Button(self.myTab, image=self.img_home, borderwidth=0, highlightthickness=0, command=self.openMenuTab, relief="flat")
        self.b10.place(x=42, y=-13, width=133, height=62)

        # annotations button
        self.b9 = Button(self.myTab, image=self.img_annotate, borderwidth=0, highlightthickness=0, command=self.openAnnotationTab, relief="flat")
        self.b9.place(x=516, y=-13, width=270, height=62)

        # sort tab button
        self.b8 = Button(self.myTab, image=self.img_sort, borderwidth=0, highlightthickness=0, command=self.openFolderTab, relief="flat")
        self.b8.place(
            x=824, y=-18,
            width=270,
            height=67)
        
        # quit button
        self.b7 = Button(self.myTab, image=self.img_quit, borderwidth=0, highlightthickness=0, command=quit, relief="flat")
        self.b7.place( x=1773, y=23, width=120, height=45)


        # select checkpoint file, resume from checkpoint
        self.b11 = Button(self.myTab, image=self.img_slct_small, borderwidth=0, highlightthickness=0, command=self.CheckpointLocation, text="", compound="center", bg="#FFBAA2", activebackground="#FFBAA2", font=("Roboto", 16), fg="#999eb1", relief="flat")
        self.b11.place(x=1564, y=790, width=285, height=45)

        # checkbox buttons
        # on json tab, output relative filenames
        #self.var_relFileNames = BooleanVar()

        #option_yes = tk.Radiobutton(self.myTab, variable=self.var_relFileNames, value=False, bg="#FFFFFF")
        #option_yes.place(x=1561, y=569, width=30, height=30)
        #option_no = tk.Radiobutton(self.myTab, variable=self.var_relFileNames, value=True, bg="#FFFFFF")
        #option_no.place(x=1635, y=569, width=30, height=30)


        self.threshEntry, self.myTab = self.entry1_func(self.myTab, self.img_enter_small, 1580.0, 584)
        self.checkFreqEntry, self.myTab = self.entry2_func(self.myTab, self.img_enter_small, 1580.0, 680)
        self.NcoresEntry, self.myTab = self.entry2_func(self.myTab, self.img_enter_small, 1580.0, 882)
        self.entry0, self.myTab = self.entry0_func(self.myTab, self.img_enter_name, 110.0, 636)

        return self.myTab, self.tabControl


    # JSON location popup window
    def JSONLocation(self):
        JSONDirectory = filedialog.askdirectory(initialdir="/", title="Select JSON location")
        self.b5['text'] = JSONDirectory
    
    # Checkpoint location popup window
    def CheckpointLocation(self):
        CheckpointDir=filedialog.askopenfilename(initialdir="/",title ="Select Checkpoint file (.json format)", filetypes=[(".JSON",".json")])
        self.b11['text'] = CheckpointDir


    # creates command line for creating JSON file
    def make_command(self):
        jsonInput = self.b5['text'] + "/" + self.entry0.get() + ".json"
        command = ["python", "-u", self.main_path+self.scriptName, self.main_path+self.detectorName, self.inputName_finalfolder, jsonInput, "--recursive"]

        #optional arguments
        #relativeFilenameArg = "--output_relative_filenames"
        #if self.var_relFileNames.get() == True:
        #    command.append(relativeFilenameArg)

        threshArg = '--threshold'
        if self.threshEntry.get() != "":   # in entry functions
          command.append(threshArg)
          command.append(self.threshEntry.get())

        checkFreqArg = '--checkpoint_frequency'
        if self.checkFreqEntry.get() != "":   # in entry functions
            command.append(checkFreqArg)
            command.append(self.checkFreqEntry.get())

        resumeCheckArg = '--resume_from_checkpoint'
        if self.b11['text'] != "":
            command.append(resumeCheckArg)
            command.append(self.b11['text'])

        NcoresArg = '--ncores'
        if self.NcoresEntry.get() != "":
            command.append(NcoresArg)
            command.append(self.NcoresEntry.get())

        print(command)
        return command






class ANNOTATE_Tab(MD_GUI):       #inherited class
    def __init__(self,window, menuTab, jsonTab, myTab, folderTab, tabControl):
        MD_GUI.__init__(self, window)
        self.tabControl, self.menuTab, self.jsonTab, self.myTab, self.folderTab =tabControl, menuTab, jsonTab, myTab, folderTab

        self.img_run_annotation = PhotoImage(file=f"annotate.png")
        
        self.visualizerName = "\\Resources\\CameraTraps\\visualization\\visualize_detector_output.py"    #location of visualizer script
        self.inputName_dir=""               #created later
        self.inputName_finalfolder = ""     #created later
        self.outputName = ""            #location of where to put the images that have visualizers on them

    def buttons(self):
        # Annotations Tabs

        # Quit button
        self.b12 = Button(self.myTab, image=self.img_quit, borderwidth=0, highlightthickness=0, command=quit, relief="flat")
        self.b12.place(x=1773, y=23, width=120, height=45)

        # Sort Folder Tab
        self.b13 = Button(self.myTab, image=self.img_sort, borderwidth=0, highlightthickness=0, command=self.openFolderTab, relief="flat")
        self.b13.place(x=824, y=-18, width=270, height=67)

        # Home Tab
        self.b14 = Button(self.myTab, image=self.img_home, borderwidth=0, highlightthickness=0, command=self.openMenuTab, relief="flat")
        self.b14.place(x=42, y=-13, width=133, height=62)

        # JSON Tab
        self.b15 = Button(self.myTab, image=self.img_json, borderwidth=0, highlightthickness=0, command=self.openJsonTab, relief="flat")
        self.b15.place(x=209, y=-18, width=270, height=67)


        # Annotations widgets
        # Save location
        self.btn_SaveDir = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.SaveLocation, relief="flat", text="", compound="center", bg="#FFBAA2", activebackground="#FFBAA2", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_SaveDir.place(x=100, y=576, width=530, height=60)

        # JSON input
        self.btn_json = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.JSONLocation, relief="flat", text="", compound="center", bg="#FFBAA2", activebackground="#FFBAA2", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_json.place(x=100, y=434, width=530, height=60)

        # Name input
        self.btn_input = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.inputLocation, relief="flat", text="", compound="center", bg="#FFBAA2", activebackground="#FFBAA2", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_input.place(x=100, y=294, width=530, height=60)

        # Annotate Button
        self.b19 = Button(self.myTab, image=self.img_run_annotation, borderwidth=0, highlightthickness=0, command=threading.Thread(target=self.Run).start, relief="flat", bg="#FFBAA2", activebackground="#FFBAA2")
        self.b19.place(x=100, y=710, width=321, height=69)

        # Annotation Name Input
        self.entrySeed, self.myTab = self.entry2_func(self.myTab, self.img_enter_small, 1580, 866)
        self.entryWidth, self.myTab = self.entry2_func(self.myTab, self.img_enter_small, 1580, 780)
        self.entrySize, self.myTab = self.entry2_func(self.myTab, self.img_enter_small, 1580, 696)
        self.entryThresh, self.myTab = self.entry1_func(self.myTab, self.img_enter_small, 1580, 590)

        return self.myTab, self.tabControl

    # JSON location popup window
    def JSONLocation(self):
        JSONDir=filedialog.askopenfilename(initialdir="/",title ="Select JSON file", filetypes=[(".JSON",".json")])
        self.btn_json['text'] = JSONDir

    def SaveLocation(self):
        SaveDir = filedialog.askdirectory(initialdir="/", title="Select Save location")
        self.btn_SaveDir['text'] = SaveDir

        # creates command line for creating JSON file
    def make_command(self):
        jsonInput = self.btn_json['text']
        SaveDirName = self.btn_SaveDir['text']
        command = ["python", "-u", self.main_path+self.visualizerName, jsonInput, SaveDirName,'--images_dir', self.inputName_dir]

        #optional arguments
        ThreshArg = "--confidence"
        if self.entryThresh.get() !="":
            command.append(ThreshArg)
            command.append(self.entryThresh.get())
            

        SizeArg = '--sample'
        if self.entrySize.get() != "":   # in entry functions
            command.append(SizeArg)
            command.append(self.entrySize.get())

        WidthArg = '--output_image_width'
        if self.entryWidth.get() != "":   # in entry functions
            command.append(WidthArg)
            command.append(self.entryWidth.get())

        SeedArg = '--random.seed'
        if self.entrySeed.get() != "":
            command.append(SeedArg)
            command.append(self.entrySeed.get())


        print(command)
        return command


class FOLDER_Tab(MD_GUI):
    def __init__(self,window, menuTab, jsonTab, annotationTab,myTab,  tabControl):
        MD_GUI.__init__(self, window)
        self.tabControl, self.menuTab, self.jsonTab, self.annotationTab, self.myTab = tabControl, menuTab, jsonTab, annotationTab, myTab
        self.img_run_annotation = PhotoImage(file=f"annotate.png")

        self.sepfolderCodeName = "\\Resources\\CameraTraps\\api\\batch_processing\\postprocessing\\separate_detections_into_folders.py"      #locatin of separating folders script

        self.img_selectFolder = PhotoImage(file = f"selectFolder.png")
        self.img_sort = PhotoImage(file = f"sortFolder.png")
        
    def buttons(self):
        # Quit Button
        b20 = Button(self.myTab, image=self.img_quit, borderwidth=0, highlightthickness=0, command=quit, relief="flat",)
        b20.place(x=1773, y=23, width=120, height=45)

        # Home Tab Button
        b21 = Button(self.myTab, image=self.img_home, borderwidth=0, highlightthickness=0, command=self.openMenuTab, relief="flat")
        b21.place(x=42, y=-16, width=133, height=65)

        # Annotations Tab Button
        b22 = Button(self.myTab, image=self.img_annotate, borderwidth=0, highlightthickness=0, command=self.openAnnotationTab, relief="flat")
        b22.place(x=516, y=-13, width=270, height=62)

        # JSON Tab Button
        b23 = Button(self.myTab, image=self.img_json, borderwidth=0, highlightthickness=0, command=self.openJsonTab, relief="flat")
        b23.place(x=208, y=-13, width=270, height=62)

        # Folder For Selected Images
        self.btn_SaveDir = Button(self.myTab, image=self.img_selectFolder, borderwidth=0, highlightthickness=0, command=self.SaveLocation, relief="flat", bg="#FFBAA2", activebackground="#FFBAA2", text="", compound="center",  font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_SaveDir.place(x=100, y=628, width=758, height=59)

        # Folder Containing Images
        self.btn_input = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.inputLocation, relief="flat", bg="#FFBAA2", activebackground="#FFBAA2", text="", compound="center", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_input.place(x=100, y=330, width=758, height=59)

        # JSON File Location
        self.btn_json = Button(self.myTab, image=self.img_folder_select, borderwidth=0, highlightthickness=0, command=self.JSONLocation, relief="flat", bg="#FFBAA2", activebackground="#FFBAA2", text="", compound="center", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.btn_json.place(x=100, y=482, width=758, height=59)

        # Sort Button, RUN
        self.b27 = Button(self.myTab, image=self.img_sort, borderwidth=0, highlightthickness=0, command=threading.Thread(target=self.Run).start, relief="flat", bg="#FFBAA2", activebackground="#FFBAA2", text="", compound="center", font=("Roboto", 16), fg="#999eb1", anchor="w")
        self.b27.place(x=100, y=756, width=321, height=72)

        # Optional Sorting Entries
        self.entryAnimal, self.myTab = self.entry1_func(self.myTab, self.img_enter_small, 1475, 527)
        self.entryVehicle, self.myTab = self.entry1_func(self.myTab, self.img_enter_small, 1475, 615)
        self.entryHuman, self.myTab = self.entry1_func(self.myTab, self.img_enter_small, 1475, 700)
        self.entryThreads, self.myTab = self.entry2_func(self.myTab,self.img_enter_small, 1475, 800)

        # Checkbox Buttons
        # Allow Existing Directory
        self.var_ExistingDirectory = BooleanVar()
        option_directory_yes = tk.Radiobutton(self.myTab, variable=self.var_ExistingDirectory, value=False, bg="#FFFFFF")
        option_directory_yes.place(x=1478, y=926, width=20, height=20)
        option_directory_no = tk.Radiobutton(self.myTab, variable=self.var_ExistingDirectory, value=True, bg="#FFFFFF")
        option_directory_no.place(x=1559, y=926, width=20, height=20)

        return self.myTab, self.tabControl

        # JSON location popup window
    def JSONLocation(self):
        JSONDir=filedialog.askopenfilename(initialdir="/",title ="Select JSON file", filetypes=[(".JSON",".json")])
        self.btn_json['text'] = JSONDir

    def SaveLocation(self):
        SaveDir = filedialog.askdirectory(initialdir="/", title="Select Save location")
        self.btn_SaveDir['text'] = SaveDir

            # creates command line for creating JSON file
            
    def make_command(self):
        jsonInput = self.btn_json['text']
        SaveDirName = self.btn_SaveDir['text']
        command = ["python", "-u", self.main_path+self.sepfolderCodeName, jsonInput, self.inputName_dir,SaveDirName ]

        #optional arguments
        animalArg = "--animal_threshold"
        if self.entryAnimal.get() !="":
            command.append(ThreshArg)
            command.append(self.entryAnimal.get())
            

        vehicleArg = '--vehicle_threshold'
        if self.entryVehicle.get() != "":   # in entry functions
            command.append(vehicleArg)
            command.append(self.entryVehicle.get())

        humanArg = '--human_threshold'
        if self.entryHuman.get() != "":   # in entry functions
            command.append(humanArg)
            command.append(self.entryHuman.get())

        threadsArg = '--n_threads'
        if self.entryThreads.get() != "":
            command.append(threadsArg)
            command.append(self.entryThreads.get())

        relativeFilenameArg = "--allow_existing_directory"
        if self.var_ExistingDirectory.get() == False:
            command.append(relativeFilenameArg)


        print(command)
        return command

    


#MAIN

window = tk.Tk()               #window
WINDOW = MD_GUI(window)
WINDOW.create()






