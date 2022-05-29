"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
  Test for thread creation

Documentation in https://docs.python.org/3/library/unittest.html

Usage:
    python -m unittest $HOME/development/KA_detector/dataset_management/test/test_multithreading.py

"""


import unittest
import os
import logging
import time
from multithreading.job_thread_log import JobThreadLog


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print('Service Exit --> \r')
    pass


class TestDatasetConfig(unittest.TestCase):

    def setUp(self):
        # CONFIGURE HERE PATHS TO A TEST DATASET
        self.root_folder = os.path.abspath('')

    def test_job_thread(self):
        """
        Testing creation of threads
        """
        logging.basicConfig(format='%(asctime)s %(message)s', filename='threadlogger.log', level=logging.DEBUG)
        try:
            job_thread = JobThreadLog()
            job_thread.start()
            expected_number = job_thread.ident
            time.sleep(1)
            job_thread.shutdown_flag.set()
            job_thread.join()

        except ServiceExit:
            print('ServiceExit Exception --> ')
            print('CATCHING any Exception HERE!-->')
            job_thread.shutdown_flag.set()
            job_thread.join()

        self.assertEqual(expected_number, job_thread.ident)
