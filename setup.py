#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'neon_audio_noise_plugin=neon_audio_noise_plugin:BackgroundNoise'
setup(
    name='neon_audio_noise_plugin',
    version='0.0.1',
    description='A audio parser/classifier/transformer plugin for ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/neon_audio_noise_plugin',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='bsd3',
    packages=['neon_audio_noise_plugin'],
    zip_safe=True,
    keywords='mycroft plugin audio parser/classifier/transformer',
    entry_points={'neon.plugin.audio': PLUGIN_ENTRY_POINT}
)
