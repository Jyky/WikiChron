#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   __init__.py

   Defines metrics package and init public list: available_metrics.

   Created on: 15-nov-2017

   Copyright 2017 Abel 'Akronix' Serrano Juste <akronix5@gmail.com>
"""

from .metrics_generator import generate_metrics, generate_dict_metrics, generate_metric_category_names

print('Generating available metrics...')
available_metrics = generate_metrics()
metrics_dict = generate_dict_metrics(available_metrics)
metric_category_names = generate_metric_category_names()
