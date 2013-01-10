import os

import jinja2
from jinja2.exceptions import TemplateNotFound
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Page(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.offers = {
            None : {
                'template': 'offer/default-subscription.html',
                'promoCode': 'FBA01',
            },
            'offer/FBA01' : {
                'template': 'offer/default-subscription.html',
                'promoCode': 'FBA01',
            },
            'offer/TAA01' : {
                'template': 'offer/default-voucher.html',
                'promoCode': 'TAA01',
            },
            'offer/TCA01' : {
                'template': 'offer/default-voucher.html',
                'promoCode': 'TCA01',
            },
            'paper2013': {
                'template': 'offer/2013.html',
                'promoCode': 'PBA01',
            },
            'press2013': {
                'template': 'offer/2013.html',
                'promoCode': 'PBA02',
            },
            'email2013': {
                'template': 'offer/2013.html',
                'promoCode': 'PDA01',
            },
            'letter2013': {
                'template': 'offer/2013.html',
                'promoCode': 'PCA01',
            },
            'web2013': {
                'template': 'offer/2013.html',
                'promoCode': 'PGA01',
            },
            'ppc2013': {
                'template': 'offer/2013.html',
                'promoCode': 'PHA01',
            },
        }

    def get(self, offer_key = None):
        method = self.request.get('method', 'voucher')

        if(offer_key in self.offers) :
            offer = self.offers.get(offer_key)
            template = jinja_environment.get_template(offer.get('template'))
            self.response.out.write(template.render(method = method, promoCode = offer.get('promoCode')))
        elif offer_key:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', Page),
    ('/(.*?)', Page),
], debug=True)
