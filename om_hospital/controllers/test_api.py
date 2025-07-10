from odoo import http
class PartnersController(http.Controller):
    @http.route('/v1/partners', type="http",auth='none', methods=['GET'], csrf=False)
    def partners_endpoint(self):
        print("ok")
