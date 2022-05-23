# -*- coding: utf-8 -*-
from odoo import models, fields, api


class BasicPlanning(models.Model):
    _name = 'basic.planning'
    _description = "Basic planning"

    tour_id = fields.Many2one(
        comodel_name='tour.plan',
        string='Tour',
    )

    driver_id = fields.Many2one(
        string='Driver',
        related='tour_id.driver_id',
        readonly=True,
    )

    tour_number = fields.Integer(
        string='Tour number',
        related='tour_id.tour_number',
        readonly=True,
    )

    start_date = fields.Date(
        string='Start date',
    )

    end_date = fields.Date(
        string='End date',
    )

    route_length = fields.Integer(
        string='Route length',
        related='tour_id.route_length',
        readonly=True,
    )

    fleet_vehicle_id = fields.Many2one(
        comodel_name='fleet.vehicle',
        string='Fleet vehicle',
        related='tour_id.fleet_vehicle_id',
        readonly=True,
    )

    is_driver_lunch_break_included = fields.Boolean(
        string='Is_driver_lunch_break_included',
        related='tour_id.is_driver_lunch_break_included',
        readonly=True,
    )
