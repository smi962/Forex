import os.path
import requests
import sys
import datetime

class tick_data_request():

    global str_Request = 'https://sandbox-api.spotware.com/connect/tradingaccounts'

    def __init__(self,start,ed,symbol,account_id):
        self.start = start
        self.ed = ed
        self.symbol = symbol
        self.account_id = account_id
        self.request_string = []
        self.auth_code = []


    def get_request_URL(self):

        if not self.auth_code:
            raise ValueError('No authority code provided for request. Please obtain one to obtain tick data.')
        else:
            s1 = os.path.join(str_Request, self.account_id)
            s2 = os.path.join(s1, 'symbols', str(self.symbol))
            s3 = os.path.join(s2, 'ask?')
            date_range = 'from={}&to={}'.format(datetime.strftime('%Y%m%d%H%M%S',self.start),datetime.strftime('%Y%m%d%H%M%S',self.ed))
            print date_range
            self.request_string = s3 + date_range + '&' + 'oauth_token =' + self.auth_code
        print self.request_string
        return self.request_string

    def get_auth_code(self):
        self.account_id

    def url_request(self):
        if not self.request_string:
            raise ValueError('No request string provided. Please provide one.')
        else:
            req = requests.get(self.request_string)
            if req.status_code == '200':
                file=req.json
            elif req.status_code == '400':
                raise ValueError('Bad HTTP request for tick data.')
            elif req.status_code == '404':
                raise ValueError('Requested tick data was not found')
            elif req.status_code == '500':
                raise ValueError('Internal server error')
        return file