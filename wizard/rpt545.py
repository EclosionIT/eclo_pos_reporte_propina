# -*- encoding: utf-8 -*-
##############################################################################
#
##############################################################################

import time
from datetime import datetime
from openerp.osv import osv, fields

class l10n_co_rpt545(osv.osv_memory):
	
	def _default_session_id(self,cr,uid,context=None):
		res = context.get('active_id')
		return res

	_name = 'eclo_545.rpt545'
	_columns = {
			'session_id':fields.many2one('pos.session',string='Pos',required=True),
			}
	_defaults = {
			}
	
	def action_report(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		data = {}
		data['ids'] = context.get('active_ids', [])
		data['model'] = context.get('active_model', 'ir.ui.menu')
		data['form'] = self.read(cr, uid, ids, ['session_id',], context=context)[0]
			
		return self.pool['report'].get_action(cr, uid, [], 'eclo_pos_reporte_propina.report_rpt545', data=data, context=context)