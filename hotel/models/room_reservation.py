# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_

class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'rooms'
    _rec_name = "room_no"
    room_no = fields.Integer(string="Room No")
    reserve_no = fields.Many2one('hotel.reservations',string="Reservation NO")
