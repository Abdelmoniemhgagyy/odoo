from odoo import models, fields, api
import uuid


class HrLeaveRequest(models.Model):
    _name = 'leave.esign'
    _description = 'Leave Request with eSignature & Geo'


    name = fields.Char(string='Reference', required=True, default=lambda self: 'LR/' + (uuid.uuid4().hex[:8]).upper())
    employee_name = fields.Char(string='Employee Name', required=True)
    employee_email = fields.Char(string='Employee Email')
    leave_type_id = fields.Many2one('hr.leave.type', string='Leave Type')
    date_from = fields.Date(string='Start Date')
    date_to = fields.Date(string='End Date')
    reason = fields.Text(string='Reason')
    state = fields.Selection([
    ('draft','Draft'),
    ('waiting_employee','Waiting Employee'),
    ('waiting_hr','Waiting HR'),
    ('waiting_manager','Waiting Manager'),
    ('approved','Approved'),
    ('rejected','Rejected')
    ], string='Status', default='draft', tracking=True)


    token = fields.Char(string='Access Token', copy=False, index=True)
    signature = fields.Binary(string='Employee Signature')
    signature_mime = fields.Char(string='Signature MIME Type')
    signed_location = fields.Char(string='Signed Location')
    signature_time = fields.Datetime(string='Signature Time')


    hr_checker_id = fields.Many2one('res.users', string='HR Checker')
    manager_id = fields.Many2one('res.users', string='Manager')

    def action_send_link(self):
        template = self.env.ref('leave_esign_geo.mail_template_sign_link', raise_if_not_found=False)
        for rec in self:
            if not rec.token:
                rec.token = uuid.uuid4().hex
                rec.state = 'waiting_employee'
            if template and rec.employee_email:
                template.sudo().with_user(self.env.uid).send_mail(rec.id, force_send=True)
        return True

    def action_mark_waiting_hr(self):
        self.state = 'waiting_hr'


    def action_send_to_manager(self):
        self.state = 'waiting_manager'
    # notify manager via mail (optionally)


    def action_approve(self):
        self.state = 'approved'


    def action_reject(self):
        self.state = 'rejected'