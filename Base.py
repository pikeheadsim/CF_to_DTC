#
#
import os
import sys
import json
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog as fd
import FA18

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./")
 
    return os.path.join(base_path, relative_path)


class base:
    
    #   *************  set default values for the class variables. *************
    path_run = "~/Dropbox/varis/DCS-DTC-3.3.0-RC12/beta01_mods/Beta0.1/" #running path.
    flights_dic={}   #diccionary with the flights, keys are the callsigns.
    flights_calls=[""] #list of fight callsigns.

    input_filename="" #input filenam, should exported for combatflite in XML.
    base_filename=""  #filename without extension.
    number_flights=0  #total number of flights in the combatflite file. 


    T=""
    plane=""
    string_variable=""
    save_dtc_files=True
    old_str=""

    precise=True
    SaveFiles=True

    def update_status(self):
    # ************* Reset values and paths to start again ************* 
        if self.input_filename == "":
            return False
        
        self.flights_dic={}
        self.flights_calls=[]

        # ************* set values paths and lists ************* 
        self.number_flights = len(self.input_file.findall("Waypoints"))
        self.string_variable.set(self.input_filename)
        self.path_run=os.path.dirname(self.input_filename)
        self.base_filename=os.path.basename(self.input_filename).split('.', 1)[0]
        self.convert()

    
    def select_file(self):
        filetypes = (('CombatFlite (xml)', '*.xml'),('All files', '*.*'))
        old=self.input_filename
        self.input_filename = fd.askopenfilename(title='Open a file',initialdir=self.path_run, filetypes=filetypes)
        if self.input_filename == "":
            self.input_filename = old
            return False
        
        self.input_file = ET.parse(self.input_filename)
        self.update_status()
        return True
    
    def from_decimal_dms(self,val, ck=True):
        ''' This funcitions transforms the decimal 
        value in degrees to (ex. N 34.54.3456) it can 
        be used with precision or standard (ex.34.54.34) '''

        dec = abs(float(val))
        deg = int(dec)
        minutes = int((dec - deg)*60)
        if self.precise and ck:
            sec = round((dec - deg - minutes/60.0)*360000)
            output = str(deg).zfill(2) + "." + str(minutes).zfill(2)+"."+str(sec).zfill(4)
        else:
            sec = round((dec - deg - minutes/60.0)*3600)
            output = str(deg).zfill(2) + "." + str(minutes).zfill(2)+"."+str(sec).zfill(2)
        return output
    
    def wp_to_DCTwp(self,w, idx, ck=True):
        '''Funciont that takes the info from the xml structure of the waypoint.'''
        flight_name = w.find("Name").text.split("\n")[0]
        wp_name    = w.find("Name").text.split("\n")[1]
        Lat   = w.find("Position").find("Latitude").text
        Lon   = w.find("Position").find("Longitude").text
        Ele   = w.find("Position").find("Altitude").text
    
        if float(Lon) < 0.0:
            long_dir="W "
        else:
            long_dir="E "
    
        return flight_name,{'Sequence': idx, 'Name': wp_name, 'Latitude': "N "+ self.from_decimal_dms(Lat,ck), 'Longitude': long_dir + self.from_decimal_dms(Lon,ck), 'Elevation': int(float(Ele)), 'Blank': False}



    def convert(self):
        ''' Converts every flight in a dicctionary of waypoints that can be 
        send to a json files compatible with DCS-DTC or save it for later upload 
        the info in the plane. T is the tkinter text box.'''
        
        #self.input_file = ET.parse(self.input_filename);
        flights = self.input_file.findall("Waypoints")
        string_flights=""
        heather = "\n***************  "+ self.base_filename[:19] + " ***************"
        print(self.path_run)
        for flight in flights: #loop on flights
            wplist=[]
            wplist_file=[]
            for idx,w in enumerate(flight):#loop on waypoints
                flight_name, wp_info = self.wp_to_DCTwp(w,idx+1)
                wplist.append(wp_info)
                _, wp_info = self.wp_to_DCTwp(w,idx+1,False)
                wplist_file.append(wp_info)
            if self.SaveFiles:
                with open(self.path_run + "\\"+self.base_filename+"_"+flight_name+'_DTC.json', 'w') as f:
                    json.dump({"Waypoints":{"Waypoints":wplist_file,"SteerpointStart":0,"EnableUpload":True},"Sequences":None,"PrePlanned":None,"Radios":None,"CMS":None,"Misc":None}, f)
                    
            string_flights +=  "\n     " +flight_name + ((len(heather)-10)//3)*" - " + str(len(wplist))
            self.flights_dic[flight_name]=wplist
            self.flights_calls.append(flight_name)

        self.T.configure(state='normal')
        #self.T.delete('0.0', tk.END)
        text = str(self.number_flights)+" Flights found" + heather + "\n"+"  Callsign" + (len(heather)-10)*" "+"Num Wps\n  "
        text += (len(heather)+5)*"-"
        text += string_flights + "\n" + len(heather)*"*" + "\n\n"
        self.T.insert("1.0",text+self.old_str)
        self.old_str= text + self.old_str
        self.T.configure(state='disabled')

    def create_clicks(self,flight_name):
        wplist=self.flights_dic[flight_name]
        if self.plane == "FA18":
            p=FA18.FA18()
        return p.BuildWPCommands(wplist)

    def upload_plane(self, selected_flight):
        ''' '''
        import socket
        host = "127.0.0.1" 
        port = 43001 
        commandtosend = self.create_clicks(selected_flight)
        commandtosend = commandtosend.replace("'","\"")
        commandtosend = "["+ commandtosend[:-1]+"]\n"
        print(host)
        #print(commandtosend2)
        s = socket.socket()#socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(str.encode(commandtosend,"ascii"))
        s.close()
        

      
