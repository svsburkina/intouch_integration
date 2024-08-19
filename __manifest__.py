# -*- coding: utf-8 -*-
{
    'name': "Intouch Integration",

    'summary': "Intouch Integration",

    'description': """
Provide a way to integrate with Intouch
    """,

    'author': "Bigmachini",
    'website': "https://www.svsburkina.com",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['svs_burkina'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
