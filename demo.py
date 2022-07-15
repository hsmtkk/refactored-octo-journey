# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.hcaptcha(
        sitekey='3ceb8624-1970-4e6b-91d5-70317b70b651',
        url='https://2captcha.com/demo/hcaptcha',
    )
    print(type(result))

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))