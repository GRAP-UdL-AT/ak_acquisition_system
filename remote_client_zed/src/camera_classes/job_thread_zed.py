"""
Project: Zed camera management
Author: Juan Carlos Miranda
Date: August 2021
Description:
This is an wrapper to use Zed functions as a thread process
This class is used when we need to launch process  from loops as
a remote client. Methods are similar to zed_manager.py

Use:
"""
import threading
import logging
import os
import pyzed.sl as sl
import cv2 as cv2
from datetime import datetime


class JobThreadZed(threading.Thread):
    # ZED camera device
    _zed_device = None
    zed_device_config = None
    zed_runtime_config = None
    _f_path = None

    # todo: add depth functions

    def __init__(self, device_config_param=None, f_path_output_param=None):
        if device_config_param is None:
            logging.debug("Default config loaded")
            # Load config by default
            self.zed_device_config = sl.InitParameters()  # default config
        else:
            logging.debug('External config loaded')
            self.zed_device_config = device_config_param

        self.zed_runtime_config = sl.RuntimeParameters()  # todo check this in SDK help
        self._f_path = f_path_output_param
        logging.debug("__init__(self): - Initialize loading Zed Manager")

        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()

    def __del__(self):
        print('__DEL__')
        logging.debug("__del__(self): - Finalize Zed Manager")

    def initialize_sensor(self):
        logging.debug("Initialize_sensor()")
        self._zed_device = sl.Camera()
        if not self._zed_device.is_opened():
            print("Opening ZED Camera...")
        status = self._zed_device.open(self.zed_device_config)
        if status != sl.ERROR_CODE.SUCCESS:
            print(repr(status))
            exit(1)
            # todo: raise and exception to manage this

    def finalize_sensor(self):
        logging.debug("finalize_sensor()")
        self._zed_device.close()

    def get_svo_file_name(self):
        print("Recording ZED data")
        resolutionp = "_"
        if self.zed_device_config.camera_resolution == sl.RESOLUTION.HD720:
            resolutionp = "720"
        if self.zed_device_config.camera_resolution == sl.RESOLUTION.HD1080:
            resolutionp = "1080"
        if self.zed_device_config.camera_resolution == sl.RESOLUTION.HD2K:
            resolutionp = "HD2K"

        utc_time_now = datetime.utcnow()
        date_string = utc_time_now.strftime("%Y%m%d_%H%M%S")
        f_extension = ".svo"
        f_name = date_string + "_" + resolutionp + f_extension
        f_path_name = os.path.join(self._f_path, f_name)
        logging.info(f"CREATING_FILE {f_path_name}")

        return f_path_name

    def run(self):
        # todo: check this function
        # todo: based on S01-camera_control.py
        self.initialize_sensor()
        print("Recording data")
        f_path_name = self.get_svo_file_name()
        print("Recording... Creating file.")
        runtime = sl.RuntimeParameters()
        #image_mat = sl.Mat()
        record_param = sl.RecordingParameters(f_path_name)
        vid = self._zed_device.enable_recording(record_param)

        # #####################
        # # RECORD loop
        # #####################
        vid = sl.ERROR_CODE.FAILURE
        out = False
        while vid != sl.ERROR_CODE.SUCCESS and not out:
            vid = self._zed_device.enable_recording(record_param)
            print(repr(vid))
            if vid == sl.ERROR_CODE.SUCCESS:
                print("Recording started...")
                frames_recorded = 0
                out = True
                try:
                    print('RECORDING-STARTED #%s' % self.ident)
                    logging.info(f'RECORDING-STARTED #{self.ident}')
                    start_video = datetime.utcnow()
                    while not self.shutdown_flag.is_set():
                        err = self._zed_device.grab(runtime)
                        if err == sl.ERROR_CODE.SUCCESS:
                            frames_recorded += 1
                            #logging.info(f'frames_recorded -- {frames_recorded}')
                    stop_video = datetime.utcnow()
                    time_recorded = stop_video - start_video
                    logging.info(f"RECORDING- {time_recorded} recorded time, {frames_recorded} frames written")

                except KeyboardInterrupt:
                    print("(Ctrl-C) pressed!!")
                    print(f"{frames_recorded} frames written.")
                    logging.info(f"{frames_recorded} frames written.")
            else:
                print("There is a problem with the SVO file!")
                print("Recording not started.!")
        self._zed_device.disable_recording()
        # ... Clean shutdown code here ...
        print(f'RECORDING-STOPPED #{self.ident}')
        logging.info(f'RECORDING-STOPPED #{self.ident}')
        # close sensor sensor
        self._zed_device.disable_recording()
        self.finalize_sensor()

    def run_real_time(self):
        # todo: review this method
        print('RECORDING-STARTED #%s' % self.ident)
        self.initialize_sensor()
        while not self.shutdown_flag.is_set():
            image_mat = sl.Mat()
            err_flag = self._zed_device.grab(self.zed_device_config)
            if err_flag == sl.ERROR_CODE.SUCCESS:
                self._zed_device.retrieve_image(image_mat, sl.VIEW.LEFT)
                cv2.imshow("Real time data", image_mat.get_data())
            else:
                print("err_flag->", err_flag)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                cv2.destroyAllWindows()
                image_mat.free(memory_type=sl.MEM.CPU)
                break
        print(f'RECORDING-STOPPED #{self.ident}')
        logging.info(f'RECORDING-STOPPED #{self.ident}')
        self.finalize_sensor()

# todo: def show_a_capture(self):
# todo: def get_a_capture(self):
