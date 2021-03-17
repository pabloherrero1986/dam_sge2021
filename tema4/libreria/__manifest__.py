# -*- coding: utf-8 -*-
{
    'name': "Librería",

    'summary': """
        Librería de Pablo Herrero""",

    'description': """
        Librería de Pablo Herrero Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """,

    'author': "Herrero S.L.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xml'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_libro.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
