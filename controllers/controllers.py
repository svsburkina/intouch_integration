# -*- coding: utf-8 -*-
# from odoo import http


# class IntouchIntergration(http.Controller):
#     @http.route('/intouch_intergration/intouch_intergration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/intouch_intergration/intouch_intergration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('intouch_intergration.listing', {
#             'root': '/intouch_intergration/intouch_intergration',
#             'objects': http.request.env['intouch_intergration.intouch_intergration'].search([]),
#         })

#     @http.route('/intouch_intergration/intouch_intergration/objects/<model("intouch_intergration.intouch_intergration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('intouch_intergration.object', {
#             'object': obj
#         })

