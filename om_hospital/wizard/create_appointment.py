from odoo import models, fields

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'
    date_appointment = fields.Date(string='Date', required=True)
    patient_id = fields.Many2one('hospital.patient',string='Patient')
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor')
    def create_appointment(self):
        vals={
            'patient_id' : self.patient_id.id,
            'doctor_id' : self.doctor_id.id,
            'date_appointment':self.date_appointment
        }
        rec_appointment = self.env['hospital.appointment'].create(vals)
        return {
            'name':'Appointment',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': rec_appointment.id,
            'target': 'new',
        }
    def appointment_view(self):
        action = self.env.ref('om_hospital.hospital_appointment_action').read()[0]
        # action = self.env["ir.actions.actions"]._for_xml_id("om_hospital.hospital_appointment_action")

        action['domain'] = [('patient_id','=',self.patient_id.id)]
        return action
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name':'Appointment',
        #     'res_model': 'hospital.appointment',
        #     'view_type': 'form',
        #     'domain': "[('patient_id','=',self.patient_id.id)]",
        #     'target': 'current',
        #     'view_mode': 'tree,form',
        # }
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res
