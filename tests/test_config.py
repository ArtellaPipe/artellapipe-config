#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tests for artellapipe-config
"""

import pytest


def test_version():
    from artellapipe.config import __version__
    assert __version__.__version__
