import os
import sys
from tkinter import *
import FA18
import Base

#The code is very simple and the user interface too

#colors 
col1 = "#e0e2e4"
col2 = "#c6bcb6"
col3 = "#96897f"
col4 = "#625750"


col2 = "#011f4b"
col4 = "#03396c"
col3 = "#005b96"
col2 = "#6497b1"
col5 = "#b3cde0" 

col1 = "#e0e2e4"
col4 = "#d0e1f9"
col3 = "#4d648d"
col2 = "#283655"



#pyinstaller stuff for the path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./")
 
    return os.path.join(base_path, relative_path)

bs=Base.base()                   #base class ( talks tod DCS, imports data, and exports data)
root = Tk()                      #window
root.title("CombatFlite to DTC")

#  path where the executable is running, all strats there. 
path_run = os.path.dirname(sys.executable)
bs.path_run = path_run
# path_run = os.path.dirname(__file__)

root.iconbitmap(resource_path('Icon.ico'))


root.configure(bg=col3)
string_variable = StringVar(master=root, value="...xml file not selected...")
T = Text(root)  #Text window
bs.T = T
T.tag_config('good', foreground="darkblue")
T.tag_config('good2', foreground="darkgreen")
T.tag_config('bad', foreground="darkred")
T.insert(END, "No flights yet...", "good2")
T.configure(state='disabled',font=('Monospace', 12))

#setting few default options to the base class (for now only FA18 is implemented)
bs.plane="FA18" 
bs.string_variable = string_variable

root.grid_rowconfigure(0, minsize=10)
root.grid_columnconfigure(0, minsize=10)
root.grid_columnconfigure(1, minsize=150)


# first label
Label(root,text="CombatFlite file:",
      bg=col3,font=('Monospace', 13, "bold")).grid(row=1,column=1,
                                              columnspan=2, rowspan=1)

root.grid_rowconfigure(1, minsize=10)

# settin the text for the path
entry=Entry(root, textvariable=string_variable, width=90,font=('Monospace 11'),fg = "black")
entry.configure(state='disabled', disabledforeground="darkred")
entry.grid(row=2,column=1,columnspan=11)

root.grid_rowconfigure(2, minsize=33)

# flights menu
variable = StringVar(root)
variable.set("No Flights") # default value
flightsmenu = OptionMenu(root, variable, "No Flights")
flightsmenu.config(width=9,height=1, bg=col2,activebackground=col4,font=('Monospace', 12))
flightsmenu.grid(row=4,column=1,rowspan=1, columnspan=3, sticky="nw")

def menucom(value ):
    variable.set(value)
    T.configure(state='normal')
    T.insert("1.0", "   .... Fligth "+value+" loaded .... \n\n",  "good")
    T.configure(state='disabled')        
    
#main function that opens the xml file, read the data and updates menus, 
#called with the button load    
def call_and_update():
    if not bs.select_file():
        #entry.configure(state='disabled', disabledforeground="darkred")
        return
    else:
        entry.configure(state='readonly', disabledforeground="darkblue")
        aux=flightsmenu["menu"]
        aux.delete(0,"end")
        if len(bs.flights_calls)>0:
            variable.set(bs.flights_calls[0])
        else:
            variable.set("No Flights")
        for string in bs.flights_calls:
            aux.add_command(label=string, 
                            command=lambda value=string: menucom(value))
    

#load button to select the xml file
load_button = Button(text="Load File",font=('Monospace', 12),bg=col2,activebackground=col4,fg="#ffffff",
                     command=call_and_update, width=8,height=1)
load_button.grid(row=3,column=1,columnspan=1,sticky="nw")

