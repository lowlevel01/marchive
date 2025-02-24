import re

def find_urls_and_ips(text):
    url_pattern = re.compile(
        r'\b(?:https?://|www\.)\S+\b', re.IGNORECASE
    )
    
    ip_pattern = re.compile(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    )
    
    urls = url_pattern.findall(text)
    ips = ip_pattern.findall(text)
    return {
        'urls': urls,
        'ips': ips
    }

file = open("8535c08d7e637219470c701599b5de4b85f082c446b4d12c718fa780e7535f07","r").read()

print(find_urls_and_ips(file))
