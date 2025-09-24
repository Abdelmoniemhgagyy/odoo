from odoo import fields,models
class TodoList(models.Model):
    _name = 'todo.list'

    name = fields.Char(string="Todo List")
    is_done = fields.Boolean(string="Is Done")