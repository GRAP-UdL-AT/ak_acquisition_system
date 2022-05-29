"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
  Uses of threads jobs, launch a thread and sleep.

Usage:
    python main_thread_example_2.py

"""

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

def service_shutdown(signum, frame):
    print('Service shut down --> Caught signal %d' % signum)
    raise ServiceExit

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', filename='../threadlogger.log', level=logging.DEBUG)
    try:
        job_thread = JobThreadLog()
        job_thread.start()
        time.sleep(5)
        job_thread.shutdown_flag.set()
        job_thread.join()
        print(job_thread.ident)

    except ServiceExit:
        print('ServiceExit Exception --> ')
        print('CATCHING any Exception HERE!-->')
        job_thread.shutdown_flag.set()
        job_thread.join()
