import os
import sys
import json
import re


def collect_ids(new_id, ids=[]):
    ids.append(new_id)
    return ids


def build_report(rows):
    report = ""
    for row in rows:
        report = report + str(row) + "\n"
    return report


def load_config(path):
    try:
        f = open(path)
        data = f.read()
        return data
    except:
        return None


def check_status(value):
    if value == None:
        return "unknown"
    return "ok"
