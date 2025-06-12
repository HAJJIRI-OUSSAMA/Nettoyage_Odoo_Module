from odoo import models, fields, api

class Material(models.Model):
    _name = 'nettoyage.material'
    _description = 'Matériel de Nettoyage'

    name = fields.Char('Nom du Matériel', required=True)
    quantity = fields.Integer('Quantité Disponible')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('in_use', 'En Utilisation'),
        ('maintenance', 'En Maintenance')
    ], default='available')
    last_maintenance = fields.Date('Dernière Maintenance')
    next_maintenance = fields.Date('Prochaine Maintenance')
