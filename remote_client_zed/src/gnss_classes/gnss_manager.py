"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
        Code converted to OOP and adapted from original functions made by https://github.com/Jordi-Gene-Mola


Date: August 2021
Description: Manage GNSS ArduSimple functions

Use:
    gnss_config_obj = GNSSConfig(path_config_gnss_file)
    gnss_obj = GNSSManager(gnss_config_obj)

"""

import logging
import serial
from gnss_classes.gnss_config import GNSSConfig
from gnss_classes.nmea_classes import NMEAMessages
from gnss_classes.nmea_classes import RMCMessage
from gnss_classes.nmea_classes import GGAMessage
from gnss_classes.nmea_classes import GeoPoint
from datetime import datetime


class GNSSManager:
    _gnss_config = None
    _GGA_line = ''  # To store the data of the measurement
    _gnss_read_ID = 0  # To keep track of the step
    flag_enabled = True

    def __init__(self, config_param):
        logging.debug('STARTING GNSS MANAGER')

        if config_param is None:
            logging.debug('config_param is empty')
            self._gnss_config = GNSSConfig()  # by default
        else:
            self._gnss_config = config_param

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
                print("Error. Ardusimple not available!", e.with_traceback())
                self.flag_enabled = False

    def read_raw_line(self, nmea_message_id):
        logging.info("SOMETHING")
        while 1:
            raw_line = self.ser.readline().decode('ascii', errors='replace')
            if nmea_message_id in raw_line:
                break
        return raw_line

    def read_lines_to_file(self, track_file, nmea_message_id):
        f1 = open(track_file, 'a')
        gnss_read_ID = 0
        while 1:
            try:
                line = self.ser.readline().decode('ascii', errors='replace')
                # $GNGGA,102646.00,4136.99658,N,00037.05311,E,1,12,0.65,182.9,M,49.8,M,,*4B
                if nmea_message_id in line:
                    gnss_read_ID += 1
                    utc_time = datetime.utcnow()
                    print('\n' + 'GNSS read: ' + str(gnss_read_ID) + ' ; ' + line[:-2])
                    f1.write(line[:-2] + ',' + str(utc_time) + '\r\n')
            except KeyboardInterrupt:
                break
        f1.close()

    def get_file_str(self):
        rmc_line = self.read_rmc_line()
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

    def encode_raw_rmc(self, rmc_line):
        # NMEA 4.10
        # https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
        # $GNRMC,120238.00,A,4136.99420,N,00037.05325,E,0.032,,170821,,,A,V*11
        line_rmc_list = rmc_line.split(",")
        rmc_obj = RMCMessage()
        rmc_obj.nmea_id = line_rmc_list[0]
        rmc_obj.utc_time = line_rmc_list[1][:6]  #
        rmc_obj.status = line_rmc_list[2]
        rmc_obj.latitude = line_rmc_list[3]
        rmc_obj.latitude_indicator = line_rmc_list[4]
        rmc_obj.longitude = line_rmc_list[5]
        rmc_obj.longitude_indicator = line_rmc_list[6]
        rmc_obj.speed_over_ground = line_rmc_list[7]
        rmc_obj.course_over_ground = line_rmc_list[8]
        rmc_obj.utc_date = line_rmc_list[9]  # ddmmyy
        rmc_obj.magnetic_variation = line_rmc_list[10]
        rmc_obj.magnetic_variation_indicator = line_rmc_list[11]
        rmc_obj.mode = line_rmc_list[12]
        rmc_obj.checksum = line_rmc_list[13]

        return rmc_obj

    def encode_raw_gga(self, gga_line):
        # NMEA 4.10
        # https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
        # $GNGGA,132801.10,4136.99614,N,00037.05381,E,1,12,0.80,199.8,M,49.8,M,,*45
        line_gga_list = gga_line.split(",")
        print(line_gga_list)
        gga_obj = GGAMessage()
        gga_obj.nmea_id = line_gga_list[0]
        gga_obj.utc_time = line_gga_list[1]
        gga_obj.latitude = line_gga_list[2]
        gga_obj.latitude_indicator = line_gga_list[3]
        gga_obj.longitude = line_gga_list[4]
        gga_obj.longitude_indicator = line_gga_list[5]
        gga_obj.position_fix_indicator = line_gga_list[6]
        gga_obj.satellites_used = line_gga_list[7]
        gga_obj.hdop = line_gga_list[8]
        gga_obj.msl_altitude = line_gga_list[9]
        gga_obj.msl_units = line_gga_list[10]
        gga_obj.geoid_separation = line_gga_list[11]
        gga_obj.geoid_units = line_gga_list[12]
        gga_obj.age_of_diff_corr = line_gga_list[13]
        gga_obj.checksum = line_gga_list[14][:3]
        return gga_obj

    def get_position(self):
        geo_position_obj = GeoPoint()
        # todo: to implement
        print("get_position(self)-->")
        raw_gga_line = self.read_raw_line(NMEAMessages.GGA)
        line_geopoint_list = raw_gga_line.split(",")
        geo_position_obj = GGAMessage()
        geo_position_obj.utc_time = line_geopoint_list[1]
        geo_position_obj.latitude = line_geopoint_list[2]
        geo_position_obj.latitude_indicator = line_geopoint_list[3]
        geo_position_obj.longitude = line_geopoint_list[4]
        geo_position_obj.longitude_indicator = line_geopoint_list[5]
        geo_position_obj.position_fix_indicator = line_geopoint_list[6]
        geo_position_obj.satellites_used = line_geopoint_list[7]
        geo_position_obj.msl_altitude = line_geopoint_list[9]
        geo_position_obj.msl_units = line_geopoint_list[10]

        return geo_position_obj
