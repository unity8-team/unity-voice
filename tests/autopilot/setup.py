#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#
# Unity Voice Autopilot Test Suite
# Copyright (C) 2013 Canonical
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup
from setuptools import find_packages

setup(
    name='unity-voice',
    version='1.0',
    description='Unity voice autopilot tests.',
    url='https://launchpad.net/unity-voice',
    license='GPLv3',
    packages=find_packages(),
)
