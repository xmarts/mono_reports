# -*- coding: utf-8 -*-
{
    'name': "reportes",

    'summary': """   
        Generates reports in the inventory module of existing products""",

    'description': """    
        Generates reports in the inventory module of existing products, by type of product, warehouse, category or general""",

    'author': "Xmarts",
    'collaborators': "Gilberto Santiago Acevedo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','purchase','sale'],
    
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reporte/layout.xml',
        'reporte/report_stock.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}