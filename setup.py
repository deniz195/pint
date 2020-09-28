#!/usr/bin/env python3
from setuptools import setup

def fixed_version(*args, **kwds):
    return '0.15.1'

def no_tag(*args, **kwds):
    return ''


if __name__ == "__main__":
    conf = dict(use_scm_version=dict(
            version_scheme=fixed_version,
            local_scheme=no_tag)
        )
    setup(**conf)
