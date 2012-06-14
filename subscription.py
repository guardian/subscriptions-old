import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class Index(webapp2.RequestHandler):
    def get(self, r):
        r = r if r else 'index'
        method = self.request.get('method') if self.request.get('method') else 'voucher'
        template = jinja_environment.get_template(r + '.html')
        self.response.out.write(template.render(method = method))

app = webapp2.WSGIApplication([
    ('/(.*)', Index)
], debug=True)