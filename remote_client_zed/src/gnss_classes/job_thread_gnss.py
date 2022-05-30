"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
        Code converted to OOP and adapted from original functoins made by https://github.com/Jordi-Gene-Mola


Date: August 2021
Description:

    This is an wrapper to use Ardusimple GNSS functions as a thread process
    This class is used when we need to launch process  from loops as
    a remote client. Methods are similar to gnss_manager.py


Usage:
        gnss_config_obj = GNSSConfig(path_gnss_config_file)
        job_thread_gnss = JobThreadGNSS(gnss_config_obj)

"""

import os
import threading
import logging
import serial
from datetime import datetime
from gnss_classes.gnss_config import GNSSConfig
from gnss_classes.nmea_classes import NMEAMessages


class JobThreadGNSS(threading.Thread):
    _gnss_config = None
    _GGA_line = ''  # To store the data of the measurement
    _gnss_read_ID = 0  # To keep track of the step
    flag_enabled = True

    def __init__(self, gnss_config_param):
        logging.debug('STARTING GNSS MANAGER')

        if gnss_config_param is None:
            logging.debug('config_param is empty')
            self._gnss_config = GNSSConfig()  # by default
        else:
            self._gnss_config = gnss_config_param

        self.GGA_line = ''  # To store the data of the measurement
        self.gnss_read_ID = 0  # To keep track of the step
        try:
            self.ser = serial.Serial(self._gnss_config.serial_port_master, self._gnss_config.baudrate)
            print(f"Ardu simple detected in {self._gnss_config.serial_port_master}")
        except Exception as e:
            print(f"Error. Ardusimple not available in {self._gnss_config.serial_port_master}!")
            print(f"Checking in alternative port {self._gnss_config.serial_port_alternative}!")
            try:
                self.ser = serial.Serial(self._gnss_config.serial_port_alternative, self._gnss_config.baudrate)
            except Exception as e:
                # print("Error. Ardusimple not available!", e.with_traceback())
                self.flag_enabled = False
                os.exit(1)  # todo check this
        finally:
            if self.flag_enabled is True:
                threading.Thread.__init__(self)
                self.shutdown_flag = threading.Event()
            else:
                print("False ->")

    def read_raw_line(self, nmea_message_id):
        # logging.info("GNSS - READ A LINE")
        while 1:
            raw_line = self.ser.readline().decode('ascii', errors='replace')
            if nmea_message_id in raw_line:
                break
        return raw_line

    def get_file_str(self):
        rmc_line = self.read_raw_line(NMEAMessages.RMC)
        line_list = rmc_line.split(",")
        gnss_year = line_list[9][-2:]
        gnss_month = line_list[9][2:4]
        gnss_day = line_list[9][:2]
        gnss_utc_time = line_list[1][:6]  # equivalent to line_list[1][:-3]
        gnss_utc_date = line_list[9][:6]

        logging.debug('gnss_year: ' + gnss_year)
        logging.debug('gnss_month: ' + gnss_month)
        logging.debug('gnss_day: ' + gnss_day)
        logging.debug('gnss_utc_time: ' + gnss_utc_time)
        logging.debug('gnss_utc_date: ' + gnss_utc_date)

        file_str = gnss_year + gnss_month + gnss_day + '_' + gnss_utc_time

        return file_str

    def run(self):
        print('GNSS - STARTED #%s' % self.ident)
        logging.info('GNSS - STARTED #%s' % self.ident)
        line = self.ser.readline().decode('ascii', errors='replace')
        logging.info(f'GNSS - #{line[:-2]}')

        file_name_datestr = self.get_file_str()
        print("-->", self._gnss_config.path_gnss_output_file)
        print("file_name_datestr-->", file_name_datestr)
        print("self._gnss_config.file_name-->", self._gnss_config.file_name)
        track_file = os.path.join(self._gnss_config.path_gnss_output_file,
                                  file_name_datestr + self._gnss_config.file_name)
        f1 = open(track_file, 'a')
        gnss_read_ID = 0
        while not self.shutdown_flag.is_set():
            try:
                line = self.ser.readline().decode('ascii', errors='replace')
                if NMEAMessages.GGA in line:
                    gnss_read_ID += 1
                    utc_time = datetime.utcnow()
                    # logging.info(f'GNSS - #{line[:-2]}')
                    # print('GNSS read: ' + str(gnss_read_ID) + ' ; ' + line[:-2])
                    f1.write(line[:-2] + ',' + str(utc_time) + '\r\n')
            except KeyboardInterrupt:
                break
        # ... Clean shutdown code here ...
        print(f'GNSS - STOPPED #{self.ident}')
        logging.info(f'GNSS - STOPPED #{self.ident}')
        logging.info(f'GNSS - #{line[:-2]}')
        f1.close()
