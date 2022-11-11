# -*- coding: utf-8 -*-
# pylint: disable=pointless-statement
{
    'name': "CPTI Sales Customizations",
    'version': '15.1.0',

    'summary': """
        CPTI Sales Customizations
    """,

    'description': """
        This module contains customizations for..
        - Quotation Customer View and Print Copy
    """,

    'author': "Courtesy Point Tech, Inc.",
    'website': "http://www.courtesypoint.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml # noqa: E501
    # for the full list
    'category': 'Sales/Sales',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],
 
    # always loaded
    'data': [
        'views/sale_report_templates.xml',
        'views/sale_portal_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
