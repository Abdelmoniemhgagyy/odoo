# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_

class Employee(models.Model):
    _name = 'hotel.employee'
    _description = 'employee'

    name = fields.Char(string="Employee Name")
    age = fields.Integer(string="Age")
    salary = fields.Float(string="Main Salary")
    employee_id = fields.Char(
        string='EMPLOYEE ID',
        copy=False, readonly=True,
        default=lambda self: _('New'))
    employee_reservation_count = fields.Integer(string="Reservation Count",compute='_compute_reservation_count',store=True)
    employee_bouns = fields.Integer(compute="_compute_bouns",string="Bouns",store=True)
    @api.model
    def create(self, vals):
        if vals.get('employee_id', _("New")) == _("New"):
            vals['employee_id'] = self.env['ir.sequence'].next_by_code('hotel.employee') or _("New")
        return super(Employee, self).create(vals)


    def _compute_reservation_count(self):
        for employee in self:
            res = self.env['hotel.customer'].search_count([('employee_id', '=', employee.id)])
            employee.employee_reservation_count = res
    def _compute_bouns(self):
        for employee in self:
            employee.employee_bouns = (employee.employee_reservation_count // 10 ) * 50 if employee.employee_reservation_count  else 0
