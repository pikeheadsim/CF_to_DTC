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
Label(root,text="CombatFlite file exported in .xml file:",
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
    file_loaded = bs.select_file()
    if not file_loaded:
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
T.configure(height=11, width=50, bg=col1,font=('Monospace', 12))
T.grid(row=3,column=4,rowspan=16, columnspan=6, sticky="ne")


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
        T.insert(END,str(e))
        T.configure(state='disabled')        
    
image = PhotoImage(file = resource_path("upload.png"))
upload_button = Button(text="Upload!",font=('Monospace', 12),image=image,bg="black",activebackground=col4,
                       command=upload, width=120,height=120)

upload_button.grid(row=6,column=1,columnspan=2,sticky="nw")

#w.configure(text="Load File",font=('Monospace', 12),bg=col3,
 #                    command=bs.select_file, width=10,height=1)

#second label
# Label(root,text="Flights:",
#       bg=col2,font=('Monospace', 13)).grid(row=4,column=1,
#                                               columnspan=1, rowspan=1, sticky="nw")
# listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)
# listbox.grid(row=5,column=1,columnspan=1, rowspan=1, sticky="nw")

# root.grid_rowconfigure(1, minsize=85)
# entry=Entry(root, textvariable=string_variable, width=80)
# entry.configure(state='disabled')
# entry.grid(row=2,column=1,columnspan=5,sticky="n")

# S = Scrollbar(root,orient=VERTICAL,command=T.yview)
# S.grid(row=3,column=5,rowspan=1,ipady=40, sticky="ne")
# S.config(command=T.yview)
# T.grid(row=3,column=4,rowspan=1)

# image = tk.PhotoImage(file = resource_path("./ConvertButton.png"))
# button = Button(root, text="Select XML file", bg="#b9ab81", command=bs.select_file, image=image2, width=70,height=70)
# button.grid(row=1,column=1,sticky="n")

# image2 = tk.PhotoImage(file = resource_path("./XMLButton.png"))
# button2 = Button(text="Convert",font=('Arial', 20),bg="#b9ab81", command=bs.convert, image=image, width=120,height=120)
# button2.grid(row=3,column=1, columnspan=2,sticky="n")

#

#button3 = Button(text="push",font=('Arial', 20),bg="#b9ab81", command=test)
#button3.grid(row=4,column=1, columnspan=2,sticky="n")

#root.geometry("650x300")

#title_bar = Frame(root, bg="#b9ab81", relief='raised', bd=2)

#Label(root,text="Ouput files are saved in input-file folder", bg=bgcolor,font=('Arial', 10)).grid(row=4,column=3,columnspan=4, rowspan=1)



root.mainloop()  
