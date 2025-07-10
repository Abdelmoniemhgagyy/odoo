# -*- coding: utf-8 -*-
{
    'name': "Scraped Content",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/scraped_job_views.xml',
        'views/scraped_blog_views.xml',
        'views/scraped_page_views.xml',
        'views/menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
