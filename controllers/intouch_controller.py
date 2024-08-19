# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request

INTOUCH_TRANSACTION_FIELDS = ['meter_no', 'amount', 'first_name', 'last_name', 'email_address', 'phone_number',
                              'callback']

TRANSACTION_CALLBACK_RESPONSE = [
    'service_id', 'gu_transaction_id', 'status', 'partner_transaction_id', 'call_back_url', 'commission', 'message'
]


class IntouchController(http.Controller):
    @http.route('/api/intouch/transaction', auth='public', methods=['POST'], csrf=False, type='json')
    def initiate_transaction(self, **kw):
        raw_data = request.httprequest.get_data()
        data = json.loads(raw_data)

        if not all(field in data for field in INTOUCH_TRANSACTION_FIELDS):
            return {
                "message": "Missing required fields",
                "status": False,
                'data': {}
            }

        transaction_request = request.env['intouch_integration.transaction_request'].sudo().create({
            'recipient_email': data.get('email_address'),
            'recipient_first_name': data.get('first_name'),
            'recipient_last_name': data.get('last_name'),
            'destinataire': data.get('meter_no'),
            'recipient_number': data.get('phone_number'),
            'amount': data.get('amount'),
            'callback': data.get('callback'),
            'service_code': 'PAIEMENTMARCHANDOMPAYCIDIRECT'

        })

        if transaction_request:
            return {
                'message': 'Transaction initiated successfully',
                'status': True,
                'data': {
                    "otp": transaction_request.otp
                }
            }
        else:
            return {
                'message': 'Failed to initiate transaction',
                'status': False,
                'data': {}
            }

    @http.route('/api/intouch/callback', auth='public', methods=['POST'], csrf=False, type='json')
    def transaction_callback(self, **kw):
        raw_data = request.httprequest.get_data()
        data = json.loads(raw_data)

        if not all(field in data for field in INTOUCH_TRANSACTION_FIELDS):
            return {
                "message": "Missing required fields",
                "status": False,
                'data': {}
            }

        transaction_request = request.env['intouch_integration.transaction_request'].sudo().create({
            'recipient_email': data.get('email_address'),
            'recipient_first_name': data.get('first_name'),
            'recipient_last_name': data.get('last_name'),
            'destinataire': data.get('meter_no'),
            'recipient_number': data.get('phone_number'),
            'amount': data.get('amount'),
            'callback': data.get('callback'),
            'service_code': 'PAIEMENTMARCHANDOMPAYCIDIRECT'

        })

        if transaction_request:
            return {
                'message': 'Transaction initiated successfully',
                'status': True,
                'data': {
                    "otp": transaction_request.otp
                }
            }
        else:
            return {
                'message': 'Failed to initiate transaction',
                'status': False,
                'data': {}
            }
