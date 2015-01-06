import os

import jinja2
from jinja2.exceptions import TemplateNotFound
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class SubscriptionsUK(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)

    def get(self, legacy_offer_key = None):
        if legacy_offer_key:
            self.redirect('/', permanent=True)
        else:
            template = jinja_environment.get_template('subscriptions-uk.html')
            self.response.out.write(template.render())

class SubscriptionsUS(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('subscriptions-us.html')
        self.response.out.write(template.render())

class SubscriptionsAu(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('subscriptions-au.html')
        self.response.out.write(template.render())

class DigitalPackUK(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('digital-pack-uk.html')
        self.response.out.write(template.render())

class DigitalPackUS(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('digital-pack-us.html')
        self.response.out.write(template.render())

class DigitalPackAu(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('digital-pack-au.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/us/digitalpack', DigitalPackUS),
    ('/us', SubscriptionsUS),
    ('/au/digitalpack', DigitalPackAu),
    ('/au', SubscriptionsAu),
    ('/digitalpack', DigitalPackUK),
    ('/', SubscriptionsUK),
    ('/(.*?)', SubscriptionsUK),
], debug=True)
