#-*- coding:utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2014 One Click Software (<http://oneclick.solutions>)
#	 Contributed to the Odoo - Australian localisation project
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm

class hr_contract_au(orm.Model):
	_inherit = 'hr.contract'

	_columns = {
		'terms_type': fields.selection([('Award',1),('Enterprise Agreement',2),('Contract',3),('Other',4)], 'Source of Employment Terms'),
		'terms_doc': fields.char('Employment Terms Document',size=128),
		'terms_class': fields.char('Position Classification',size=128),
    }

hr_contract_au()

class hr_payroll_tax_table(orm.Model):
	_name = 'hr.payroll.tax.table'
	_description = 'Australian tax table'
	
	_columns = {
	'name': fields.char('Description', size=128),
	}
	
hr_payroll_tax_table()

class hr_employee_au(orm.Model):
	_inherit = 'hr.employee'
	_columns = {
		'superfund': fields.many2one('res.partner', 'Superannuation Fund'),
		'super_acct': fields.char('Superannuation Account', size=50),
		'taxtable': fields.many2one('hr.payroll.tax.table','Tax Table'),
		'payslip_delivery': fields.selection([('Print',1),('Email',2),('Both',3)], 'Payslip Delivery'),
  }

hr_employee_au()

class hr_payroll_paygw_table(orm.Model):
	_name = 'hr.payroll.paygw.table'
	_description = 'Australian PAYG Withholding Table'
      
	_columns = {
		'name': fields.char('Description', size=128),
		'year': fields.integer('Year', required=True),
		'date_from': fields.date('Date From'),
		'date_to': fields.date('Date To'),
		'line_ids': fields.one2many('hr.payroll.paygw.table.line', 'table_id', 'Lines'),
		}


class hr_payroll_paygw_table_line(orm.Model):
	_name = 'hr.payroll.paygw.table.line'
	_description = 'PAYG Line'
	_columns = {
		'table_id': fields.many2one('hr.payroll.paygw.table', 'Table'),
		'inc_from': fields.float('Income From', digits=(16, 2), required=True),
		'inc_to': fields.float('Income To', digits=(16, 2), required=True),
		'coeff_a': fields.float('Coefficient (a)', digits=(16, 2)),
		'coeff_b': fields.float('Coefficient (b)', digits=(16, 2)),
		}

	_rec_name = 'inc_from'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
