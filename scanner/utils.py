import re

def find_links(text):
    url_pattern = r'(https?://[^\s]+)'
    return re.findall(url_pattern, text)
