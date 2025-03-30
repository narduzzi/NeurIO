#!/user/bin/env python

"""
Author: Simon Narduzzi
Email: simon.narduzzi@csem.ch
Copyright: CSEM, 2025
Creation: 30.03.2025
Description: TODO
"""
#!/user/bin/env python

"""
Author: Simon Narduzzi
Email: simon.narduzzi@csem.ch
Copyright: CSEM, 2023
Creation: 15.01.2024
Description: Time monitor for phases recording, to be used with external tools
"""

import json
import os

import time
import struct
import logging


class TimeMonitor:
    """
    Class that can be used to record the power consumption of a device using the Power Profiler Kit II from Nordic.
    """

    def __init__(self,verbose: int = 0, log_dir: str = None, **kwargs):
        self.recordings = []
        self.verbose = verbose
        if log_dir is None:
            log_dir = os.path.join("logs-{}".format(time.strftime("%Y%m%d-%H%M%S")))
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.phase = None
        self.running = False



    def start(self, phase: str):
        """
        Start recording the power consumption of the device for a given phase.
        :param phase: name of the phase
        """
        # launch a thread that acquires data
        if self.running:
            raise Exception("Already recording. Stop first")
        else:
            self.phase = phase
            self.recording = {"phase": phase, "start_timestamp": time.time()}


    def stop(self):
        """
        Stop recording the power consumption of the device.
        """
        self.recording["stop_timestamp"] = time.time()
        self.running = False
        # get samples from kit
        self.recordings.append(self.recording)

        with open(os.path.join(self.log_dir, "time_recording.json"), "w") as f:
            json.dump(self.recordings, f)
