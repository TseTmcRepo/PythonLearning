# Parse last price from tse
def last_price(namad):

    import requests
    from bs4 import BeautifulSoup
    url = namad_url(namad)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    scripts = soup.find_all('script')

    vr = str(scripts[3].text).split('TradeHistory=')[1].split('...')[0].replace('\n', '')
    ls = eval(vr[0:vr.find(';')])  # convert to list
    lp = int(float(ls[0][4]))  # last price of stock

    return lp


def namad_url(namad):
    import csv
    with open('namad_url.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        name = {}
        for row in reader:
            name.update({row[0]: row[1]})
    return name[namad]