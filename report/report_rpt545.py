# -*- encoding: utf-8 -*-
##############################################################################
#
#
#    
#    eclo_545  rpt545 
##############################################################################

import time
from datetime import datetime
from openerp.osv import osv
from openerp.report import report_sxw

class rpt545_print(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context=None):
		if context is None:
			context = {}
		super(rpt545_print, self).__init__(cr, uid, name, context=context)
		self.session_id = None
		self.lines = None
		self.localcontext.update({
			'time': time,
			'date_long': self._date_long,
			'get_session': self._get_session,
			'get_lines': self._get_lines,
		})
		
	def set_context(self, objects, data, ids, report_type=None):
		return super(rpt545_print, self).set_context(objects, data, ids, report_type=report_type)
	
	def _date_long(self, d):
		mes = {'01':'enero','02':'febrero','03':'marzo','04':'abril','05':'mayo','06':'junio',
			   '07':'julio','08':'agosto','09':'setiembre','10':'octubre','11':'noviembre','12':'diciembre'}
		return "%s de %s del %s"%(d[8:],mes[d[5:7]],d[0:4])
			
	def _get_lines(self, data, session_id):

#  Formas de pago
		cp=[0]
		cp[0]=session_id 
		self.lines = []
		q='''select b.name, a.name, sum(price_subtotal) 
		from pos_config a, pos_session b, pos_order c, pos_order_line  d
			where b.config_id=a.id and b.id = c.session_id and d.order_id= c.id  and d.product_id= discount_product_id
			and b.id=%s
			group by b.name, a.name'''

		self.cr.execute(q, (session_id, ))	
		for l in self.cr.fetchall():
			line=(l[0], l[1], l[2],) 
			self.lines.append(line)

		return self.lines


	def _get_session(self, data, objects):
		
		if data and data.get('form', False):
			if data.get('model', False)=='pos.session' and data.get('ids',False):
				session_ids = data.get('ids',[])
			else: 
				session_ids = [data['form'].get('session_id')[0]]
		else:
			session_ids = [p.id for p in objects]
		self.session = self.pool.get('pos.session').browse(self.cr, self.uid, session_ids)
	
		return self.session

class report_rpt545(osv.AbstractModel):
	_name = 'report.eclo_pos_reporte_propina.report_rpt545'
	_inherit = 'report.abstract_report'
	_template = 'eclo_pos_reporte_propina.report_rpt545'
	_wrapped_report_class = rpt545_print

