import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import config_handler
import text_processor
import text_processor_2



class LexGUI:



    def __init__(self, win):
    	self.master = win
    	



    def createTabs(self):
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [40, 10],
                                        "font" : ('URW Gothic L', '11', 'bold')},}})
        s.theme_use("MyStyle")
        s.configure('TButton', relief='raised', padding= 6)
        

        self.tabControl = ttk.Notebook(self.master)
        
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        #self.tab3 = ttk.Frame(self.tabControl)
        #self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Lower Case')
        self.tabControl.add(self.tab2, text = 'Normal Case')      
        #self.tabControl.add(self.tab3, text = 'Settings')
        #self.tabControl.add(self.tab4, text = 'Upload')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/TEXT", 
            title = "Select a clean text", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename):
            self.filepath.set(self.filename) #set the textbox to the file path
            #self.button2.config(state = "normal")
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE,self.filename)

    def dirDialog(self):
        self.filename2 = filedialog.askdirectory()
        if (self.filename2):
            self.filepath2.set(self.filename2) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR,self.filename2)
    
    def processText(self):
        if(self.filepath2.get() and self.filepath31.get()):
            text_processor.processText(self.filepath31.get(), self.filepath2.get())
        else:
            messagebox.showwarning("Error", "Missing input file or output directory")
   
    def createTab1(self):
        #frame

        self.labelFrame = ttk.LabelFrame(self.tab1, text= 'Select Input Folder:')
        self.labelFrame.grid(column=0, row=0, padx = 20, pady = 20)
        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)

   
        #textbox 31
        self.filepath31 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR3)
        self.filepath31.set(value) 
        self.path31 = ttk.Entry(self.labelFrame, width=90, 
            textvariable = self.filepath31)
        self.path31.grid(column = 0, row = 1, sticky = "w")
        


        #button 31
        self.button31 = ttk.Button(self.labelFrame, text = "Browe Directory", 
            command=self.dirDialog3)
        self.button31.grid(column = 1, row = 1, sticky = "w")


        #label 31
        self.label31 = ttk.Label(self.labelFrame, text="Select Output Folder:")
        self.label31.grid(column = 0, row = 2, sticky = "w")

        #textbox
        self.filepath = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE)
        self.filepath.set(value)

        
       #textbox 2
        self.filepath2 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR)
        self.filepath2.set(value) 
        self.path2 = ttk.Entry(self.labelFrame, width=90, textvariable = self.filepath2)
        self.path2.grid(column = 0, row = 3, sticky = "w")
        

        #button 3
        self.button3 = ttk.Button(self.labelFrame, text = "Browse Directory", command=self.dirDialog)
        self.button3.grid(column = 1, row = 3, sticky = "w")

    
       
        #button no 5
        self.button5 = ttk.Button(self.labelFrame, text = "START PROCESS", command=self.processText)
        self.button5.grid(column = 0, row = 5)


    def fileDialog2(self):
        self.filename21 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/SENTENCE", 
            title = "Select a JSON file", filetypes = (("JSON files", "*.json"),  ("all files", "*.*")))
        if (self.filename21):
            self.filepath21.set(self.filename21) #set the textbox to the file path
            #self.button2.config(state = "normal")
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE2,self.filename21)

    

    def dirDialog2(self):
        self.filename21 = filedialog.askdirectory()
        if (self.filename21):
            self.filepath21.set(self.filename21) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR2,self.filename21)

    def dirDialog4(self):
        self.filename22 = filedialog.askdirectory()
        if (self.filename22):
            self.filepath22.set(self.filename22) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR4,self.filename22)        

    def processText2(self):
        if(self.filepath21.get() and self.filepath22.get()):
            text_processor.processText2(self.filepath21.get(), self.filepath22.get())
        else:
            messagebox.showwarning("Error", "Missing input or output directory")

    def createTab2(self):
        #frame

        self.labelFrame2 = ttk.LabelFrame(self.tab2, text= 'Select an Input Folder:')
        self.labelFrame2.grid(column=0, row=0, padx = 20, pady = 20)

  
        #textbox 21
        self.filepath21 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR2)
        self.filepath21.set(value) 
        self.path21 = ttk.Entry(self.labelFrame2, width=90, 
            textvariable = self.filepath21)
        self.path21.grid(column = 0, row = 1, sticky = "w")
        

        #button 21
        self.button21 = ttk.Button(self.labelFrame2, text = "Browse Directory", 
            command=self.dirDialog2)
        self.button21.grid(column = 1, row = 1, sticky = "w")

        #label 22
        self.label31 = ttk.Label(self.labelFrame2, text="Select Output Folder:")
        self.label31.grid(column = 0, row = 2, sticky = "w")
    
        #textbox 22
        self.filepath22 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR4)
        self.filepath22.set(value) 
        self.path22 = ttk.Entry(self.labelFrame2, width=90, 
            textvariable = self.filepath22)
        self.path22.grid(column = 0, row = 3 , sticky = "w")
        

        #button 22
        self.button22 = ttk.Button(self.labelFrame2, text = "Browse Directory", 
            command=self.dirDialog4)
        self.button22.grid(column = 1, row = 3, sticky = "w")

        #button no 5
        self.button5 = ttk.Button(self.labelFrame2, text = "START PROCESS", command=self.processText2)
        self.button5.grid(column = 0, row = 5)



    def dirDialog3(self):
        self.filename31 = filedialog.askdirectory()
        if (self.filename31):
            self.filepath31.set(self.filename31) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR3,self.filename31)


        
    def createTab3(self):
        #frame

        self.labelFrame3 = ttk.LabelFrame(self.tab3, text= 'Select Input Directory:')
        self.labelFrame3.grid(column=0, row=0, padx = 20, pady = 20)


 


    def createGUI(self):
        self.createTabs()    
        self.createTab1()
        self.createTab2()
        #self.createTab3()
