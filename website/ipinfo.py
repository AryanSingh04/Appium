import requests
def ip_data(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    try:
     if response.status_code == 200:
       data = response.json()
       print(data)
     else:
      print("Server Error :", response.status_code)
    except Exception as e:
        print("Error Occurred: ",e)
    
ips=[
       "49.43.2.165",
       "27.7.244.88",
       "80.231.130.130"
]
    
for e in ips:
 ip_data(e)


