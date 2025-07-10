from odoo import fields,models,api,_
class Subscriptions(models.Model):
    _name="gym.subscriptions"
    _description = "gym subscriptions"
    _rec_name = 'subscription_id'
    subscription_id = fields.Char(
        string="Subscriptions ID",
        copy=False, readonly=True,
        default=lambda self: _('New'))
    subscription_type = fields.Selection([("annual","Annual"),("monthly","monthly")],string="SUB TYPE")
    price = fields.Integer(string="Price")
    @api.model
    def create(self, val):
            if not val.get('subscription_id') or val['subscription_id'] == _('New'):
                val['subscription_id'] = self.env['ir.sequence'].next_by_code('gym.subscriptions') or _('New')
            return super(Subscriptions,self).create(val)