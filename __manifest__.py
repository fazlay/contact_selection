# -*- coding: utf-8 -*-
{
    'name': "Contact Role Manager",

    'summary': """
        Categorize partners as Customers, Suppliers, or Manufacturers 
        and link them to products""",

    'author': "Metamorphosis",
    'website': "https://metamorphosis.com.bd/",
    'category': 'Uncategorized',
    'version': '17.0.0.1',
    'license': 'AGPL-3',
    'depends': ['base','product'],

    'data': [
        'security/ir.model.access.csv',
        'views/contact_selection_views.xml',
        'views/contact_product_views.xml',
     
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
