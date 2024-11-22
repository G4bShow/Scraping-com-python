import requests
from bs4 import BeautifulSoup

url = "https://www.kabum.com.br/hardware/placa-de-video-vga"

headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")

last_pag = soup.find("a", class_="page active").get_text().strip()


for i in range (1,int(last_pag)):
        url_pag = f"https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={i}&page_size=20&facet_filters=&sort=most_searched"
        site = requests.get(url_pag, headers=headers)
        soup = BeautifulSoup(site.content, "html.parser")
        placas = soup.find_all("div", class_= "sc-27518a44-8 dsdRWH")
        
        with open ("precos_placa.csv","a", newline="", encoding="UFT-8") as f:
                for placa in placa:
                        marca = placa.find("span", class_="sc-d79c9c3f-0 nlmfp sc-27518a44-9 iJKRqI nameCard").get_text().strip()
                        
                        try:
                            price = placa.find("span", class_= "sc-d79c9c3f-0 nlmfp sc-27518a44-9 iJKRqI nameCard").get_text().strip()
                            num_price = price[2:]
                            num_price = num_price[:-3]
                            
                        except:
                            num_price = "0"  
                                    
                        try:                                 
                           price_ticket = placa.find("", class_="").get_text().strip()
                           index = price_ticket.find(",")
                           num_price_ticket = price_ticket[10:index]
  
                        except:
                           num_price_ticket = "0"       
                           
                        linha = marca + "," + num_price + "," + num_price_ticket + "/n"  
                        
                        
                        print(linha) 
                        f.write(linha)
        print(url_pag)                
