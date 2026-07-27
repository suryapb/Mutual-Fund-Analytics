#url="https://api.mfapi.in/mf/125497"
#response=requests.get(url)
#print(response.status_code)
#data=response.json()
#print(data.keys())
#print(data["status"])
#print(data["meta"])
#print(type(data["data"]))
#print(data["data"][0])
#data["data"]
#print(len(data["data"]))
#nav_df = pd.DataFrame(data["data"])
#nav_df
#print(nav_df.head())
#nav_df.to_csv("data/raw/live_nav.csv", index=False)
#print("Live NAV saved successfully.")
import requests
import pandas as pd

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}
for fund_name, amfi_code in funds.items():
    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    filename = f"data/raw/{fund_name}.csv"

    nav_df.to_csv(filename, index=False)

    print(f"{fund_name} saved successfully.")