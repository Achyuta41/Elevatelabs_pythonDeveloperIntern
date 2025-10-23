import requests
from bs4 import BeautifulSoup
def scarp_headline(limit):
    url="https://www.bbc.com/news"
    try:
        response=requests.get(url)
        if response.status_code!=200:
            print(f"Failed to fetch webpages. status code {requests.status_code}")
            return []
        soup =BeautifulSoup(response.text,'html.parser')
        headlines=soup.find_all('h2')
        headlst=[headline.get_text().strip() for headline in headlines if headline.get_text().strip()]

        headlst=list(dict.fromkeys(headlst))
        return headlst[:limit]
    except Exception as e:
        print(f"An error occured:{e}")
        return []
    
def save(headlines,limit,filename="Task3/headlines.txt"):
    try:
        with open(filename,'w',encoding='utf-8') as file:
            print(f"Top {limit} headlines from BBC news",file=file)
            print("----------------------------------------",file=file)
            for i,headline in enumerate(headlines,1):
                file.write(f"{i}.{headline}\n")
            print(f"\n\nHeadlines saved to file {filename} ")
    except Exception as e:
        print(e)
if __name__=='__main__':
    print("Scarping headlines from BBC news.......")
    limit=int(input("Enter how many headlines you want??"))
    headlines=scarp_headline(limit)
    if headlines:
        print(f"\n Top {limit} headlines from BBC news")
        for i,headline in enumerate(headlines,1):
            print(f"{i}.{headline}")

        save(headlines,limit)
    else:
        print("NOOO")
        
