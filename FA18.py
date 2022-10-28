

class FA18:
    Dev={}
    Com={}
    
    wait = "{'device':'wait', 'delay': 200},"
    waitlong = "{'device':'wait', 'delay': 600},"
    waitverylong = "{'device':'wait', 'delay': 17000},"

    precise=True
    
    delay = 150 #Settings.CommandDelayMs;
    delayMFDs = delay
    delayUFC = delay / 4
    delayUFCOpt = delay /2
    delayUFCOnOff = delay 
    delayUFCEnt = delay / 2
    delayIFEI = delay / 2
    delayRot = delay / 20
    WPstart=0
    
    Dev["UFC"]=25
    Com["AP"]=(3001, "AP", delayUFC, 1)
    Com[ "IFF"]=(3002, "IFF", delayUFC, 1)
    Com[ "TCN"]=(3003, "TCN", delayUFC, 1)
    Com[ "ILS"]=(3004, "ILS", delayUFC, 1)
    Com[ "DL"]=(3005, "DL", delayUFC, 1)
    Com[ "BCN"]=(3006, "BCN", delayUFC, 1)
    Com[ "OnOff"]=(3007, "OnOff", delayUFCOnOff, 1)
    Com[ "COM1"]=(3008, "COM1", delayUFCOnOff, 1)
    Com[ "COM2"]=(3009, "COM2", delayUFCOnOff, 1)
    Com[ "Opt1"]=(3010, "Opt1", delayUFCOpt, 1)
    Com[ "Opt2"]=(3011, "Opt2", delayUFCOpt, 1)
    Com[ "Opt3"]=(3012, "Opt3", delayUFCOpt, 1)
    Com[ "Opt4"]=(3013, "Opt4", delayUFCOpt, 1)
    Com[ "Opt5"]=(3014, "Opt5", delayUFCOpt, 1)
    Com[ "0"]=(3018, "0", delayUFC, 1)
    Com[ "1"]=(3019, "1", delayUFC, 1)
    Com[ "2"]=(3020, "2", delayUFC, 1)
    Com[ "3"]=(3021, "3", delayUFC, 1)
    Com[ "4"]=(3022, "4", delayUFC, 1)
    Com[ "5"]=(3023, "5", delayUFC, 1)
    Com[ "6"]=(3024, "6", delayUFC, 1)
    Com[ "7"]=(3025, "7", delayUFC, 1)
    Com[ "8"]=(3026, "8", delayUFC, 1)
    Com[ "9"]=(3027, "9", delayUFC, 1)
    Com[ "CLR"]=(3028, "CLR", delayUFC, 1)
    Com[ "ENT"]=(3029, "ENT", delayUFCEnt, 1)
    
    Com[ "COM1ChDec"]=(3033, "COM1ChDec", -1, 0)
    Com[ "COM1ChInc"]=(3033, "COM1ChInc", -1, 2)
    Com[ "COM2ChDec"]=(3034, "COM2ChDec", -1, 0)
    Com[ "COM2ChInc"]=(3034, "COM2ChInc", -1, 2)
    

    Dev["IFEI"]=33
    Com[ "UP"]=(3003, "UP", delayIFEI, 1)
    Com[ "DOWN"]=(3004, "DOWN", delayIFEI, 1)

    Dev["LMFD"]=35
                        
    Com[ "OSB-01"]=(3011, "OSB-01", delayMFDs, 1)
    Com[ "OSB-02"]=(3012, "OSB-02", delayMFDs, 1)
    Com[ "OSB-03"]=(3013, "OSB-03", delayMFDs, 1)
    Com[ "OSB-04"]=(3014, "OSB-04", delayMFDs, 1)
    Com[ "OSB-05"]=(3015, "OSB-05", delayMFDs, 1)
    Com[ "OSB-06"]=(3016, "OSB-06", delayMFDs, 1)
    Com[ "OSB-07"]=(3017, "OSB-07", delayMFDs, 1)
    Com[ "OSB-08"]=(3018, "OSB-08", delayMFDs, 1)
    Com[ "OSB-09"]=(3019, "OSB-09", delayMFDs, 1)
    Com[ "OSB-10"]=(3020, "OSB-10", delayMFDs, 1)
    Com[ "OSB-11"]=(3021, "OSB-11", delayMFDs, 1)
    Com[ "OSB-12"]=(3022, "OSB-12", delayMFDs, 1)
    Com[ "OSB-13"]=(3023, "OSB-13", delayMFDs, 1)
    Com[ "OSB-14"]=(3024, "OSB-14", delayMFDs, 1)
    Com[ "OSB-15"]=(3025, "OSB-15", delayMFDs, 1)
    Com[ "OSB-16"]=(3026, "OSB-16", delayMFDs, 1)
    Com[ "OSB-17"]=(3027, "OSB-17", delayMFDs, 1)
    Com[ "OSB-18"]=(3028, "OSB-18", delayMFDs, 1)
    Com[ "OSB-19"]=(3029, "OSB-19", delayMFDs, 1)
    Com[ "OSB-20"]=(3030, "OSB-20", delayMFDs, 1)


    Dev["RMFD"] = 36
    Com[ "OSB-01"]=(3011, "OSB-01", delayMFDs, 1)
    Com[ "OSB-02"]=(3012, "OSB-02", delayMFDs, 1)
    Com[ "OSB-03"]=(3013, "OSB-03", delayMFDs, 1)
    Com[ "OSB-04"]=(3014, "OSB-04", delayMFDs, 1)
    Com[ "OSB-05"]=(3015, "OSB-05", delayMFDs, 1)
    Com[ "OSB-06"]=(3016, "OSB-06", delayMFDs, 1)
    Com[ "OSB-07"]=(3017, "OSB-07", delayMFDs, 1)
    Com[ "OSB-08"]=(3018, "OSB-08", delayMFDs, 1)
    Com[ "OSB-09"]=(3019, "OSB-09", delayMFDs, 1)
    Com[ "OSB-10"]=(3020, "OSB-10", delayMFDs, 1)
    Com[ "OSB-11"]=(3021, "OSB-11", delayMFDs, 1)
    Com[ "OSB-12"]=(3022, "OSB-12", delayMFDs, 1)
    Com[ "OSB-13"]=(3023, "OSB-13", delayMFDs, 1)
    Com[ "OSB-14"]=(3024, "OSB-14", delayMFDs, 1)
    Com[ "OSB-15"]=(3025, "OSB-15", delayMFDs, 1)
    Com[ "OSB-16"]=(3026, "OSB-16", delayMFDs, 1)
    Com[ "OSB-17"]=(3027, "OSB-17", delayMFDs, 1)
    Com[ "OSB-18"]=(3028, "OSB-18", delayMFDs, 1)
    Com[ "OSB-19"]=(3029, "OSB-19", delayMFDs, 1)
    Com[ "OSB-20"]=(3030, "OSB-20", delayMFDs, 1)
    
    Dev["RadAlt"]=30
    Com["Decrease"]=(3002, "Decrease", delayRot, -8)
    Com["Increase"]=(3002, "Increase", delayRot, 0.015)
    Com["Test"]=(3001, "Test", delay, 1)
    
    
    Dev["CMDS"] = 54
    Com["ON"]=(3001, "ON", -1, 0.1)
    Com["OFF"]=(3001, "OFF", -1, -1)
    Com["BYPASS"]=(3001, "BYPASS", -1, 1)



    def GetCommand(self,D,C):
        #ComID=0
        #ComDL=2
        #ComAC=3
        return "{'device': '" + str(self.Dev[D]) + "', 'code': '" + str(self.Com[C][0])     + "', 'delay': '" + str(int(self.Com[C][2])) + "', 'activate': '" + str(self.Com[C][3]) + "'},";

    def StartCommand(self):
        output = "{'start_condition': 'NOT_AT_WP_0'}," + self.GetCommand("RMFD","OSB-13") + "{'end_condition': 'NOT_AT_WP_0'},";
        output = output*100 
        return output
    
    def buildDigits(self,coord):
        out=""
        co=coord.replace(" ","").replace(".","")

        for i,c in enumerate(co):
            if c == "N":
                out += self.GetCommand("UFC","2")
            elif c == 'S':
                out += self.GetCommand("UFC","8")
            elif c == 'E':
                out += self.GetCommand("UFC","6")
            elif c == 'W':
                out += self.GetCommand("UFC","4")
            else:
                if self.precise and len(co)-i == 4:
                    out += self.GetCommand("UFC","ENT")
                out += self.GetCommand("UFC",c)
        return out

    def BuildWPCommands(self,WayPoints):
        ComLine=""
        ComLine += self.GetCommand("RMFD","OSB-18") # MENU
        ComLine += self.GetCommand("RMFD","OSB-18") # MENU
        ComLine += self.GetCommand("RMFD","OSB-02") # HSI
        
        ComLine += self.GetCommand("RMFD","OSB-10") # DATA
        ComLine += self.GetCommand("RMFD","OSB-07") # WYPT
        ComLine += self.StartCommand()

        for i in range(self.WPstart):
            ComLine += self.GetCommand("RMFD","OSB-12") # set the initial WP
        if self.precise:
            ComLine += self.GetCommand("RMFD","OSB-19") # set precision coords
        ComLine += self.GetCommand("RMFD","OSB-05") # UFC
        ComLine += self.wait
        for w in WayPoints:
 #           ComLine += self.GetCommand("UFC","Opt1")
            ComLine += self.GetCommand("UFC","Opt1")
            ComLine += self.wait
            ComLine += self.buildDigits(w['Latitude'])
            ComLine += self.GetCommand("UFC","ENT")
            ComLine += self.waitlong
            ComLine += self.buildDigits(w['Longitude'])
            ComLine += self.GetCommand("UFC","ENT")
            ComLine += self.waitlong
            ComLine += self.GetCommand("UFC","Opt3")
            ComLine += self.GetCommand("UFC","Opt1")
            for c in str(w['Elevation']):
                ComLine += self.GetCommand("UFC",c)
            ComLine += self.GetCommand("UFC","ENT")
            ComLine += self.wait
            ComLine += self.GetCommand("RMFD","OSB-12") #next WP
        for i in  range(len(WayPoints)):
            ComLine += self.GetCommand("RMFD","OSB-13")
        ComLine += self.wait
        if self.precise:
            ComLine += self.GetCommand("RMFD","OSB-19") # set precision coords
        ComLine += self.GetCommand("RMFD","OSB-18")
        ComLine += self.wait
        ComLine += self.GetCommand("RMFD","OSB-18")
        ComLine += self.GetCommand("RMFD","OSB-15")

        return ComLine



