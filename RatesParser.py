import json

class RatesParser():
    def __init__(self, rates_file): # We must pass in a valid json file at object instantiation
        rate_info = self.open_json_file(rates_file)
        self.base = rate_info['base']
        self.date = rate_info['date']
        self.rates = rate_info['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def open_json_file(self,json_file):
        with open(json_file) as rates:
            return json.load(rates)

rate_reader = RatesParser("exchange_rate.json")
print(rate_reader.gbp)
print(rate_reader.aud)

class RatesParser2():
    def __init__(self, base, date, rates, AUD, GBP):
        self.base = base
        self.date = date
        self.rates = rates
        self.aud = AUD
        self.gbp = GBP

def open_json_file(json_file):
    with open(json_file) as rates:
        return json.load(rates)

rates_file_2 = open_json_file("exchange_rate.json")
base = rates_file_2['base']
date = rates_file_2['date']
rates = rates_file_2['rates']
aud = rates['AUD']
gbp = rates['GBP']
rates_parser2_obj = RatesParser2