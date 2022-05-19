# -*- coding: utf-8 -*-
from odoo import models, fields


class DriverBreak(models.Model):
    _name = 'driver.break'
    _description = "Driver break"

    name = fields.Char(
        required=True,
    )
