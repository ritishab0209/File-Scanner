import re
import requests

# Define a simple regex-based malicious URL checker
def check_url_malicious(url):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    if re.search(ip_pattern, url):
        return "Suspicious (IP-based URL)"
    else:
        return "No issues found"

# For VirusTotal or other APIs
def check_url_with_virus_total(url, api_key):
    headers = {"x-apikey": api_key}
    response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url}", headers=headers)
    return response.json()  # Process response as needed
