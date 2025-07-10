from odoo import api, fields, models, _, tools

class Hotba(models.Model):
    _name = "hotba"
    _description = "hotba islamic"
    name = fields.Char(string="أسم الخطبة")
    shahik_id = fields.Many2one("shahik",string="أسم الشيخ")
    video = fields.Binary(string="Video", attachment=True)
    audio = fields.Binary(string="Audio", attachment=True)