import os

import jinja2
from jinja2.exceptions import TemplateNotFound
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class LandingPage(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)

    def get(self, legacy_offer_key = None):
        if legacy_offer_key:
            self.redirect('/', permanent=True)
        else:
            template = jinja_environment.get_template('landing-page.html')
            self.response.out.write(template.render())

class InternationalPage(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)

    def get(self):
        template = jinja_environment.get_template('international.html')
        self.response.out.write(template.render())

class DigitalPackUK(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('digital-pack-uk.html')
        self.response.out.write(template.render())

class DigitalPackUS(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('digital-pack-us.html')
        self.response.out.write(template.render())

class DigitalPackAus(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('digital-pack-aus.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/digitalpack', DigitalPackUK),
    ('/digitalpackus', DigitalPackUS),
    ('/digitalpackaus', DigitalPackAus),
    ('/international', InternationalPage),
    ('/', LandingPage),
    ('/(.*?)', LandingPage),
], debug=True)
