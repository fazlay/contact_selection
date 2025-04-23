# -*- coding: utf-8 -*-
{
    'name': "contact-selection",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '17.0',
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/contact_selection_views.xml',
        'views/contact_product_views.xml',
        'views/contact_type_list.xml',
    ],
}
