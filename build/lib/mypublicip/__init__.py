import requests

def ip():

    try:
        try:
            # Get public IP address
            publicIP = requests.get('http://ip.42.pl/raw').text
        except:
            publicIP = requests.get('https://api.ipify.org').text  
            
        return publicIP  
        
    except Exception as e:
        return ('Can\'t get IP info from http://ip.42.pl/raw or https://api.ipify.org [Error] :', e)
