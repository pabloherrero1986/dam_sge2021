# -*- coding: utf-8 -*-
# from odoo import http


# class Panaderia(http.Controller):
#     @http.route('/panaderia/panaderia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/panaderia/panaderia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('panaderia.listing', {
#             'root': '/panaderia/panaderia',
#             'objects': http.request.env['panaderia.panaderia'].search([]),
#         })

#     @http.route('/panaderia/panaderia/objects/<model("panaderia.panaderia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('panaderia.object', {
#             'object': obj
#         })
