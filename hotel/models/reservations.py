# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_

class Reservations(models.Model):
    _name = 'hotel.reservations'
    _description = 'reservations'
    _rec_name = "reserve_no"
    date_st = fields.Date(string="Date Start",required=True)
    date_en = fields.Date(string="Date End",required=True)
    stay_days = fields.Integer(string="Stay Days",compute="_compute_stay_days",store=True)
    price_stay = fields.Integer(string="Stay Price",compute="_compute_stay_days",store=True)
    customer_no= fields.Many2one('hotel.customer',string="Customer NO")
    reserve_no = fields.Char(
        string='Reservation NO',
        copy=False, readonly=True,
        default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('reserve_no', _("New")) == _("New"):
            vals['reserve_no'] = self.env['ir.sequence'].next_by_code('hotel.reservations') or _("New")
        return super(Reservations, self).create(vals)

    @api.depends('date_st','date_en')
    def _compute_stay_days(self):
                for record in self:
                    if record.date_st and record.date_en:
                        record.stay_days = (record.date_en - record.date_st).days
                        record.price_stay = record.stay_days * 10
                    else:
                        record.stay_days = 0
                        record.price_stay = 0