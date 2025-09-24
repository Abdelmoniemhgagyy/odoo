# -*- coding: utf-8 -*-
{
    'name': "Todo List",
    'summary': """ """,

    'description': """ Todo List In Odoo """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/todo_owl.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'todo_list/static/src/js/todoList.js',
            'todo_list/static/src/xml/todo_list.xml',
            'todo_list/static/src/css/todoList.css',
        ],},
    # only loaded in demonstration mode
    'demo': [ ],
    'sequence': -10,
    'application': True,
}
