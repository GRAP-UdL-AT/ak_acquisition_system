"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
  Test for thread creation with log writting

Use:
    job_thread = JobThreadLog()
    job_thread.start()
    job_thread.shutdown_flag.set()
    job_thread.join()

"""


import time
import threading
import logging


class JobThreadLog(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        # \n

    def run(self):
        print('STARTED #%s' % self.ident)
        logging.info('STARTED #%s' % self.ident)
        while not self.shutdown_flag.is_set():
            print(f'WORKING #{self.ident}')
            logging.info(f'WORKING #{self.ident}')
            time.sleep(1)

        # ... Clean shutdown code here ...
        print(f'STOPPED #{self.ident}')
        logging.info(f'STOPPED #{self.ident}')
