import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class SimpleTemplate(webapp2.RequestHandler):
    template_path = ''

    def get(self):
        if self.template_path:
            template = jinja_environment.get_template(self.template_path)
            self.response.out.write(template.render())
        else:
            raise jinja2.exceptions.TemplateNotFound

class SubscriptionsUK(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)

    def get(self, legacy_offer_key = None):
        if legacy_offer_key:
            self.redirect('/', permanent=True)
        else:
            template = jinja_environment.get_template('subscriptions-uk.html')
            self.response.out.write(template.render())

class SubscriptionsUS(SimpleTemplate):
    template_path = 'subscriptions-us.html'

class SubscriptionsAu(SimpleTemplate):
    template_path = 'subscriptions-au.html'

class DigitalPackUK(SimpleTemplate):
    template_path = 'digital-pack-uk.html'

class DigitalPackUS(SimpleTemplate):
    template_path = 'digital-pack-us.html'

class DigitalPackAu(SimpleTemplate):
    template_path = 'digital-pack-au.html'


app = webapp2.WSGIApplication([
    ('/us/digitalpack', DigitalPackUS),
    ('/us', SubscriptionsUS),
    ('/au/digitalpack', DigitalPackAu),
    ('/au', SubscriptionsAu),
    ('/digitalpack', DigitalPackUK),
    ('/', SubscriptionsUK),
    ('/(.*?)', SubscriptionsUK),
], debug=True)
