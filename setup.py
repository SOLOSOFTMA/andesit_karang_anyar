# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements

version = '0.0.1'
requirements = parse_requirements("requirements.txt", session="")

setup(
	name='andesit_karang_anyar',
	version=version,
	description='ERPNext customization for Andesit Karang Anyar',
	author='MN Technique',
	author_email='support@castlecraft.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)