#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tests for artellapipe-config
"""

import os
import sys
import pytest

source_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'source')
if source_path not in sys.path:
    sys.path.append(source_path)

from artellapipe.config import __version__


def test_version():
    assert __version__.__version__
