from odoo import models, fields


class IntouchTransactionResponse(models.Model):
    _name = 'intouch_integration.intouch_transaction_status'
    _description = 'Intouch Transaction Status'

    transaction_request_id = fields.Many2one('intouch_integration.intouch_transaction_request',
                                             string='Transaction Request')
    response_status = fields.Char(string='Response Status')
