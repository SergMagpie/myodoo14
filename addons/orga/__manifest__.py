# -*- coding: utf-8 -*-
{
    'name': "orga",

    'summary': """
        The module was created by Serhii Sorokin 
        """,

    'description': """
        The module was created by Serhii Sorokin        
    """,
    'author': "Serhii Sorokin",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'fleet',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/tour_plan.xml',
        'views/driver_break.xml',
        'views/vacation_schedule.xml',
        'views/basic_planing.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -100,
}
