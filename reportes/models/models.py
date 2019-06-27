# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
	_inherit ="product.template"

	stock_gdl = fields.Integer(compute="_compute_stock_qty")
	stock_mex = fields.Integer(compute="_compute_stock_qty")
	stock_mer = fields.Integer(compute="_compute_stock_qty")
	stock_et  = fields.Integer(compute="_compute_stock_qty")

	@api.one
	def _compute_stock_qty(self):
		stock_warehouse_gdl = self.env['stock.warehouse'].search([('code', 'like', 'GDL')], limit=1)
		stock_warehouse_mex = self.env['stock.warehouse'].search([('code', 'like', 'MEX')], limit=1)
		stock_warehouse_mer = self.env['stock.warehouse'].search([('code', 'like', 'MER')], limit=1)
		stock_warehouse_et  = self.env['stock.warehouse'].search([('code', 'like', 'ET')], limit=1)

		con = self.env.cr
		query_stock = "select product_qty from stock_inventory_line where product_id = %s and location_id = %s"

		datos_gdl = (self.product_variant_id.id,stock_warehouse_gdl.lot_stock_id.id)
		datos_mex = (self.product_variant_id.id,stock_warehouse_mex.lot_stock_id.id)
		datos_mer = (self.product_variant_id.id,stock_warehouse_mer.lot_stock_id.id)
		datos_et  = (self.product_variant_id.id,stock_warehouse_et.lot_stock_id.id)

		con.execute(query_stock, datos_gdl)
		if con:
			row = con.fetchall()
			for x in row:
				self.stock_gdl = x[0]
		con.execute(query_stock, datos_mex)
		if con:
			row2 = con.fetchall()
			for x2 in row2:
				self.stock_mex = x2[0]
		con.execute(query_stock, datos_mer)
		if con:
			row3 = con.fetchall()
			for x3 in row3:
				self.stock_mer = x3[0]
		con.execute(query_stock, datos_et)
		if con:
			row4 = con.fetchall()
			for x4 in row4:
				self.stock_et = x4[0]		