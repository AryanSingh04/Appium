import requests
def breach_data(mail):
    url = f"https://api.haveibeenbreached.com/?contact={mail}"
    response = requests.get(url)
    try:
     if response.status_code == 200:
       data = response.json()
       print("Given Email:",mail)
       print("Your Breach Count:",len(data))
       for d in data:
           if(d["Domain"]!=""):      
            print(f"https://{d["Domain"]}","on",d["BreachDate"])
            print("Compromised Data:",d["DataClasses"])
       
     else:
      print("Server Error :", response.status_code)
    except Exception as e:
        print("Error Occurred: ",e)
     
emails = [
"demo@gmail.com"
]

for e in emails:
    print("\n")
    breach_data(e)
