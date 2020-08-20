import tkinter as tk
import main
import logs

def FormatNum(input):
    digit = 0
    tmp = str(input)[::-1]
    for c in tmp:
        if (c.isdigit() == False):
            return input

    output = ""
    while (digit < len(tmp)):
        if (digit % 3 == 0):
            output = " " + output

        output = tmp[digit] + output
        digit += 1
         

    return output

def PrintToTerminal(data,previous):
    print(f"Todays date: {data.date}")
    print(f"Hour now: {data.time}\n")
    print(f"World active: {FormatNum(data.totalActiveCases)}")
    print(f"World confirmed: {FormatNum(data.totalConfirmedCases)}")
    print(f"World deaths: {FormatNum(data.totalDeaths)}")
    print(f"World recovered: {FormatNum(data.totalRecovered)}\n")
    print(f"Slovakia active: {FormatNum(data.countryActiveCases)}")
    print(f"Slovakia confired: {FormatNum(data.countryConfirmedCases)}")
    print(f"Slovakia deaths: {FormatNum(data.countryDeaths)}")
    print(f"Slovakia recovered: {FormatNum(data.countryRecovered)}\n")

    print("--------------------")
    print(f"Previous date: {previous.date}")
    print(f"Hour previous: {previous.time}\n")
    print(f"World active: {FormatNum(previous.totalActiveCases)}")
    print(f"World confirmed: {FormatNum(previous.totalConfirmedCases)}")
    print(f"World deaths: {FormatNum(previous.totalDeaths)}")
    print(f"World recovered: {FormatNum(previous.totalRecovered)}\n")
    print(f"Slovakia active: {FormatNum(previous.countryActiveCases)}")
    print(f"Slovakia confired: {FormatNum(previous.countryConfirmedCases)}")
    print(f"Slovakia deaths: {FormatNum(previous.countryDeaths)}")
    print(f"Slovakia recovered: {FormatNum(previous.countryRecovered)}")


def Diff(x,y):
    val = int(x) - int(y)
    if (val>0):
        out = f"+{FormatNum(val)}"
    else:
        out = f"{FormatNum(val)}"
    return out


def CreateWindow(data,previous):
    root = tk.Tk()
    root.title("Active covid cases")
    output1types = f"""
    Todays date:        
    Hour now:           
    World active:
    World confirmed:
    World deaths:
    World recovered:
    Slovakia active:
    Slovakia confirmed:
    Slovakia deaths:
    Slovakia recovered:
    """
    output2types = f"""
    Previous date:
    Hour previous:
    World active:
    World confirmed:
    World deaths:
    World recovered:
    Slovakia active:
    Slovakia confired:
    Slovakia deaths:
    Slovakia recovered:
    """
    output1values=f"""
    {data.date}
    {data.time}
    {FormatNum(data.totalActiveCases)}
    {FormatNum(data.totalConfirmedCases)}
    {FormatNum(data.totalDeaths)}
    {FormatNum(data.totalRecovered)}
    {FormatNum(data.countryActiveCases)}
    {FormatNum(data.countryConfirmedCases)}
    {FormatNum(data.countryDeaths)}
    {FormatNum(data.countryRecovered)}
    """

    output2values = f"""
    {previous.date}
    {previous.time}
    {FormatNum(previous.totalActiveCases)}
    {FormatNum(previous.totalConfirmedCases)}
    {FormatNum(previous.totalDeaths)}
    {FormatNum(previous.totalRecovered)}
    {FormatNum(previous.countryActiveCases)}
    {FormatNum(previous.countryConfirmedCases)}
    {FormatNum(previous.countryDeaths)}
    {FormatNum(previous.countryRecovered)}
    """

    diffvalues = f"""
    Diffe
    rence
    {Diff(data.totalActiveCases,previous.totalActiveCases)}
    {Diff(data.totalConfirmedCases,previous.totalConfirmedCases)}
    {Diff(data.totalDeaths,previous.totalDeaths)}
    {Diff(data.totalRecovered,previous.totalRecovered)}
    {Diff(data.countryActiveCases,previous.countryActiveCases)}
    {Diff(data.countryConfirmedCases,previous.countryConfirmedCases)}
    {Diff(data.countryDeaths,previous.countryDeaths)}
    {Diff(data.countryRecovered,previous.countryRecovered)}
    """

    label1 = tk.Label(root, text=output2types,font = "Helvetica 15",justify="left")
    label2 = tk.Label(root, text=output2values,font = "Helvetica 15",justify="left")
    label3 = tk.Label(root, text=output1types,font = "Helvetica 15",justify="left")
    label4 = tk.Label(root, text=output1values,font = "Helvetica 15",justify="left")
    label5 = tk.Label(root, text=diffvalues,font = "Helvetica 15",justify="left")

    label1.grid(row=0,column=0)
    label2.grid(row=0,column=1)
    label3.grid(row=0,column=2)
    label4.grid(row=0,column=3)
    label5.grid(row=0,column=4)

    if (data.date != previous.date):
            logs.WriteLog(data)
            label6 = tk.Label(root, text="Previous overwritten",font = "11",justify="left")
            label6.grid(row=1,column=0)


    root.mainloop()

if __name__ == "__main__":
    main.Main()