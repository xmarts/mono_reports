# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ReportStock(models.TransientModel):
	_name = "wizard.report.stock"

	type_report = fields.Selection( [('category','Categoria'),('product','Producto'),('stock','Almacen'),('all','General')], strting="Tipo de reporte" )
	type_category = fields.Many2one('product.category', string="Categoria de producto")
	type_stock = fields.Many2one('stock.location', string="Ubicacion de inventario")

	def open_table(self):
		self.ensure_one()

		if self.type_report:
			dom = []
			title_sel = ""
			if self.type_report == 'category':
				dom = [('categ_id','=', self.type_category.id)]
				title_sel = ' por Categoria'
			elif self.type_report == 'product' :
				dom = [('type','=','product')]
				title_sel = ' por Producto'
			elif self.type_report == 'stock' :
				dom = [('property_stock_inventory','=',self.type_stock.id)]
				title_sel = ' por Inventario'
			else:
				dom = []
				title_sel = 'General'

			tree_view_id = self.env.ref('product.product_template_tree_view').id
			form_view_id = self.env.ref('product.product_template_only_form_view').id
			# We pass `to_date` in the context so that `qty_available` will be computed across
			# moves until date.
			action = {
				'type': 'ir.actions.act_window',
				'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
				'view_mode': 'tree,form',
				'name': _('Reporte' + str(title_sel)),
				'res_model': 'product.template',
				#"'context': dict(self.env.context, to_date=self.date),
				'domain':  dom
			}
			return action
		else:
			self.env['stock.quant']._merge_quants()
			return self.env.ref('stock.quantsact').read()[0]