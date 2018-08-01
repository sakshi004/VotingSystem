import requests
from pyquery import PyQuery as pq

base_url="http://dev.trustnote.org:3000/detail#{0}"
def get_amount(address):
    url=base_url.format(address)

    r = requests.get(url)
    html = r.text
    d = pq(r.text)
    print (d("#address").text())
    print (url)

get_amount("JVFHPXAA7FJEJU3TSTR5ETYVOXHOBR4H")
