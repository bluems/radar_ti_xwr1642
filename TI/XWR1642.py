import serial
import time
import numpy as np


class XWR1642:
    def __init__(self, cfg_path='1642config.cfg'):
        self.cfg_path = cfg_path
        pass
