from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Model of Book'

    name = fields.Char('Title', required=True)
    author = fields.Char('Author')