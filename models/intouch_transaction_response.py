from odoo import models, fields


class IntouchTransactionResponse(models.Model):
    _name = 'intouch_integration.intouch_transaction_response'
    _description = 'Intouch Transaction Response'

    transaction_request_id = fields.Many2one('intouch_intergration.intouch_transaction_request',
                                             string='Transaction Request')
    id_from_gu = fields.Char(string='ID from GU')
    amount = fields.Float(string='Amount')
    fees = fields.Float(string='Fees')
    service_code = fields.Selection(related='transaction_request_id.service_code', string='Service Code', required=True)
    recipient_number = fields.Char(string='Recipient Number')
    date_time = fields.Datetime(string='Transaction Date')
    status = fields.Char(string='Status')
    num_transaction = fields.Char(string='Transaction Number')
    payment_url = fields.Char(string='Payment URL')
    code_marchand = fields.Char(string='Code Marchand')



