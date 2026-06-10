from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    my_type = fields.Selection(
        selection=[
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
        ],
        string='Type',
        default='a',
    )
