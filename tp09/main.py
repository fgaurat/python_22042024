import requests
from bs4 import BeautifulSoup
from pprint import pprint
def main():
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for a in soup.find_all('a'):
        print(a['href'])        
    
    # url_logs = filter(lambda u:u['href'].endswith('.log'),soup.find_all('a') )
    all_a = soup.find_all('a')
    url_logs = [u['href'] for u in all_a if u['href'].endswith('.log')]
    pprint(url_logs)
    




if __name__=='__main__':
    main()
