"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description: NMEA types and data format

Use:

"""


# NMEA National Marine Electronics Association https://www.nmea.org/
# https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
# https://www.olaje.com/documentos/MN000315E_NMEA_ref_manual.pdf

class NMEAMessages:
    GGA = "GGA"
    GLL = "GLL"
    GSA = "GSA"
    GSV = "GSV"
    MSS = "MSS"
    RMC = "RMC"
    VTG = "VTG"
    ZDA = "ZDA"
    OK = "150"


class RMCMessage:
    # https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
    nmea_id = None
    utc_time = None
    status = None
    latitude = None
    latitude_indicator = None
    longitude = None
    longitude_indicator = None
    speed_over_ground = None
    course_over_ground = None
    utc_date = None
    magnetic_variation = None
    magnetic_variation_indicator = None
    mode = None
    checksum = None

    def __str__(self):
        # print(self.nmea_id, self.utc_time, self.status, self.latitude, self.latitude_indicator,
        #      self.longitude, self.longitude_indicator, self.speed_over_ground, self.course_over_ground, self.utc_date,
        #      self.magnetic_variation, self.magnetic_variation_indicator, self.mode, self.checksum)
        return str(self.nmea_id)


class GGAMessage:
    # https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
    nmea_id = None
    utc_time = None
    latitude = None
    latitude_indicator = None
    longitude = None
    longitude_indicator = None
    position_fix_indicator = None
    satellites_used = None
    hdop = None
    msl_altitude = None
    msl_units = None
    geoid_separation = None
    geoid_units = None
    age_of_diff_corr = None
    diff_ref_station = None
    checksum = None

    def __str__(self):
        print(self.nmea_id, self.utc_time, self.latitude, self.latitude_indicator, self.longitude,
              self.longitude_indicator, self.position_fix_indicator, self.satellites_used, self.hdop, self.msl_altitude,
              self.msl_units, self.geoid_separation, self.geoid_units, self.age_of_diff_corr, self.diff_ref_station,
              self.checksum)


class GGAMessage:
    # https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
    nmea_id = None
    utc_time = None
    latitude = None
    latitude_indicator = None
    longitude = None
    longitude_indicator = None
    position_fix_indicator = None
    satellites_used = None
    hdop = None
    msl_altitude = None
    msl_units = None
    geoid_separation = None
    geoid_units = None
    age_of_diff_corr = None
    diff_ref_station = None
    checksum = None


class GeoPoint:
    # https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual1.pdf
    utc_time = None
    latitude = None
    latitude_indicator = None
    longitude = None
    longitude_indicator = None
    position_fix_indicator = None
    satellites_used = None
    msl_altitude = None
    msl_units = None

    def __str__(self):
        geo_string = str(self.utc_time) + ", " + str(self.latitude) + ", " + str(self.latitude_indicator) + ", " + str(
            self.longitude) + ", " + str(self.longitude_indicator) + ", " + str(
            self.position_fix_indicator) + ", " + str(self.satellites_used) + ", " + str(
            self.msl_altitude) + ", " + str(self.msl_units)
        return geo_string
