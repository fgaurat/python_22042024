import requests
from bs4 import BeautifulSoup
from pprint import pprint
def main():
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for a in soup.find_all('a'):
        print(a['href'])        
    
    # url_logs = list(filter(lambda u:u.endswith('.log'),[u['href'] for u in soup.find_all('a')] ))
    
    all_a = soup.find_all('a')
    url_logs = [u['href'] for u in all_a if u['href'].endswith('.log')]

    for file_name in url_logs:
        u = f"{url}{file_name}"
        response = requests.get(u)
        with open(file_name,"w") as f:
            f.write(response.text)
            # print(response.text,file=f)
    




if __name__=='__main__':
    main()
