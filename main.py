import getdata
import gui
import logs

from structure import *

import datetime

def Main():
    
    connection = getdata.TestConnection()

    if (connection):
        print("Can connect :)")
        data = obj_Covid()

        data.date = datetime.date.today().strftime("%d/%m/%Y")
        data.time = int(datetime.datetime.now().strftime("%H"))

        data = getdata.GetData(data)

        previousData = obj_Covid()

        previousData = logs.ReadLog(previousData)

        # gui.PrintToTerminal(data,previousData)

        gui.CreateWindow(data,previousData)

    else:
        print("Can't connect :(")
        a= input()
        print(a)
    
    


if __name__ == "__main__":
    Main()