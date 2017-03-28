# -*- coding: utf-8 -*-
##############################################################################
#
#   HR Account Move Cancel
#   Copyright 2017 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "HR Account Move Cancel",
    'version': '1.0',
    'depends': ['hr_expense'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'HR',

    'summary': """Account Move Cancel""",

    'description': """
HR Account Move Cancel
======================

This module allows to move entry from waiting paiment and paid to draft.
    """,

    'data': [
        'views/hr_expense_view.xml',
        'views/hr_expense_workflow.xml',
    ],

    'demo': [
    ],

}
