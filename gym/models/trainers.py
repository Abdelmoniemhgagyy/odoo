from email.policy import default

from odoo import models , fields ,api
from odoo.tools.populate import compute


class Trainers(models.Model):
    _name = "gym.trainers"
    _description = "gym trainers"
    name=fields.Char(string="Full name")
    age=fields.Integer(string="Age",default=20)
    gender=fields.Selection([("male","Male"),("female","Female")],string="Gender",default="male")
    phone=fields.Char(string="Phone Number")
    date_employee=fields.Date(string="Date Employee")
