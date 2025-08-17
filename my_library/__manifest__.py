{
    'name': 'My Library',
    'version': '1.0',
    'summary': 'A simple module to manage books.',
    'author': 'Maria Fernanda',
    'website': 'https://www.wwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        ],
    'installable': True,
    'application': True,
}