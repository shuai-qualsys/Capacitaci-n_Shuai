from odoo import api, fields, models
from odoo.exceptions import UserError

class QualsysCourses(models.Model):
    _name = 'qualsys.courses'
    _description = 'Cursos'

    name = fields.Char(string='Nombre', required=True)
    duration = fields.Integer(string='Duratión en horas', required=True)
    start_date = fields.Date(string='Fecha de inicio', required=True)
    end_date = fields.Date(string='Fecha de termino', required=True)
    code = fields.Char(string='Codigo', required=True)
   
    attendees_ids = fields.One2many('qualsys.attendees', 'courses_id', string='Asistentes')
    teacher_id = fields.Many2one(comodel_name='res.users', string='Instructor')
    school_id = fields.Many2one(comodel_name='qualsys.school', string='Escuela')

    attendees_number = fields.Integer(string='No. Asistentes', compute="get_course_attendees")

    @api.depends('attendees_ids')
    def get_course_attendees(self):
        for data in self:
            data.attendees_number = len(data.attendees_ids)
    
    
    
    
    
    
    
