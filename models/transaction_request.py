import logging
import random
import uuid

import requests

from odoo import models, fields, api
from .utils import AGENCY_CODE, LOGIN_AGENT, PASSWORD_AGENT, SERVICE_CODES, TRANSACTION_STATUS


class IntouchTransactionRequest(models.Model):
    _name = 'intouch_integration.transaction_request'
    _description = 'Intouch Transaction Request'

    transaction_request_id = fields.Char(default=lambda s: uuid.uuid4().hex, help="Transaction UUID", size=20,
                                         readonly=True)
    recipient_email = fields.Char(string='Recipient Email')
    recipient_first_name = fields.Char(string='Recipient First Name')
    recipient_last_name = fields.Char(string='Recipient Last Name')
    destinataire = fields.Char(string='Destinataire')
    recipient_number = fields.Char(string='Recipient Number', required=True)
    otp = fields.Char(string='OTP', default=lambda s: str(random.randint(1000, 9999)), required=True, readonly=True)
    amount = fields.Float(string='Amount', required=True)
    callback = fields.Char(string='Callback URL')
    service_code = fields.Selection(SERVICE_CODES, string='Service Code', required=True)
    transaction_status = fields.Selection(TRANSACTION_STATUS, string='Transaction Status', default='pending')
    error_message = fields.Text(string='Error Message')

    @api.model
    def create(self, vals):
        record = super(IntouchTransactionRequest, self).create(vals)
        record.on_create_trigger()
        return record

    def on_create_trigger(self):
        url = f"https://apidist.gutouch.net/apidist/sec/touchpayapi/{AGENCY_CODE}/transaction"
        params = {
            'loginAgent': LOGIN_AGENT,
            'passwordAgent': PASSWORD_AGENT
        }
        transaction_data = {
            "idFromClient": self.transaction_request_id,
            "additionnalInfos": {
                "recipientEmail": self.recipient_email,
                "recipientFirstName": self.recipient_first_name,
                "recipientLastName": self.recipient_last_name,
                "destinataire": self.destinataire,
                "otp": self.otp
            },
            "amount": self.amount,
            "callback": self.callback,
            "recipientNumber": self.recipient_number,
            "serviceCode": self.service_code
        }

        try:
            response = requests.post(url, params=params, json=transaction_data, timeout=10)
            response_status = response.status_code

            # updated the status code for the request
            self.env['intouch_integration.intouch_transaction_response'].create({
                'transaction_request_id': self.transaction_request_id,
                'response_status': response_status
            })

            # updated the response for the request
            if response_status == 200:
                data = response.json()
                self.env['intouch_integration.intouch_transaction_response'].create({
                    'transaction_request_id': self.transaction_request_id,
                    'id_from_gu': data.get('idFromGU'),
                    'amount': data.get('amount'),
                    'fees': data.get('fees'),
                    'service_code': data.get('serviceCode'),
                    'recipient_number': data.get('recipientNumber'),
                    'date_time': fields.Datetime.from_string(data.get('dateTime')),
                    'status': data.get('status'),
                    'num_transaction': data.get('numTransaction'),
                    'payment_url': data.get('payment_url'),
                    'code_marchand': data.get('codeMarchand')
                })
            else:
                raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
        except Exception as e:
            self.write({'transaction_status': 'failed',
                        'error_message': f"Failed to fetch data: {e}"})
            logging.error(f'on_create_trigger:: Exception: {e}')
