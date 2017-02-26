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

from odoo import api, fields, models
import pdb

# Tax Table for storing the various schedules of tables (e.g. No Tax Free,
# Tax Free, Foreign Resident, etc)

class HrPayrollTaxSchedule(models.Model):
	_name = 'hr.payroll.tax.schedule'
	_description = 'Australian tax table'
	
	name = fields.Char('Description', size=128)
	schedule = fields.Char('Tax Scale', size=10)
	paygw_scales = fields.One2many('hr.payroll.paygw.table','schedule','Tax Scales')

class HrEmployee(models.Model):
	_inherit = 'hr.employee'
		
	superfund = fields.Many2one('res.partner', 'Superannuation Fund')
	super_acct = fields.Char('Superannuation Account', size=50)
	taxtable = fields.Many2one('hr.payroll.tax.schedule','Tax Schedule')
	payslip_delivery = fields.Selection([('p','Print'),('e','Email'),('b','Both')], 'Payslip Delivery')	
	
	def calculate_paygw(self, date, taxinc):
		""" Return the amount of tax to be withheld for the employee for the
			requested date or false if no tax table defined
            

            :param date: date of the payment
            :param taxinc: taxable income for the period 
        """
		res = {}
		calcA = False
		calcB = False
#		for employees in self.browse(cr, uid, ids, context=context):
#			num = False
#			if employees.taxtable:
#				tax_tables = self.pool.get('hr.payroll.paygw.table')
#				for tax_table in tax_tables:
#					if tax_table.schedule.id == employees.taxtable.id:
#						for tax_rate in tax_table.line_ids:
#							if taxinc <= tax_rate.inc_to:
#								calcA = tax_rate.coeff_a
#								calcB = tax_rate.coeff_b
		
#		if (calcA and calcB):
#			res = (taxinc * calcA) - calcB
		res = 0.5								 
		return res

# Withholding table for a specific tax year

class HrPayrollPaygwTable(models.Model):
	_name = 'hr.payroll.paygw.table'
	_description = 'Australian PAYG Withholding Table'

	schedule = fields.Many2one('hr.payroll.tax.schedule', 'Tax Scale')
	name = fields.Char('Description', size=128)
	year = fields.Integer('Year', required=True)
	date_from = fields.Date('Date From')
	date_to = fields.Date('Date To')
	line_ids = fields.One2many('hr.payroll.paygw.table.line', 'table_id', 'Lines')
	
	@api.onchange('schedule','year')
	def change_year(self):
		if self.schedule:
			self.name = self.schedule.name
		else:
			self.name = ''
			
		if self.year:
			self.name += ' (' + str(self.year) + ')'
		
#	def onchange_year(self, cr, uid, ids, year, sched, context=None):
#		res = {}
#		if sched:
#			sched_obj = self.pool.get('hr.payroll.tax.schedule').browse(cr, uid, sched)
#			res['name'] = sched_obj.name
#		else:
#			res['name'] = ''
#		if year:
#			res['name'] += ' (' + str(year) + ')'
#		
#		return {'value': res}

class HrPayrollPaygwTableLine(models.Model):
	_name = 'hr.payroll.paygw.table.line'
	_description = 'PAYG Line'
	
	table_id = fields.Many2one('hr.payroll.paygw.table', 'Table')
	inc_from = fields.Float('Income From', digits=(16, 2), required=True)
	inc_to = fields.Float('Income To', digits=(16, 2), required=True)
	coeff_a = fields.Float('Coefficient (a)', digits=(16, 4))
	coeff_b = fields.Float('Coefficient (b)', digits=(16, 4))

#	_rec_name = 'inc_to'
