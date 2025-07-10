# -*- coding: utf-8 -*-
# from odoo import http


# class ScrapedContent(http.Controller):
#     @http.route('/scraped_content/scraped_content', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scraped_content/scraped_content/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('scraped_content.listing', {
#             'root': '/scraped_content/scraped_content',
#             'objects': http.request.env['scraped_content.scraped_content'].search([]),
#         })

#     @http.route('/scraped_content/scraped_content/objects/<model("scraped_content.scraped_content"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scraped_content.object', {
#             'object': obj
#         })
