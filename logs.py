import main

def WriteLog(data):
    with open ("total_previous.txt","w") as f:
        f.write(f"{data.date}\n")
        f.write(f"{data.time}\n")
        f.write(f"{data.totalActiveCases}\n")
        f.write(f"{data.totalConfirmedCases}\n")
        f.write(f"{data.totalDeaths}\n")
        f.write(f"{data.totalRecovered}\n")
        f.write(f"{data.countryActiveCases}\n")
        f.write(f"{data.countryConfirmedCases}\n")
        f.write(f"{data.countryDeaths}\n")
        f.write(f"{data.countryRecovered}")
        

def ReadLog(data):
    try:
        with open ("total_previous.txt","r") as f:
            
            tmp = f.read()
            tmp = tmp.split("\n")
            
            data.date = tmp[0]
            data.time = int(tmp[1])
            data.totalActiveCases = int(tmp[2])
            data.totalConfirmedCases = int(tmp[3])
            data.totalDeaths = int(tmp[4])
            data.totalRecovered = int(tmp[5])
            data.countryActiveCases = int(tmp[6])
            data.countryConfirmedCases = int(tmp[7])
            data.countryDeaths = int(tmp[8])
            data.countryRecovered = int(tmp[9])
    except:
        print("Error while reading file :(")
        exit()
    
    return data

if __name__ == "__main__":
    main.Main()