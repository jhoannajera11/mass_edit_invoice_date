# -*- coding: utf-8 -*-
{
    'name': "Asistente para Cambiar Fecha de Factura Masivamente",
    'summary': "Añade una acción para cambiar la fecha de factura en múltiples borradores.",
    'description': """
        Este módulo añade un asistente en el menú de acción de las facturas
        para poder establecer una fecha de factura específica a múltiples
        facturas en estado borrador de forma simultánea.
    """,
    'author': "Humanytek",
    'category': 'Accounting/Accounting',
    'version': '18.0.1.0.0',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/update_invoice_date_wizard_view.xml',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}