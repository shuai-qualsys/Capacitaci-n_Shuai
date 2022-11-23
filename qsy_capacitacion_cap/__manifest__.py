{
    'name': "capacitacion",
    'version': '15.0.1',
    'depends': ['base'],
    'author': "Qualsys Consulting",
    'category': 'Customizations',
    'sumary': 'Capacitación para nuevos programadores',
    # Utilizan un tipo de estructura llamado reestructured 
    'description': """
Escuela
=========================

Modulos
-----------------------------
- Escuelas

- Profesores

- Asignaturas
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_assing_courses_views.xml',
        'wizards/wizard_assing_attendees_views.xml',
        'views/qualsys_schools_views.xml',
        'views/qualsys_courses_views.xml',
        'views/qualsys_asistentes_views.xml'

    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        #'demo/demo_data.xml',
    ],
    'license' : 'LGPL-3'
}
