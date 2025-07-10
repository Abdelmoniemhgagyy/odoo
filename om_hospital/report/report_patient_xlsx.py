from odoo import models
import base64
from io import BytesIO

class PartnerXlsx(models.AbstractModel):
    _name = 'report.om_hospital.template_id_card_patient_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        report_name = "Patient xlsx"
        sheet = workbook.add_worksheet(report_name[:31])
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
        sheet.write(row, col, "Name", bold)
        sheet.write(row, col+1, "Age", bold)
        row += 1

        for obj in patients:
            # Insert image if available
            if obj.image:
                image_data = base64.b64decode(obj.image)
                image_stream = BytesIO(image_data)
                sheet.insert_image(row,col, 'patient_image.png', {'image_data': image_stream, 'x_scale': 0.1, 'y_scale': 0.1})
                row += 5

            # Write patient name and age
            sheet.write(row, col, obj.name, bold)
            sheet.write(row, col+1, obj.age, bold)
            row += 1

