# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_

class Foods(models.Model):
    _name = 'hotel.foods'
    _description = 'foods'
    _rec_name = "food_id"
    food_id = fields.Char(
                string='Food ID',
                copy=False, readonly=True,
                default=lambda self: _('New'))

    food_name = fields.Char(string="Food Name")
    price = fields.Float(string="Price")
    # customer_no = fields.Many2one('hotel.customer',string="Customer NO")

    @api.model
    def create(self, vals):
        if vals.get('food_id', _("New")) == _("New"):
            vals['food_id'] = self.env['ir.sequence'].next_by_code('hotel.foods') or _("New")
        return super(Foods, self).create(vals)
