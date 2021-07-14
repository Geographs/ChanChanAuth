# ChanChanAuth
Python wrapper for https://api.ccauth.app/
## Examples of Usage

### Login
```py
from chanchanauth import Client


client = Client(AID, APIKEY, SECRET)
response = client.login(USERNAME, PASSWORD, HWID)

if response.is_authenticated:
    print("Logged in")
```
### Register
```py
from chanchanauth import Client

client = Client(AID, APIKEY, SECRET)
response = client.register(USERNAME, PASSWORD, HWID, DISCORD, LICENSE)

if response.success:
    print("Success")
```
### Reset HWID
```py
from chanchanauth import Client

client = Client(AID, APIKEY, SECRET)
response = client.hwid_reset(USERNAME, PASSWORD, HWID, HWID_KEY)

if response.success:
    print("success")
 ```
 ### Generate License
 ```py
 from chanchanauth import Admin
 
 admin = Admin(AID, APIKEY, USERNAME, PASSWORD)
 response = admin.generate_license()
 
 if response.success:
    print(response.license)
```
 ### Generate HWID Key
 ```py
 from chanchanauth import Admin
 
 admin = Admin(AID, APIKEY, USERNAME, PASSWORD)
 response = admin.generate_hwidkey()
 
 if response.success:
    print(response.key)
```
