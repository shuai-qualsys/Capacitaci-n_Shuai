from odoo import fields, models


class WizardAssingAttendees(models.TransientModel):
    _name = 'wizard.assing.attendees'
    _description = 'Asignación de asistentes a cursos'

    attendees_id = fields.Many2one(comodel_name='qualsys.attendees', string='Asistente a asociar')

    def asignador(self):
        for record in self:
            curso_id = int(self.env.context.get('active_id', False))    
            record.attendees_id.courses_id = curso_id