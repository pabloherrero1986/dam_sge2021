# -*- coding: utf-8 -*-

from odoo import models, fields, api


class panaderia_categoria(models.Model):
     _name = 'panaderia.categoria'

     name = fields.Char('Nombre', required=True, help='introduce el nombre de la categoría')
     description = fields.Text('Descripción')
     panes = fields.One2many('panaderia.pan','categoria','Panes')

class panaderia_pan(models.Model):
     _name = 'panaderia.pan'

     name = fields.Char('Variedad', required=True)
     precio = fields.Float('Precio')
     ejemplares = fields.Integer('Ejemplares')
     fecha = fields.Date('Fecha de compra')
     segmano = fields.Boolean('Segunda mano')
     estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],'Estado', default='0')
     categoria = fields.Many2one('panaderia.categoria','Categoría',required=True,ondelete='cascade')
     importetotal = fields.Float(string="Importe Total", compute="_importetotal", store=True)

     @api.depends('precio','ejemplares')
     def _importetotal(self):
         for r in self:
             r.importetotal = r.ejemplares*r.precio


# class panaderia(models.Model):
#     _name = 'panaderia.panaderia'
#     _description = 'panaderia.panaderia'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
