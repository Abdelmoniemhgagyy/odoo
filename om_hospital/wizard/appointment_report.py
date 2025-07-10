from odoo import models, fields
class AppointmentReportWizard(models.TransientModel):
    _name = 'appointment.report.wizard'
    _description = 'report Appointment Wizard'
    date_from = fields.Date(string='Date From',)
    date_to = fields.Date(string='Date To',)
    patient_id = fields.Many2one('hospital.patient',string='Patient')
    def print_xlsx_report(self):
        appointments = self.env['hospital.appointment'].search_read()
        data = {
                'appointments': appointments,
                'form': self.read()[0]
               }
        return self.env.ref('om_hospital.appointments_wizard_xlsx').report_action(self, data=data)
    def print_report(self):
        domain=[]
        patient_id = self.patient_id
        if patient_id:
            domain+=[('patient_id','=',patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain+=[('date_appointment','>=',date_from)]
        date_to = self.date_to
        if date_to:
            domain+=[('date_appointment','<=',date_to)]
        appointments = self.env['hospital.appointment'].search_read(domain)
        data = {
            'form':self.read()[0],
            'appointments':appointments
        }
        return self.env.ref('om_hospital.actions_appointment_report').report_action(self, data=data)