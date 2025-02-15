from subprocess import call
from pymisp import PyMISP 
from dicttoxml import dicttoxml
import hashlib
import xml.etree.ElementTree as ET
import urllib
def internet_on():
    try:
        urllib.request.urlopen('http://149.13.33.15', timeout=1)
        return True
    except urllib.error.URLError as err: 
        return False
def prelim(fname):
    #for signature based detection  
    print("Testing at MISP")
    hash_md5 = hashlib.md5()
    with open(fname,"rb") as f:
        for chunk in iter(lambda: f.read(4096),b""):
            hash_md5.update(chunk)
    md5=hash_md5.hexdigest()        
   
    return md5
def mispextract(fpath):
        
       # md5="626576e5f0f85d77c460a322a92bb267"
        url="https://misppriv.circl.lu"
        apikey="6hmcjLFKtbk9i0eSGvxeUZ6RRJdcC5zRhafoNmXs"
        conn=internet_on()
        if conn:
            api=PyMISP(url,apikey,ssl=True, out_type='json' ,debug=False, proxies=None)
            md5=prelim(fpath)
            response = api.search_all(md5)
            length=len(response["response"])
            retu={"connection":True,
                  "positives":length
                  }
            return retu
            #print(len(list(root)))
            
        else:
            print("No connectivity with MISP")
            retu={"connection":False,
                  "positives":0
                  }
            return retu

