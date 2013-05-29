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
            template = jinja_environment.get_template('landing_page.html')
            self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', LandingPage),
    ('/(.*?)', LandingPage),
], debug=True)
