# -*- coding: utf-8 -*-
{
    'name': "gse_purchase_stock",

    'summary': """
        Add completion status on Purchase""",

    'description': """
        
    """,

    'author': "Sébastien Bühl",
    'website': "http://www.buhl.be",

    'category': 'Customizations',
    'version': '0.1.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['purchase_stock'],

    'data': [       
        'views/purchase_views.xml',
    ],
    
}