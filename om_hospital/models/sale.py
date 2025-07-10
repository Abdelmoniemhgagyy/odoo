from odoo import models, fields
from odoo.addons.sale.models.sale import SaleOrder as SaleOdooOrder
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    sale = fields.Char(string='Sale Order')
    # def unlink(self):
    #     return super(SaleOdooOrder, self).unlink()