from json import load
import os
import sys

import bs4
import requests
import twocaptcha

APIKEY_ENV = 'APIKEY_2CAPTCHA'
URL = 'https://accounts.hcaptcha.com/demo'

def main():
    api_key = os.getenv(APIKEY_ENV)
    if api_key is None:
        print('you must define', APIKEY_ENV, ' environment variable')
        sys.exit(1)    

    # get and parse html contents
    resp = requests.get(URL)
    html = resp.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # find data-sitekey
    div = soup.find(id='hcaptcha-demo')
    data_sitekey = div['data-sitekey']
    print('data-sitekey', data_sitekey)

    solver = twocaptcha.TwoCaptcha(api_key)
    result = solver.hcaptcha(
        sitekey=data_sitekey,
        url=URL,
    )

    print('2captcha result', result)

    # post response code
    payload = {'h-captcha-response': result['code']}
    resp = requests.post(URL, data=payload)
    print(resp.text)

if __name__ == '__main__':
    main()
