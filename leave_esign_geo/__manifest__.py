{
    'name': 'Leave with eSignature & Geo Verification',
    'version': '1.0.0',
    'summary': 'Submit leaves, e-sign by employee (no user required), capture geo-location, HR verification and manager approval',
    'author': 'Generated for user',
    'category': 'Human Resources',
    'depends': ['hr', 'website', 'mail','hr_holidays'],
    'data': [
    'security/security.xml',
    'security/ir.model.access.csv',
    'data/mail_template_data.xml',
    'views/hr_leave_request_views.xml',
    'views/leave_templates.xml',
    'views/website_leave_sign.xml',
    ],
    'assets': {
    'web.assets_frontend': [
    'leave_esign_geo/static/src/js/sign.js',
    'leave_esign_geo/static/src/css/sign.css',
    ],
    },
    'installable': True,
    'application': False,
}