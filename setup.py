#!/usr/bin/env python

import os
from setuptools import setup, find_packages

# 讀取長描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 讀取版本
version = "0.1.0"

# 設置
setup(
    packages=find_packages(exclude=["tests*", "examples*"]),
)
