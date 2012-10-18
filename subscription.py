import os

import jinja2
from jinja2.exceptions import TemplateNotFound
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Page(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.templateDict = {
            None : "offer/default-subscription.html",
            "FBA01" : "offer/default-subscription.html",
            "TAA01" : "offer/default-offer.html",
            "TCA01" : "offer/default-offer.html"
        }

    def get(self, promoCode = None):
        method = self.request.get('method', 'voucher')
        if(promoCode in self.templateDict) :
            template = jinja_environment.get_template(self.templateDict[promoCode])
            self.response.out.write(template.render(method = method, promoCode = promoCode))
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/.*?/(.*?)', Page),
    ('/.*?', Page)
], debug=True)
