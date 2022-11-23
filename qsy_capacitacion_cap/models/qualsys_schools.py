from odoo import api, fields, models
from odoo.exceptions import UserError

class QualsysSchool(models.Model):
    _name = 'qualsys.school'
    _description = 'Escuelas'

    name = fields.Char(string="Nombre", required=True)
    street = fields.Char(string="Calle")
    street_number = fields.Char(string="No. Ext.")
    city = fields.Char(string="Ciudad", required=True)
    state = fields.Many2one(string="Estado", comodel_name='res.country.state', required = True)
    country = fields.Many2one(string="Pais", comodel_name='res.country', required = True)
    phone_one = fields.Char(string="Teléfono Uno", required=True)
    phone_two = fields.Char(string="Teléfono Dos")
    email = fields.Char(string="Correo", required = True)
    courses_number = fields.Integer(string="No. Cursos", compute = 'get_courses_number')
    courses_ids = fields.One2many(comodel_name='qualsys.courses', inverse_name='school_id', string='Curso', required = True)
    
    @api.depends('courses_ids')
    def get_courses_number(self):
      for data in self:
        data.courses_number = len(data.courses_ids)




