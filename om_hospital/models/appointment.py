from odoo import models, fields,api ,_
from odoo.exceptions import ValidationError
class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name="patient_id"
    _order = "id desc,doctor_id desc "
    reference = fields.Char(string='Reference',
                            required=True, copy=False,
                            readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient',string='Patient')
    patient_name_id = fields.Many2one('hospital.patient',string='Patient Name')
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor')
    age = fields.Integer(string='Age',related='patient_id.age',tracking=True,store=True)
    gender = fields.Selection([('male','Male'),('female','Female')],related='patient_id.gender',store=True,string="Gender")
    state = fields.Selection([ ('draft', 'Draft'),('confirm', 'Confirm'),('done', 'Done'),('cancel', 'Cancel')
    ], string='Status',default='draft',tracking=True)
    note = fields.Text(string='Note')
    date_appointment=fields.Date(string="Date")
    datetime_appointment=fields.Datetime(string="DateTime")
    prescription = fields.Text()
    prescription_lines_ids=fields.One2many("appointment.prescription.lines","appointment_id",
                                           string="Prescription Lines")

    def action_draft(self):
        self.state="draft"
    def action_confirm(self):
        self.state="confirm"
    def action_done(self):
        self.state="done"
    def action_cancel(self):
        self.state="cancel"
    @api.model
    def create(self,vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        res = super(HospitalAppointment,self).create(vals)
        return res
    # @api.onchange("patient_id")
    # def onchange_patient(self):
    #     if self.patient_id:
    #         if self.patient_id.gender:
    #             self.gender = self.patient_id.gender
    #     else:
    #         self.gender = ''
    def unlink(self):
        if self.state == 'done':
            raise ValidationError(f"you cant delete it ")

        super(HospitalAppointment, self).unlink()
    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://portfolio-hgagy.vercel.app/',
        }



class AppointmentPrescriptionLines(models.Model):
    _name = 'appointment.prescription.lines'
    _description = 'Appointment Prescription Lines'
    name=fields.Char(string="Medicine")
    qyt = fields.Integer(string="Quantity")
    appointment_id=fields.Many2one("hospital.appointment",
                                           string="Appointment")


