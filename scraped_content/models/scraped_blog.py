from odoo import models, fields


class ScrapedBlog(models.Model):
    _name = 'scraped.blog'
    _description = 'Scraped Blog'
    _rec_name = "title"
    title = fields.Char(string="Title")
    summary = fields.Text(string="Summary")
    content = fields.Text(string="Content")
    source_url = fields.Char(string="Source URL")
    date_published = fields.Date(string="Date Published")
    status = fields.Selection([
        ('new', 'New'),
        ('reviewed', 'Reviewed'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], string="Status", default='new')
