# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Demo_App',
    'category': 'Website/Website',
    'sequence': 265,
    'summary': 'Manage a forum with FAQ and Q&A',
    'version': '1.1',
    'description': """
Ask questions, get answers, no distractions
        """,
    'website': 'https://www.odoo.com/app/Demo_App',
    'depends': [
        'auth_signup',
        'website_mail',
        'website_profile',
    ],
    'data': [
        "Views/views.xml",
        "Views/menus.xml",
    ],
    'demo': [

            ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}
