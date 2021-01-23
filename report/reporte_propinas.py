# -*- coding: utf-8 -*-
from openerp import http

# class EcloPosReportePropina(http.Controller):
#     @http.route('/eclo_pos_reporte_propina/eclo_pos_reporte_propina/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eclo_pos_reporte_propina/eclo_pos_reporte_propina/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eclo_pos_reporte_propina.listing', {
#             'root': '/eclo_pos_reporte_propina/eclo_pos_reporte_propina',
#             'objects': http.request.env['eclo_pos_reporte_propina.eclo_pos_reporte_propina'].search([]),
#         })

#     @http.route('/eclo_pos_reporte_propina/eclo_pos_reporte_propina/objects/<model("eclo_pos_reporte_propina.eclo_pos_reporte_propina"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eclo_pos_reporte_propina.object', {
#             'object': obj
#         })