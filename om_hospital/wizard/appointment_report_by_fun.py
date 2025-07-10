from odoo import models, fields

class AppointmentReportWizardByFunc(models.TransientModel):
    _name = 'appointment.report.wizard.by.func'
    _description = 'report Appointment Wizard By'
    age = fields.Integer(string='Age',)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', tracking=True)
    def print_report(self):
        data = {
            'form':self.read()[0],
        }
        return self.env.ref('om_hospital.actions_appointment_report').report_action(self, data=data)

