from odoo import api, fields, models
class SH(models.Model):
    _name = "shahik"
    name = fields.Char(string="أسم الشيخ ")
    shahik_ids = fields.One2many("hotba", "shahik_id", string="أسم الشيخ")
    @api.model
    def create(self, vals):
        record = super(SH,self).create(vals)
        record['name'] = "الشيخ " + record.name
        return record