import requests
def breach_data(mail):
    url = f"https://api.haveibeenbreached.com/?contact={mail}"
    response = requests.get(url)
    if response.status_code == 200:
       data = response.json()
       print("Given Email:",mail)
       print("Your Breach Count:",len(data))
       for d in data:
           if(d["Domain"]!=""):      
            print(d["Domain"],d["BreachDate"])
    else:
     print("Server Error :", response.status_code)
     
breach_data("demo@gmail.com")
