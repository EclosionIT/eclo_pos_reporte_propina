# -*- encoding: utf-8 -*-
##############################################################################
#
#
##############################################################################
{
	"name": "Reporte Session POS Propinas",
	"version": "1.0",
	"description": """
Imprime por Session el total de propina

Key Features
------------
* rpt545  form
	""",
	"author": "Eclosion ",
	"website": "http://www.eclosionit.com",
	"category": "pos",
	"depends": [
			"point_of_sale",
			"base",
			],
	"data":[
			"wizard/rpt545_view.xml",
			"rpt545_cfg.xml",
			"report/report_rpt545.xml",
			],
}