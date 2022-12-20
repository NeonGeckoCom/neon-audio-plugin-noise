# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2021 Neongecko.com Inc.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions
#    and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
#    and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written permission.
import wave

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from neon_transformers import AudioTransformer
import audioop
from math import log10
from neon_transformers.tasks import AudioTask


class BackgroundNoise(AudioTransformer):
    task = AudioTask.REMOVE_NOISE

    def __init__(self, config=None):
        super().__init__("background_noise", 10, config)

    @staticmethod
    def seconds_to_size(seconds):
        # 1 seconds of audio.frame_data = 44032
        return int(seconds * 44032)

    def noise_level(self):
        audio = self.noise_feed.read()
        # NOTE: might include a partial wake word at the end,
        # discard the last ~0.7 seconds of audio
        audio = audio[:-self.seconds_to_size(0.7)]
        rms = audioop.rms(audio, 2)
        if rms <= 0:
            return 0
        decibel = 20 * log10(rms)
        return decibel

    def transform(self, audio_data):
        return audio_data, {"noise_level": self.noise_level()}


def create_module(config=None):
    return BackgroundNoise(config=config)
