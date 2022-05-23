# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TourPlan(models.Model):
    _name = 'tour.plan'
    _description = "Tour Plan"

    name = fields.Char(
        required=True,
    )

    tour_number = fields.Integer(
        string='Tour number',
    )

    start_date = fields.Date(
        string='Start date',
        default=fields.Date.context_today,
    )

    is_recurring_event = fields.Boolean(
        string='Recurring event',
        default=False,
    )

    is_recurring_monday = fields.Boolean(
        string='Recurring event Monday',
        default=True,
    )

    is_recurring_tuesday = fields.Boolean(
        string='Recurring event Tuesday',
        default=True,
    )

    is_recurring_wednesday = fields.Boolean(
        string='Recurring event Wednesday',
        default=True,
    )

    is_recurring_thursday = fields.Boolean(
        string='Recurring event Thursday',
        default=True,
    )

    is_recurring_friday = fields.Boolean(
        string='Recurring event Friday',
        default=True,
    )

    is_recurring_saturday = fields.Boolean(
        string='Recurring event Saturday',
        default=False,
    )

    is_recurring_sunday = fields.Boolean(
        string='Recurring event Sunday',
        default=False,
    )

    end_date = fields.Date(
        string='End date',
        default=fields.Date.context_today,
    )

    duration = fields.Float(
        compute='_compute_duration',
        string='Duration',
    )

    route_length = fields.Integer(
        string='Route length',
    )

    driver_id = fields.Many2one(
        related='fleet_vehicle_id.driver_id',
        string='Driver',
    )

    fleet_vehicle_id = fields.Many2one(
        comodel_name='fleet.vehicle',
        string='Fleet vehicle',
    )

    is_driver_lunch_break_included = fields.Boolean(
        string='Is_driver_lunch_break_included',
    )

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.end_date and record.start_date:
                record.duration = (record.end_date - record.start_date).days
            else:
                record.duration = 0
