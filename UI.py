import os
import sys
from tkinter import *
import FA18
import Base

col1 = "#e0e2e4"
col2 = "#c6bcb6"
col3 = "#96897f"
col4 = "#625750"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./")
 
    return os.path.join(base_path, relative_path)

bs=Base.base()
root = Tk()
root.title("CombatFlite to DTC")
bgcolor="#c6bcb6"
#path_run = os.path.dirname(sys.executable)
#path_run = os.path.dirname(__file__)
#root.iconbitmap(resource_path('Icon.ico'))

root.configure(bg=col2)
string_variable = StringVar(master=root, value="...xml file not selected...")
T = Text(root)
bs.T = T
T.insert(END, "No flights found")
T.configure(state='disabled',font=('Monospace', 12))

bs.plane="FA18"
bs.string_variable = string_variable

#root.rowconfigure(9)
#root.columnconfigure(15)

#for i in range(8):
#    root.grid_columnconfigure(i, minsize=30)
#    root.grid_rowconfigure(i, minsize=40)
      
root.grid_rowconfigure(0, minsize=10)
root.grid_columnconfigure(0, minsize=10)

# first label
Label(root,text="CombatFlite file exported in .xml:",
      bg=col2,font=('Monospace', 13)).grid(row=1,column=1,
                                              columnspan=4, rowspan=1)

root.grid_rowconfigure(1, minsize=10)
#root.grid_columnconfigure(1, minsize=10)

#text for the path
entry=Entry(root, textvariable=string_variable, width=88,font=('Monospace 10'),fg = "black")
entry.configure(state='disabled')
entry.grid(row=2,column=1,columnspan=11)

root.grid_rowconfigure(2, minsize=33)

#flights menu to be updated
variable = StringVar(root)
variable.set("No Flights") # default value
flightsmenu = OptionMenu(root, variable, "No Flights")
flightsmenu.config(width=9,height=1, bg=col3,activebackground=col4,font=('Monospace', 12))
flightsmenu.grid(row=4,column=1,rowspan=1, columnspan=3, sticky="nw")


def call_and_update():
#    file_loaded = 
    if not bs.select_file():
        return
    aux=flightsmenu["menu"]
    aux.delete(0,"end")
    if len(bs.flights_calls)>0:
        variable.set(bs.flights_calls[0])
    else:
        variable.set("No Flights")
    for string in bs.flights_calls:
            aux.add_command(label=string, 
                             command=lambda value=string: variable.set(value))
    

#load button to select the xml file
#image = PhotoImage(file = resource_path("./XMLButton.png"))
load_button = Button(text="Load File",font=('Monospace', 12),bg=col4, fg=col1,activebackground=col4,
                     command=call_and_update, width=8,height=1)
load_button.grid(row=3,column=1,columnspan=1,sticky="nw")

#set textbox
S = Scrollbar(root,orient=VERTICAL,command=T.yview)
S.grid(row=3,column=11,rowspan=10,ipady=75, sticky="ne")
S.config(command=T.yview)
T.configure(height=11, width=60, bg=col1,font=('Monospace', 12))
T.grid(row=3,column=4,rowspan=16, columnspan=6, sticky="ne")
root.grid_columnconfigure(12, minsize=15)

#flights menu to be updated
variable_plane = StringVar(root)
variable_plane.set("FA18") # default value
flightsmenu2 = OptionMenu(root, variable_plane, "FA18", "Not yet (F16C)", "Not yet (A10II)")
flightsmenu2.config(width=9,height=1, bg=col3,font=('Monospace', 12),activebackground=col4)#activeforeground=col4,)
flightsmenu2.grid(row=5,column=1,rowspan=1, columnspan=3, sticky="nw")

#Load all in the plane
def upload():
    bs.plane=variable_plane.get()
    try:
        bs.upload_plane(variable.get())
    except Exception as e:
        T.configure(state='normal')
        #T.delete('0.0', tk.END)
        #print(e)
        T.insert("1.0",str(e)+"\n")
        T.configure(state='disabled')        
    
image = PhotoImage(file = resource_path("upload.png"))
upload_button = Button(text="Upload!",font=('Monospace', 12),image=image,bg="black",activebackground=col4,
                       command=upload, width=120,height=120)

upload_button.grid(row=6,column=1,columnspan=2,sticky="nw")

root.grid_rowconfigure(6, minsize=140)


c_v1=IntVar()
c_v2=IntVar()
c_v1.set(0)
c_v2.set(1)

bs.SaveFiles=bool(c_v1.get())
bs.precise=bool(c_v2.get())

def checkbox_com():
    bs.SaveFiles=bool(c_v1.get())
    bs.update_status()
    print(bs.SaveFiles)
    
checkbox = Checkbutton(root, text="Save DTC (json)", command=checkbox_com, variable=c_v1)
checkbox.config(bg=col2,font=('Monospace', 12))
checkbox.grid(row=6,column=4,columnspan=2, rowspan=1, sticky="se")


def checkbox2_com():
    bs.precise=bool(c_v2.get())
    bs.update_status()
    print(bs.precise)



checkbox2 = Checkbutton(root, text="Precise Coord",command=checkbox2_com, variable=c_v2)
checkbox2.config(bg=col2,font=('Monospace', 12))
checkbox2.grid(row=6,column=6,columnspan=2, rowspan=1, sticky="se")


def show_wp():

#        self.flights_dic={}
#        self.flights_calls=[]

    T.configure(state='normal')


    T.insert("1.0","\n\n")
    #print(wpl)
    for i,fl in reversed(list(enumerate(bs.flights_dic[variable.get()]))):
        line = str(i)+ " -  " + fl["Name"] + " - "
        line += fl["Latitude"] + " -  "
        line += fl["Longitude"] + " -  "
        line += str(fl["Elevation"])
        print(line)
        T.insert("1.0",line+"\n")
    T.insert("1.0","# "+variable.get() + " ---  Num  -  Name  -  Lat  -  Lon  -  Elev  --------------\n")    
    T.configure(state='disabled')        
    



showwp_button = Button(text="Show Selected WP",font=('Monospace', 10),bg=col4, fg=col1,activebackground=col4,
                     command=show_wp, width=15,height=1)
showwp_button.grid(row=6,column=8,columnspan=4,sticky="se")
root.grid_rowconfigure(7, minsize=10)


root.mainloop()  
