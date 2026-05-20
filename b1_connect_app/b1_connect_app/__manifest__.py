# -*- coding: utf-8 -*-
{
    'name': 'SAP Business One Connector (B1ConnectApp)',
    'summary': 'Integración automatizada y robusta para conectar Odoo con SAP Business One Service Layer.',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'author': 'Nova Desarrollos CR',
    'website': 'https://www.novadesarrolloscr.com',
    'license': 'LGPL-3',  # Al ser una app de marketing/captura, ponerla gratis (LGPL-3) atrae mas leads
    'depends': [
        'base'
    ],
    'data': [
        'views/dashboard_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}