from odoo import models, fields, api

class ServiceType(models.Model):
    _name = 'nettoyage.service.type'
    _description = 'Type de Service de Nettoyage'

    name = fields.Char('Nom du Service', required=True)
    description = fields.Text('Description')
    price_per_hour = fields.Float('Prix par Heure')
    required_materials = fields.Many2many('nettoyage.material', string='Matériels Requis')
    estimated_duration = fields.Float('Durée Estimée (heures)')
    prestation_ids = fields.One2many('nettoyage.prestation', 'service_type_id', string='Prestations')
