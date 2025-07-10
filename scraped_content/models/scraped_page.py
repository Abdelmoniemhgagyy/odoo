from odoo import models, fields


class ScrapedPage(models.Model):
    _name = 'scraped.page'
    _description = 'Scraped page'
    _rec_name = "title"
    title = fields.Char(string="Title")
    content = fields.Text(string="Content")
    source_url = fields.Char(string="Source URL")
    status = fields.Selection([
        ('new', 'New'),
        ('reviewed', 'Reviewed'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], string="Status", default='new')
