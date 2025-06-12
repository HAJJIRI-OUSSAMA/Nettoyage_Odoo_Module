from odoo import models, fields, api

class PrestationNettoyage(models.Model):
    _name = 'nettoyage.prestation'
    _description = 'Prestation de Nettoyage'

    name = fields.Char('Nom de la Prestation', required=True)
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    employe_id = fields.Many2one('hr.employee', string='Employé Affecté')
    date = fields.Date('Date de la prestation', required=True)
    duree = fields.Float('Durée (heures)')
    statut = fields.Selection([
        ('planifiee', 'Planifiée'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée')
    ], default='planifiee', string='Statut')

    total_prestations = fields.Integer(compute='_compute_statistics')
    avg_duree = fields.Float(compute='_compute_statistics')
    service_type_id = fields.Many2one('nettoyage.service.type', string='Type de Service')
    material_ids = fields.Many2many('nettoyage.material', string='Matériels Utilisés')
    price = fields.Float(compute='_compute_price', store=True)
    notes = fields.Text('Notes')
    rating = fields.Selection([
        ('0', 'Non Évalué'),
        ('1', 'Insatisfait'),
        ('2', 'Moyen'),
        ('3', 'Satisfait'),
        ('4', 'Très Satisfait')
    ], default='0', string='Évaluation Client')

    @api.depends('duree')
    def _compute_statistics(self):
        for record in self:
            prestations = self.search([])
            record.total_prestations = len(prestations)
            durees = prestations.mapped('duree')
            record.avg_duree = sum(durees) / len(durees) if durees else 0.0

    @api.depends('service_type_id', 'duree')
    def _compute_price(self):
        for record in self:
            if record.service_type_id and record.duree:
                record.price = record.service_type_id.price_per_hour * record.duree
            else:
                record.price = 0.0
