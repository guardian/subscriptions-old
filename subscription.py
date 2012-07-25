import os

import jinja2
from jinja2.exceptions import TemplateNotFound
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Page(webapp2.RequestHandler):
    def get(self, page, promoCode = None):
        page = page or 'index'
        method = self.request.get('method', 'voucher')
        try:
            template = jinja_environment.get_template(page + '.html')
            self.response.out.write(template.render(method = method, promoCode = promoCode, page = page))
        except TemplateNotFound:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/(.*?/(.*?))', Page),
    ('/(.*?)', Page)
], debug=True)
