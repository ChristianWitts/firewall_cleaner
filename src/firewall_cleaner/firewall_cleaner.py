#!/usr/bin/env python
"""
Click application to parse firewall rules written for Terraform to look for
potential rules to deduplicate.
"""

from pprint import PrettyPrinter

import click
import hcl2

PP = PrettyPrinter(indent=2)


@click.group()
def firewall_cleaner():
    """Top-level command group"""


@firewall_cleaner.command("gcp")
@click.option("--source", help="File containing compure firewall rules")
def gcp(source: str):
    """ """
    with open(source, "r") as fin:
        data = hcl2.load(fin)

    for fw in data["resource"]:
        tags = get_tags(get_inner_dict(fw["google_compute_firewall"]))
        PP.pprint(tags)


def get_tags(d):
    return d.get("target_tags", [[]])[0]


def get_inner_dict(d):
    k = list(d.keys())[0]
    return d[k]
