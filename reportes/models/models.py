# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class ProductTemplate(models.Model):
	_inherit = "product.template"

	stock_gdl = fields.Integer(compute="_compute_stock_qty", string="Stock GDL")
	stock_cdmx = fields.Integer(compute="_compute_stock_qty", string="Stock CDMX")
	stock_mer = fields.Integer(compute="_compute_stock_qty", string ="Stock MER")
	stock_etgdl  = fields.Integer(compute="_compute_stock_qty", string="En tránsito GDL")
	stock_etcdmx  = fields.Integer(compute="_compute_stock_qty", string="En tránsito CDMX")
	stock_etmer  = fields.Integer(compute="_compute_stock_qty", string="En tránsito MER")

	@api.one
	def _compute_stock_qty(self):
		stock_warehouse_gdl = self.env['stock.warehouse'].search([('code', 'like', 'GDL')], limit=1)
		stock_warehouse_cdmx = self.env['stock.warehouse'].search([('code', 'like', 'CDMX')], limit=1)
		stock_warehouse_mer = self.env['stock.warehouse'].search([('code', 'like', 'MER')], limit=1)
		
		con = self.env.cr
		query_stock = "SELECT sum(product_qty) FROM stock_inventory_line WHERE product_id = %s AND location_id = %s"

		datos_gdl = (self.product_variant_id.id,stock_warehouse_gdl.lot_stock_id.id)
		datos_cdmx = (self.product_variant_id.id,stock_warehouse_cdmx.lot_stock_id.id)
		datos_mer = (self.product_variant_id.id,stock_warehouse_mer.lot_stock_id.id)
		

		con.execute(query_stock, datos_gdl)
		if con:
			row = con.fetchall()
			for x in row:
				self.stock_gdl = x[0]
		con.execute(query_stock, datos_cdmx)
		if con:
			row2 = con.fetchall()
			for x2 in row2:
				self.stock_cdmx = x2[0]
		con.execute(query_stock, datos_mer)
		if con:
			row3 = con.fetchall()
			for x3 in row3:
				self.stock_mer = x3[0]


'''class PurchaseOrder(models.Model):
	_inherit = "purchase.order"

	@api.multi
	def action_stock_et(self):
		for record in self:

			location_enau = self.env['stock.warehouse'].search([('code', '=', 'ENAU')], limit=1)
			location_eoc = self.env['stock.warehouse'].search([('code', '=', 'EOC')], limit=1)
			location_emer = self.env['stock.warehouse'].search([('code', '=', 'EMER')], limit=1)

			fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			fecha = datetime.now().strftime("%m/%d/%y")

			id_ref = 0

			if record.picking_type_id.default_location_dest_id.id == location_enau.lot_stock_id.id:
				id_ref = location_enau.lot_stock_id.id
			elif record.picking_type_id.default_location_dest_id.id == location_eoc.lot_stock_id.id:
				id_ref = location_eoc.lot_stock_id.id
			elif record.picking_type_id.default_location_dest_id.id == location_emer.lot_stock_id.id:
				id_ref = location_emer.lot_stock_id.id
			else:
				id_ref = 0	

			if id_ref != 0:
				if record.order_line:
					for line in record.order_line:
						nombre = line.product_id.name + ' - ' + fecha
						inventario_obj = self.env['stock.inventory']
						inventario_val = {
							'name': nombre,
							'date': fecha_hora,
							'state': 'done',
							'company_id': line.company_id.id,
							'location_id': id_ref,
							'product_id': line.product_id.id,
							'filter': 'product'
						}
						inventario_id = inventario_obj.create(inventario_val)
						if inventario_id:
							inventario_linea_obj = self.env['stock.inventory.line']
							inventario_linea_val = {
								'product_id': line.product_id.id,
								'product_uom_id': 1,
								'product_qty': line.product_uom_qty,
								'location_id': id_ref,
								'company_id': line.company_id.id
							}
							inventario_linea_id = inventario_linea_obj.create(inventario_linea_val)
	@api.multi
	def button_confirm(self):
		self.action_stock_et()
		return super(PurchaseOrder, self).button_confirm()		'''		
