from odoo import models, fields, api


class WizardReportXlsx(models.AbstractModel):
    _name = 'report.om_hospital.template_id_wizard_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objs):
        report_name = "Patient xlsx"
        sheet = workbook.add_worksheet("Appointments")
        print(data['appointments'])
        print(objs)
        bold = workbook.add_format({'bold': True})
        merge_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
        })
        row = 0
        col = 0
        # sheet.merge_range('A1:B1', "Sheet 1", merge_format)
        sheet.merge_range(row,col,row+1,col+1, "Sheet 1", merge_format)
        row += 1
        sheet.set_column('A:A', 30)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 20)
        row += 1
        sheet.write(row, col, "Reference", bold)
        sheet.write(row, col+1, "Patient", bold)
        sheet.write(row, col+1, "Date", bold)
        row += 1

        for appointment in data['appointments'] :
            sheet.write(row, col, appointment['reference'], bold)
            sheet.write(row, col+1, appointment['patient_id'][1], bold)
            sheet.write(row, col+2, appointment['date_appointment'], bold)
            row+=1
