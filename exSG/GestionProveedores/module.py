# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from types import *

""" CLASE PROVEEDOR """

class proveedor(osv.osv):

	_name = "proveedores.proveedor"
	_description = "Tabla con los proveedores"
	_columns = {
		'cif':fields.char('CIF',size=20, required=True),
		'nombre':fields.char('Nombre Comercial',size=100, required=True),
		'direccion':fields.char('Dirección', size=200, required=True),
		'telefono':fields.char('Teléfono', size=20),
	}

	# Orden para que nos muestre primero los últimos proveedores
	_order = 'id desc' 

	# Restricción única al campo NIF
	_sql_constraints = [
		('cif_unique', 'unique(cif)', 'El CIF debe ser único'),
	]

proveedor()
