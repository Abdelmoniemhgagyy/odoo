# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_

class Customer(models.Model):
    _name = 'hotel.customer'
    _description = 'customer'

    name = fields.Char(string="Customer Name")
    national_id = fields.Char(string="National ID")
    customer_no = fields.Char(
        string="No.Customer",
        copy=False, readonly=True,
        default=lambda self: _('New'))
    employee_id = fields.Many2one('hotel.employee',string="Employee ID")
    reserve_ids = fields.One2many('hotel.reservations','customer_no')
    food_ids = fields.One2many('hotel.sales.foods','customer_no')
    total_price_food = fields.Float(string="Total Food Price", compute="_compute_total_price", store=True)
    total_price_reservation = fields.Float(string="Total Reservation Price",compute="_compute_total_price", store=True)
    total_price = fields.Float(string="Total Price",compute="_compute_total_price", store=True)

    @api.model
    def create(self, vals):
        if vals.get('customer_no', _("New")) == _("New"):
            vals['customer_no'] = self.env['ir.sequence'].next_by_code('hotel.customer') or _("New")
        return super(Customer, self).create(vals)
    @api.depends("food_ids.food_id.price","reserve_ids.price_stay")
    def _compute_total_price(self):
        for record in self :
            record.total_price_food = sum(record.food_ids.mapped('food_id.price'))
            record.total_price_reservation = sum(record.reserve_ids.mapped('price_stay'))  # Corrected
            record.total_price = record.total_price_food + record.total_price_reservation
