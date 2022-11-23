from odoo import api, fields, models
from odoo.exceptions import UserError
#nuevo modelo con om

class QualsysAttendees(models.Model):
    _name = 'qualsys.attendees'
    _description = 'Alumnos'


    name = fields.Char(string='Nombre', required=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='ID. Asistente')
    courses_id = fields.Many2one(comodel_name='qualsys.courses', string='Curso')
    
    age = fields.Integer(string='Edad', required=True)

    
    

    
    
    
    
    
    
