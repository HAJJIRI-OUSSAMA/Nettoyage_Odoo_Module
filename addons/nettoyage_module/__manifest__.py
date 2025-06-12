{
    'name': 'Nettoyage Module',
    'version': '1.0',
    'summary': 'Gestion des prestations de nettoyage',
    'depends': ['base', 'hr', 'sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/prestation_views.xml',
        'views/material_views.xml',
        'views/service_type_views.xml',
    ],
    'installable': True,
    'application': True,
}
