from email.policy import default

from odoo import models , fields ,api
from odoo.tools.populate import compute


class Member(models.Model):
    _name = "gym.members"
    _description = "gym gym"
    name=fields.Char(string="Full name")
    age=fields.Integer(string="Age",default=20)
    gender=fields.Selection([("male","Male"),("female","Female")],string="Gender",default="male")
    phone=fields.Char(string="Phone Number")
    date_join=fields.Date(string="Date Join")
    subscription_id = fields.Many2one("gym.subscriptions",string="Subscription ID")
    status =fields.Selection([("active","Active"),("inactive","Inactive")],string="Status",default="active")
