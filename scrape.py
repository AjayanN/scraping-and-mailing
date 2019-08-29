import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Canon-1500D-24-1MP-Digital-55-250mm/dp/B07BRR59DT?ref_=Oct_BSellerC_1389177031_3&pf_rd_p=222d974d-338a-582b-b58d-52b08e0463b7&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=1389177031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=N0J5SHABZNSQC39PX3NE&pf_rd_r=N0J5SHABZNSQC39PX3NE&pf_rd_p=222d974d-338a-582b-b58d-52b08e0463b7'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}



def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id = 'productTitle').getText()
    price = soup.find(id = 'priceblock_ourprice').getText()
    converted_price_na = price[2:8]
    converted_price = float(''.join(converted_price_na.split(',')))

    if(converted_price>30000):
        send_mail()

    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('xxxxxx@gmail.com', 'kxsbxxxxhlxxuof')

    subject = 'Price fell down'
    body = 'check here : https://www.amazon.in/Canon-1500D-24-1MP-Digital-55-250mm/dp/B07BRR59DT?ref_=Oct_BSellerC_1389177031_3&pf_rd_p=222d974d-338a-582b-b58d-52b08e0463b7&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=1389177031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=N0J5SHABZNSQC39PX3NE&pf_rd_r=N0J5SHABZNSQC39PX3NE&pf_rd_p=222d974d-338a-582b-b58d-52b08e0463b7 '
    msg = f'subject: {subject}\n\n{body}'
    server.sendmail(
        'axxxx@gmail.com',
        'frer@gmail.com',
        msg
    )
    print('email sent')
    server.quit()

check_price()
