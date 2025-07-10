from odoo import models, fields,api
class SaleOrderReportProforma(models.AbstractModel):
    _name = 'report.om_hospital.template_wizard_appointment_pdf_func'
    _description = 'Proforma Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain=[]
        gender=data.get('form').get('gender')
        if gender :
            domain+=[('gender','=',gender)]
        docs = self.env['hospital.patient'].search(domain)

        return {
            'docs': docs,
        }