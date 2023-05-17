#!/usr/bin/env python
"""
Click application to parse firewall rules written for Terraform to look for
potential rules to deduplicate.
"""

import click
import hcl2


@click.group()
def firewall_cleaner():
    """Top-level command group
    """

@firewall_cleaner.command('gcp')
@click.option('--source', help='File containing compure firewall rules')
def gcp(source: str):
    """
    """
    pass
