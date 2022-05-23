# -*- coding: utf-8 -*-
from odoo import models, fields


class VacationType(models.Model):
    _name = 'vacation.type'
    _description = "Vacation type"

    name = fields.Char(
        required=True,
    )
