# -*- coding: utf-8 -*-
from odoo import models, fields, api


class VacationSchedule(models.Model):
    _name = 'vacation.schedule'
    _description = "Vacation schedule"

    driver_id = fields.Many2one(
        comodel_name='res.partner',
        string='Driver',
        required=True,
    )

    start_date = fields.Date(
        string='Start date',
        required=True,
    )

    end_date = fields.Date(
        string='End date',
        required=True,
    )

    duration = fields.Float(
        compute='_compute_duration',
        string='Duration',
    )

    vacation_type = fields.Many2one(
        comodel_name='vacation.type',
        string='Type of holiday',
    )

    notes = fields.Char(
        string='Notes',
    )

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.end_date and record.start_date:
                record.duration = (record.end_date - record.start_date).days
            else:
                record.duration = 0
