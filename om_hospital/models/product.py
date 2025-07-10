from odoo import models, fields

class ProductOrder(models.Model):
    _inherit = 'product.template'
    type = fields.Selection(selection_add=[
        ('test','Test')
    ],ondelete={'test':'set default'})
