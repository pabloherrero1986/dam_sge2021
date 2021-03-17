# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libreria_categoria(models.Model):
     _name = 'libreria.categoria'
    
     name = fields.Char('Nombre', required=True, help='introduce el nombre de la categoría')     
     description = fields.Text('Descripción')
     libros = fields.One2many('libreria.libro','categoria','Libros')

class libreria_libro(models.Model):
     _name = 'libreria.libro'
    
     name = fields.Char('Título', required=True)     
     precio = fields.Float('Precio')
     ejemplares = fields.Integer('Ejemplares')     
     fecha = fields.Date('Fecha de compra')
     segmano = fields.Boolean('Segunda mano')     
     estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],'Estado', default='0')
     categoria = fields.Many2one('libreria.categoria','Categoría',required=True,ondelete='cascade')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
