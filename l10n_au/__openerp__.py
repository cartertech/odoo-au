# -*- encoding: utf-8 -*-
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
{
    'name': 'Australia - Accounting',
    'version': '0.1',
    'author': 'One Click Software',
    'website': 'http://oneclick.solutions',
    'category': 'Localization/Account Charts',
    'description': """
This is the module to manage the Australian accounting chart in Odoo.
===========================================================================================

Australian accounting charts.

Limitations
------------
The chart of accounts currently includes an item for WET but there is no WET in the tax chart.

    """,
    'depends': [
        'base',
        'account',
        'base_iban',
        'account_chart',
		'account_anglo_saxon'
    ],
    'data': [
        'account_chart.xml',
        'account_tax_code.xml',
        'account_chart_template.xml',
        'account_tax.xml',
        'l10n_au_wizard.xml'
    ],
    'demo': [],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

