import serial
import time
import numpy as np


class XWR1642:
    cfg, cfg_path = [], ""

    def __init__(self, cfg_path=''):
        if cfg_path != '':
            self.input_config(cfg_path)
        pass

    def input_config(self, cfg_path):
        self.cfg_path = cfg_path

        for line in open(self.cfg_path):
            if line[0] != '%':
                self.cfg.append(line.rstrip('\r\n'))
        pass

    def print_config(self):
        for i in self.cfg:
            print(i)
            time.sleep(0.01)
