from odoo import models, fields
from .utils import SERVICE_CODES


class IntouchTransactionCallback(models.Model):
    _name = 'intouch_integration.intouch_transaction_callback'
    _description = 'Intouch Transaction Callback'

    service_code = fields.Selection(SERVICE_CODES, string='Service Code', required=True)
    id_from_gu = fields.Char(related='transaction_response_id.id_from_gu', string='ID from GU')
    transaction_response_id = fields.Many2one('intouch_integration.intouch_transaction_response',
                                              string='Transaction Response')
    transaction_request_id = fields.Many2one(related='transaction_response_id.transaction_request_id')
    transaction_status = fields.Char(string='Transaction Status')
    num_transaction = fields.Char(related='transaction_response_id.num_transaction', string='Transaction Number')
    commission = fields.Float(string='Commission')
    message = fields.Char(string='Message')
