import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

editions = {
    'uk': {
        'id': 'uk',
        'name': 'UK',
        'cmp': 'dis_2408',
    },
    'us': {
        'id': 'us',
        'name': 'US',
        'cmp': 'dis_2378',
    },
    'au': {
        'id': 'au',
        'name': 'Australia',
        'cmp': 'dis_2379',
    },
}


class SimpleTemplate(webapp2.RequestHandler):
    template_path = ''
    context = {}

    def get(self):
        if self.template_path:
            template = jinja_environment.get_template(self.template_path)
            self.response.out.write(template.render(self.context))
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
    context = {'edition': editions['us']}
    template_path = 'subscriptions-int.html'


class SubscriptionsAU(SimpleTemplate):
    context = {'edition': editions['au']}
    template_path = 'subscriptions-int.html'


class DigitalPackUK(SimpleTemplate):
    context = {'edition': editions['uk']}
    template_path = 'digital-pack.html'


class DigitalPackUS(SimpleTemplate):
    context = {'edition': editions['us']}
    template_path = 'digital-pack.html'


class DigitalPackAU(SimpleTemplate):
    context = {'edition': editions['au']}
    template_path = 'digital-pack.html'


app = webapp2.WSGIApplication([
    ('/us/digitalpack', DigitalPackUS),
    ('/us', SubscriptionsUS),
    ('/au/digitalpack', DigitalPackAU),
    ('/au', SubscriptionsAU),
    ('/digitalpack', DigitalPackUK),
    ('/', SubscriptionsUK),
    ('/(.*?)', SubscriptionsUK),
], debug=True)
