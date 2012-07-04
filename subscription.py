import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Index(webapp2.RequestHandler):
    def get(self, r):
        r = r or 'index'
        method = self.request.get('method', 'voucher')
        template = jinja_environment.get_template(r + '.html')
        self.response.out.write(template.render(method = method))

class Promo(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('promo.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
	('/promo', Promo),
    ('/(.*)', Index)
], debug=True)
