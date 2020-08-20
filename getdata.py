import main

try:
    import httplib
except:
    import http.client as httplib

from covid import Covid

def TestConnection():
    conn = httplib.HTTPConnection("coronavirus.jhu.edu", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def GetData(data):
    # change data.country to your country
    data.country = "Slovakia"
    
    covid = Covid()
    
    data.totalActiveCases = covid.get_total_active_cases()
    data.totalConfirmedCases = covid.get_total_confirmed_cases()
    data.totalDeaths = covid.get_total_deaths()
    data.totalRecovered = covid.get_total_recovered()

    tmp = covid.get_status_by_country_name(data.country)

    data.countryActiveCases = tmp["active"]
    data.countryConfirmedCases = tmp["confirmed"]
    data.countryDeaths = tmp["deaths"]
    data.countryRecovered = tmp["recovered"]
    
    return data

if __name__ == "__main__":
    main.Main()
