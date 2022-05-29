"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description: Main process, which executes routines. This requires the API server to be active

Usage:
    python UI_main_thread_1.py

"""

import curses
import logging
import signal
from job_thread import JobThread

X_MESSAGE = 1
Y_MESSAGE = 1


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print('Service Exit --> \r')
    pass


def service_shutdown(signum, frame):
    print('Caught signal %d' % signum)
    raise ServiceExit


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    my_screen = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)

    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)

    try:
        job_thread = JobThread()
        # main loop
        key_pressed = None
        while key_pressed != ord('q'):
            my_screen.clear()
            my_screen.border(0)
            my_screen.addstr(2, 4, "MENU - Launch threads", curses.color_pair(3))
            my_screen.addstr(3, 4, "1 - Launch thread")
            my_screen.addstr(4, 4, "2 - Stopping thread")
            my_screen.addstr(8, 4, "q - Quit \n ")

            key_pressed = my_screen.getch()

            if key_pressed == ord('1'):
                if not job_thread.is_alive():
                    my_screen.clear()
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, "UI -> Launching thread!")
                    my_screen.addstr(X_MESSAGE + 2, Y_MESSAGE, 'UI -> Press any key!!')
                    key_pressed = my_screen.getch()
                    my_screen.clear()
                    job_thread = JobThread()
                    job_thread.start()
                else:
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, "UI -> WE CAN'T START JOB, it is ALIVE()")
                    my_screen.addstr(X_MESSAGE + 2, Y_MESSAGE, 'UI -> Press any key!!')
                    key_pressed = my_screen.getch()

            if key_pressed == ord('2'):
                if job_thread.is_alive():
                    job_thread.shutdown_flag.set()
                    job_thread.join()
                    my_screen.clear()
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, 'UI -> STOPPING thread #%s ' % job_thread.ident)
                else:
                    my_screen.clear()
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, "UI -> We CAN'T STOP JOB, it is NOT ALIVE()")

                my_screen.addstr(X_MESSAGE + 2, Y_MESSAGE, 'UI -> Press any key!!')
                key_pressed = my_screen.getch()

            if key_pressed == ord('q'):
                if job_thread.is_alive():
                    job_thread.shutdown_flag.set()
                    job_thread.join()

        curses.endwin()


    except ServiceExit:
        print('ServiceExit Exception --> \r')
        print('CATCHING any Exception HERE!--> \r')
        job_thread.shutdown_flag.set()
        job_thread.join()
