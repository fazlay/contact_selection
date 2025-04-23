# -*- coding: utf-8 -*-
# from odoo import http


# class Contact-selection(http.Controller):
#     @http.route('/contact-selection/contact-selection', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact-selection/contact-selection/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact-selection.listing', {
#             'root': '/contact-selection/contact-selection',
#             'objects': http.request.env['contact-selection.contact-selection'].search([]),
#         })

#     @http.route('/contact-selection/contact-selection/objects/<model("contact-selection.contact-selection"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact-selection.object', {
#             'object': obj
#         })
