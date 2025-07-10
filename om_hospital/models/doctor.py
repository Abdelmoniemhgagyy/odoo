from odoo import models, fields,api ,_
class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "doctor_name"

    doctor_name = fields.Char(string='Name', required=True,tracking=True)
    age = fields.Integer(string='Age',tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender',tracking=True)
    note = fields.Text(string='Note')
    doctor_image = fields.Binary(string='doctor Image')
    appointment_count = fields.Integer(string="Appointment Count",compute='_compute_appointment_count')
    active = fields.Boolean(string="Active",default=True)
    def copy(self, default=None):
        if default is None:
            default = {}
        if 'doctor_name' not in default:
            default['doctor_name'] = _(f"{self.doctor_name} (.copy)", )
            default['note']="its copied"
        return super(HospitalDoctor, self).copy(default=default)
    def _compute_appointment_count(self):
        for doctor in self:
             res = self.env['hospital.appointment'].search_count([('doctor_id','=',doctor.id)])
             doctor.appointment_count= res
