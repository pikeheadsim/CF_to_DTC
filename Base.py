#
#
import os
import sys
import json
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog as fd
import FA18


#base class, the one talking to DCS and loading and saving files
class base:
    
    #   *************  set default values for the class variables. *************
    path_run = "./" #running path.
    flights_dic={}   #diccionary with the flights, keys are the callsigns.
    flights_calls=[""] #list of fight callsigns.

    input_filename="" #input filenam, should exported for combatflite in XML.
    base_filename=""  #filename without extension.
    number_flights=0  #total number of flights in the combatflite file. 

    T=""
    plane=""
    string_variable=""
    save_dtc_files=True
    
    precise=True    
    FA18_inst = FA18.FA18()
    
    @property
    def sprecise(self):
        return self.precise
    
    @sprecise.setter
    def sprecise(self, value):
        self.precise=value
        self.FA18_inst.precise=self.precise

    SaveFiles=True
    def update_status(self, prst=False):
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
        self.convert(prst)
        return True

     # ************* function to select the  input file ************* 
    def select_file(self):
        filetypes = (('CombatFlite (xml)', '*.xml'),('All files', '*.*'))
        old=self.input_filename
        self.input_filename = fd.askopenfilename(title='Open a file',initialdir=self.path_run, filetypes=filetypes)
        if self.input_filename == "":
            self.input_filename = old
            return False
        
        self.input_file = ET.parse(self.input_filename)
        self.update_status(True)
        return True
    # ************* convert coords in degrees to deg, min, sec *************
    def from_decimal_dms(self,val, ck=True):
        dec = abs(float(val))
        deg = int(dec)
        minrest = (dec - deg)*60
        minutes = int(minrest)
        if self.precise and ck:
            decmin = round((minrest - minutes)*10000)
            if decmin == 10000:
                minutes += 1
                decmin = 0
                if minutes == 60:
                    deg += 1
                    minutes=0
            output = str(deg).zfill(2) + "." + str(minutes).zfill(2)+"."+str(decmin).zfill(4)
        else:
            decmin = round((minrest - minutes)*100)
            if decmin == 100:
                minutes += 1
                decmin = 0
                if minutes == 60:
                    deg += 1
                    minutes=0
            output = str(deg).zfill(2) + "." + str(minutes).zfill(2)+"."+str(decmin).zfill(2)
        return output
    # ************* sets the wp in the DCS-DTC format *************
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
    
        return flight_name,{'Sequence': idx, 'Name': wp_name, 'Latitude': "N "+ self.from_decimal_dms(Lat,ck), 'Longitude': long_dir + self.from_decimal_dms(Lon,ck), 'Elevation': int(float(Ele)*3.28084), 'Blank': False}



    def convert(self,prstatus=True):
        ''' Converts every flight in a dicctionary of waypoints that can be 
        send to a json files compatible with DCS-DTC or save it for later upload 
        the info in the plane. T is the window text box used to give feedback to 
        the user. '''
        
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
        if prstatus:
            self.T.configure(state='normal')
            #self.T.delete('0.0', tk.END)
            text = str(self.number_flights)+" Flights found" + heather + "\n"+"  Callsign" + (len(heather)-10)*" "+"Num Wps\n  "
            text += (len(heather)+5)*"-"
            text += string_flights + "\n" + len(heather)*"*" + "\n\n"
            self.T.insert("1.0",text)
            self.T.configure(state='disabled')

    # ************* makes the sequence of commands *************
    def create_clicks(self,flight_name):
        wplist=self.flights_dic[flight_name]
        if self.plane == "F/A-18":
            return self.FA18_inst.BuildWPCommands(wplist)

    # ************* updates to DCS using the port 43001 *************
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
        

      
