# -*- coding: utf-8 -*-

from odoo import models, fields

class SalesFood(models.Model):
    _name = 'hotel.sales.foods'
    _description = 'sales_foods'
    _rec_name = "food_id"
    food_id = fields.Many2one('hotel.foods',string="Food ID")
    customer_no = fields.Many2one('hotel.customer',string="Customer NO")
