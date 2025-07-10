# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hotba',
    'version' : '1.2',
    'summary': 'islamic website',
    'sequence': -102,
    'description': """ is islamic website""",
    'category': '',
    'depends' : ["base"],
    'data': [
        'security/ir.model.access.csv',
        "viwes/hotba.xml",
        "viwes/shahik.xml",
        "viwes/menu.xml",
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
