#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'neon_noise_level_plugin=neon_noise_level_plugin:BackgroundNoise'
setup(
    name='neon_noise_level_plugin',
    version='0.0.1',
    description='A audio parser/classifier/transformer plugin for ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/neon_noise_level_plugin',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='bsd3',
    packages=['neon_noise_level_plugin'],
    zip_safe=True,
    keywords='mycroft plugin audio parser/classifier/transformer',
    entry_points={'neon.plugin.audio': PLUGIN_ENTRY_POINT}
)
