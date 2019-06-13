# -*- coding: utf-8 -*-
from odoo import http

# class Reportes(http.Controller):
#     @http.route('/reportes/reportes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reportes/reportes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reportes.listing', {
#             'root': '/reportes/reportes',
#             'objects': http.request.env['reportes.reportes'].search([]),
#         })

#     @http.route('/reportes/reportes/objects/<model("reportes.reportes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reportes.object', {
#             'object': obj
#         })