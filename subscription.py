import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

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

packages = {
    'collection-paper-digital': {
        'method': 'collection',
        'package': 'paper-digital',
        'name': 'Paper + digital voucher subscription',
        'urls': {
            'everyday': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx01&title=gv7&skip=1',
            'sixday': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx01&title=gv6&skip=1',
            'weekend': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx01&title=gv2&skip=1',
            'sunday': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx01&title=ov1&skip=1',
        }
    },
    'collection-paper': {
        'method': 'collection',
        'package': 'paper',
        'name': 'Paper voucher subscription',
        'urls': {
            'everyday': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx00&title=gv7&skip=1',
            'sixday': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx00&title=gv6&skip=1',
            'weekend': 'https://www.guardiansubscriptions.co.uk/Voucher?prom=faa03&pkgcode=ukx00&title=gv2&skip=1',
        }
    },
    'delivery-paper-digital': {
        'method': 'delivery',
        'package': 'paper-digital',
        'name': 'Paper + digital home delivery subscription',
        'urls': {
            'everyday': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=EVERYDAY%2B',
            'sixday': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=SIXDAY%2B',
            'weekend': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=WEEKEND%2B',
            'sunday': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=SUNDAY%2B',
        }
    },
    'delivery-paper': {
        'method': 'delivery',
        'package': 'paper',
        'name': 'Paper home delivery subscription',
        'urls': {
            'everyday': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=EVERYDAY',
            'sixday': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=SIXDAY',
            'weekend': 'https://www.guardiandirectsubs.co.uk/Delivery/details.aspx?package=WEEKEND',
        }
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


class DigitalPackNew(SimpleTemplate):
    template_path = 'digital-pack-new.html'


class PackageForm(SimpleTemplate):
    template_path = 'choose-package.html'

    def post(self):
        package = self.request.get('package')
        method, package = package.rsplit('-', 1)
        try:
            url = packages[method]['urls'][package]
            return webapp2.redirect(url)
        except KeyError:
            return webapp2.redirect(self.request.referer)


class CollectionDigitalPaper(PackageForm):
    context = {'package': packages['collection-paper-digital']}


class CollectionPaper(PackageForm):
    context = {'package': packages['collection-paper']}


class DeliveryDigitalPaper(PackageForm):
    context = {'package': packages['delivery-paper-digital']}


class DeliveryPaper(PackageForm):
    context = {'package': packages['delivery-paper']}

app = webapp2.WSGIApplication([
    ('/us/digitalpack', DigitalPackUS),
    ('/us', SubscriptionsUS),
    ('/au/digitalpack', DigitalPackAU),
    ('/au', SubscriptionsAU),
    ('/digitalpack', DigitalPackUK),
    ('/digital', DigitalPackNew),
    ('/collection/paper-digital', CollectionDigitalPaper),
    ('/collection/paper', CollectionPaper),
    ('/delivery/paper-digital', DeliveryDigitalPaper),
    ('/delivery/paper', DeliveryPaper),
    ('/', SubscriptionsUK),
    ('/(.*?)', SubscriptionsUK),
], debug=debug)
