import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Page(webapp2.RequestHandler):
    def get(self, r):
        r = r or 'index'
        method = self.request.get('method', 'voucher')
        template = jinja_environment.get_template(r + '.html')
        self.response.out.write(template.render(method = method))

app = webapp2.WSGIApplication([
    ('/(.*)', Page)
], debug=True)
