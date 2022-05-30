"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Helper to load camera config from files

Use:
    import helpers.helper_zed_load_config as hc
    my_zed_device_configuration = hc.load_zed_config_from_file(path_conf_file_zed)

"""

import configparser
import pyzed.sl as sl
from pyzed.sl import FLIP_MODE, COORDINATE_SYSTEM, UNIT, DEPTH_MODE

def convert_flip_mode(convert_param):
    camera_image_flip = None
    if convert_param == 'FLIP_MODE.AUTO':
        camera_image_flip = FLIP_MODE.AUTO
    elif convert_param == 'FLIP_MODE.OFF':
        camera_image_flip = FLIP_MODE.OFF
    elif convert_param == 'FLIP_MODE.ON':
        camera_image_flip = FLIP_MODE.ON
    return camera_image_flip

def convert_camera_resolution(convert_param):
    # TODO: check resolution references, actually we make calling sl.RESOLUTION
    camera_resolution = None
    if convert_param == 'RESOLUTION.HD720':
        camera_resolution = sl.RESOLUTION.HD720
    elif convert_param == 'RESOLUTION.HD1080':
        camera_resolution = sl.RESOLUTION.HD1080
    elif convert_param == 'RESOLUTION.HD2K':
        camera_resolution = sl.RESOLUTION.HD2K
    return camera_resolution

def convert_coordinate_system(convert_param):
    # add here other configurations from InitParameters Zed SDK
    coordinate_system = None
    if convert_param == 'COORDINATE_SYSTEM.IMAGE':
        coordinate_system = COORDINATE_SYSTEM.IMAGE
    elif convert_param == 'LAST':
        coordinate_system = COORDINATE_SYSTEM.LAST
    elif convert_param == 'LEFT_HANDED_Y_UP':
        coordinate_system = COORDINATE_SYSTEM.LEFT_HANDED_Y_UP
    elif convert_param == 'LEFT_HANDED_Z_UP':
        coordinate_system = COORDINATE_SYSTEM.LEFT_HANDED_Z_UP
    elif convert_param == 'RIGHT_HANDED_Y_UP':
        coordinate_system = COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP
    elif convert_param == 'RIGHT_HANDED_Z_UP':
        coordinate_system = COORDINATE_SYSTEM.RIGHT_HANDED_Z_UP
    elif convert_param == 'RIGHT_HANDED_Z_UP_X_FWD':
        coordinate_system = COORDINATE_SYSTEM.RIGHT_HANDED_Z_UP_X_FWD
    return coordinate_system

def convert_coordinate_units(convert_param):
    # add here other configurations from InitParameters Zed SDK
    coordinate_units = None
    if convert_param == 'UNIT.MILLIMETER':
        coordinate_units = UNIT.MILLIMETER
    elif convert_param == 'UNIT.LAST':
        coordinate_units = UNIT.LAST
    elif convert_param == 'UNIT.FOOT':
        coordinate_units = UNIT.FOOT
    elif convert_param == 'UNIT.INCH':
        coordinate_units = UNIT.INCH
    elif convert_param == 'UNIT.CENTIMETER':
        coordinate_units = UNIT.CENTIMETER
    elif convert_param == 'UNIT.METER':
        coordinate_units = UNIT.METER
    return coordinate_units

def convert_depth_mode(convert_param):
    # add here other configurations from InitParameters Zed SDK
    convert_depth_mode = None
    if convert_param == 'DEPTH_MODE.PERFORMANCE':
        convert_depth_mode = DEPTH_MODE.PERFORMANCE
    elif convert_param == 'DEPTH_MODE.LAST':
        convert_depth_mode = DEPTH_MODE.LAST
    elif convert_param == 'DEPTH_MODE.NONE':
        convert_depth_mode = DEPTH_MODE.NONE
    elif convert_param == 'DEPTH_MODE.QUALITY':
        convert_depth_mode = DEPTH_MODE.QUALITY
    elif convert_param == 'DEPTH_MODE.ULTRA':
        convert_depth_mode = DEPTH_MODE.ULTRA
    return convert_depth_mode

def load_zed_config_from_file(f_config_name: object) -> object:
    """
    Read config from file settings.conf
    :return:
    """
    # todo: check config, bollean values creates errors
    f_config = configparser.ConfigParser()
    f_config.read(f_config_name)
    # zed object
    dev_zed_conf = sl.InitParameters()  # creates object
    dev_zed_conf.camera_disable_self_calib = False  # bool(f_config['DEFAULT']['camera_disable_self_calib'])
    dev_zed_conf.camera_fps = int(f_config['DEFAULT']['camera_fps'])
    dev_zed_conf.camera_image_flip = convert_flip_mode(f_config['DEFAULT']['camera_image_flip'])
    dev_zed_conf.camera_resolution = convert_camera_resolution(f_config['DEFAULT']['camera_resolution'])
    dev_zed_conf.coordinate_system = convert_coordinate_system(f_config['DEFAULT']['coordinate_system'])
    dev_zed_conf.coordinate_units = convert_coordinate_units(f_config['DEFAULT']['coordinate_units'])
    dev_zed_conf.depth_maximum_distance = float(f_config['DEFAULT']['depth_maximum_distance'])
    dev_zed_conf.depth_minimum_distance = float(f_config['DEFAULT']['depth_minimum_distance'])
    dev_zed_conf.depth_mode = convert_depth_mode(f_config['DEFAULT']['depth_mode'])
    dev_zed_conf.depth_stabilization = bool(f_config['DEFAULT']['depth_stabilization'])
    dev_zed_conf.enable_image_enhancement = True  # bool(f_config['DEFAULT']['enable_image_enhancement'])
    dev_zed_conf.enable_right_side_measure = False  # bool(f_config['DEFAULT']['enable_right_side_measure'])
    # dev_zed_conf.input = str(f_config['DEFAULT']['input'])
    dev_zed_conf.optional_opencv_calibration_file = ''  # str(f_config['DEFAULT']['optional_opencv_calibration_file'])
    dev_zed_conf.optional_settings_path = ''  # str(f_config['DEFAULT']['optional_settings_path'])
    dev_zed_conf.sdk_gpu_id = int(f_config['DEFAULT']['sdk_gpu_id'])
    dev_zed_conf.sdk_verbose = False  # bool(f_config['DEFAULT']['sdk_verbose'])
    dev_zed_conf.sdk_verbose_log_file = ''  # f_config['DEFAULT']['sdk_verbose_log_file']
    dev_zed_conf.sensors_required = False  # bool(f_config['DEFAULT']['sensors_required'])
    dev_zed_conf.svo_real_time_mode = False  # bool(f_config['DEFAULT']['svo_real_time_mode'])

    return dev_zed_conf


def load_zed_default_config():
    """
    Read config from file settings.conf
    :return:
    """
    # zed object
    dev_zed_conf = sl.InitParameters()
    dev_zed_conf.camera_disable_self_calib = False
    dev_zed_conf.camera_fps = int(0)
    dev_zed_conf.camera_image_flip = FLIP_MODE.AUTO
    dev_zed_conf.camera_resolution = sl.RESOLUTION.HD720
    dev_zed_conf.coordinate_system = COORDINATE_SYSTEM.IMAGE
    dev_zed_conf.coordinate_units = UNIT.MILLIMETER
    dev_zed_conf.depth_maximum_distance = float(1.0)
    dev_zed_conf.depth_minimum_distance = float(1.0)
    dev_zed_conf.depth_mode = DEPTH_MODE.PERFORMANCE
    dev_zed_conf.depth_stabilization = 1
    dev_zed_conf.enable_image_enhancement = True
    dev_zed_conf.enable_right_side_measure = False
    dev_zed_conf.input = ''
    dev_zed_conf.optional_opencv_calibration_file = ''
    dev_zed_conf.optional_settings_path = ''
    dev_zed_conf.sdk_gpu_id = int(- 1)
    dev_zed_conf.sdk_verbose = False
    dev_zed_conf.sdk_verbose_log_file = ''
    dev_zed_conf.sensors_required = False
    dev_zed_conf.svo_real_time_mode = False

    return dev_zed_conf
