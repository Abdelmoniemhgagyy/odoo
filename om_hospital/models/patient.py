from odoo import models, fields,api ,_
from odoo.exceptions import ValidationError
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order= "id desc"

    name = fields.Char(string='Name', required=True,tracking=True)
    reference = fields.Char(string='Reference',
                            required=True, copy=False,
                            readonly=True, default=lambda self: _('New'))
    responsible_id = fields.Many2one('res.partner',string='Responsible')
    age = fields.Integer(string='Age',tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender',tracking=True)
    state = fields.Selection([ ('draft', 'Draft'),('confirm', 'Confirm'),('done', 'Done'),('cancel', 'Cancel')
    ], string='Status',default='draft',tracking=True)
    note = fields.Text(string='Note')
    image = fields.Binary(string='Patient Image')
    appointment_count = fields.Integer(string='Appointment Count',compute='_compute_appointment_count')
    appointment_ids=fields.One2many("hospital.appointment","patient_id",string="Appointment")
    def _compute_appointment_count(self):
        for patient in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', patient.id)])
            patient.appointment_count = appointment_count
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
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        res = super(HospitalPatient,self).create(vals)
        return res

    @api.constrains('name')
    def check_name(self):
        for record in self:
            patients = self.env["hospital.patient"].search([('name','=',record.name),('id','!=',record.id)])
            if patients:
                raise ValidationError(f"{record.name} is Already Exists")
    @api.constrains('age')
    def check_age(self):
        for record in self:
            if record.age == 0 :
                raise ValidationError(f"Age Can't Equal Zero")

    def name_get(self):
        result = []
        for rec in self:
            if not self.env.context.get('hide_code'):
                name = f"[ {rec.reference} ] {rec.name}"
            else :
                name = f"{rec.name}"
            result.append((rec.id, name))
        return result


    def action_open_actions(self):
        return {
            'name': 'Appointment',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'type': 'ir.actions.act_window',
            'domain':[('patient_id', '=', self.id)],
        }