#set properties textbox
S = Scrollbar(root,orient=VERTICAL,command=T.yview)
S.grid(row=3,column=11,rowspan=10,ipady=75, sticky="ne")
root.grid_columnconfigure(11, minsize=20)
S.config(command=T.yview)
T.configure(height=11, width=60, bg=col1,font=('Monospace', 12),yscrollcommand=S.set)
T.grid(row=3,column=4,rowspan=16, columnspan=6, sticky="ne")
root.grid_columnconfigure(12, minsize=15)

#airplanes menu, not much related with that yet
variable_plane = StringVar(root)
variable_plane.set("FA18") # default value
flightsmenu2 = OptionMenu(root, variable_plane, "FA18", "Not yet (F16C)", "Not yet (A10II)")
flightsmenu2.config(width=9,height=1, bg=col2,font=('Monospace', 12),activebackground=col4)#activeforeground=col4,)
flightsmenu2.grid(row=5,column=1,rowspan=1, columnspan=3, sticky="nw")

#upload all the info in the plane
def upload():
    bs.plane=variable_plane.get()
    try:
        bs.upload_plane(variable.get())
    except Exception as e:
        T.configure(state='normal')
        T.insert("1.0",str(e)+"\n\n", "bad")
        T.configure(state='disabled')        

#upload button
image = PhotoImage(file = resource_path("upload.png"))
upload_button = Button(text="Upload!",font=('Monospace', 12),image=image,bg="black",activebackground=col5,
                       command=upload, width=120,height=120)

upload_button.grid(row=6,column=1,columnspan=2,sticky="nw")

root.grid_rowconfigure(6, minsize=140)

#Checkboxes to save DCS-DTC files and use precise coordinates
c_v1=IntVar()
c_v2=IntVar()
c_v1.set(0)
c_v2.set(1)

bs.SaveFiles=bool(c_v1.get())
bs.sprecise=bool(c_v2.get())

def checkbox_com():
    bs.SaveFiles=bool(c_v1.get())   
    if bs.update_status():
        entry.configure(state='readonly', disabledforeground="darkblue")
    else:
        entry.configure(state='disabled', disabledforeground="darkred")     
    bs.update_status()
    

checkbox = Checkbutton(root, text="Save DTC (json)", command=checkbox_com, variable=c_v1)
checkbox.config(bg=col3,activebackground=col3,font=('Monospace', 12))
checkbox.grid(row=6,column=4,columnspan=2, rowspan=1, sticky="se")

def checkbox2_com():
    bs.sprecise=bool(c_v2.get())
    if bs.update_status():
        entry.configure(state='readonly', disabledforeground="darkblue")
    else:
        entry.configure(state='disabled', disabledforeground="darkred")
    bs.update_status()

checkbox2 = Checkbutton(root, text="Precise Coord",command=checkbox2_com, variable=c_v2)
checkbox2.config(bg=col3,activebackground=col3,font=('Monospace', 12))
checkbox2.grid(row=6,column=6,columnspan=2, rowspan=1, sticky="se")


# Funcition and button to print the wayponts that are part of the selected flight

def show_wp():
    T.configure(state='normal')
    T.insert("1.0","\n\n")

    for i,fl in reversed(list(enumerate(bs.flights_dic[variable.get()]))):
        line =   " -- "
        line += fl["Latitude"] + "  --  "
        line += fl["Longitude"] + "  --  "
        line += str(fl["Elevation"])

        T.insert("1.0",line)
        T.insert("1.0", "\n"+ str(i)+" --  " + fl["Name"] , "bad")
    #T.insert("1.0", "# -- Num  --  Name  --  Lat  --  Lon  --  Elev  ---", "good")
    T.insert("1.0","# Flight Name:  -- "+variable.get()+"\n","good2")
    T.configure(state='disabled')        
  

showwp_button = Button(text="Show Selected Flight",font=('Monospace', 11),bg=col4, fg=col1,
                       activebackground=col4,command=show_wp, width=17,height=1)
showwp_button.grid(row=6,column=8,columnspan=4,sticky="se")
root.grid_rowconfigure(7, minsize=10)

root.mainloop()  
