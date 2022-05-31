"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:

Use:
from gui_frame_ext.about_window import AboutWindow

    def open_about_data(self):
        about_windows = AboutWindow(self)
        about_windows.grab_set()
"""
import datetime
import time
import tkinter as tk

from desktop_gui.ui_client_config import UIClientConfig
from desktop_gui.remote_connection import RemoteConnection
from desktop_gui.cmd_config import CmdConfig
from desktop_gui.about_window import AboutWindow


class DesktopConsole(tk.Tk):
    connection_obj = None
    take_a_capture_flag = False

    FRAME_WIDTH = 70
    LABEL_WIDTH = 15
    ENTRY_WIDTH_PATH = 50
    BUTTON_WIDTH = 30

    def __init__(self, master=None):
        super().__init__()
        # -----------------------
        # -----------------------
        self.geometry('320x480')
        self.title(_("Management Console"))
        self.resizable(width=False, height=False)
        self.attributes('-topmost', True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # calling methods to create components
        self.createWidgets()
        self.createMenuBars()
        self.ui_config_obj = UIClientConfig()
        self.connection_obj = RemoteConnection(self.ui_config_obj)
        # enable all clientes by default
        self.connection_obj.send_set_connection()
        self.connection_obj.send_remote_cmd(CmdConfig.enable_remote_client)
        self.update_tasks()  # update tasks

    def createWidgets(self):
        self.remote_cmd_frame = tk.LabelFrame(self, text=_("Remote commands"), relief=tk.RIDGE, width=self.FRAME_WIDTH)
        self.remote_cmd_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # ---------------
        self.enable_clients_button = tk.Button(self.remote_cmd_frame, text=_('Enable remote clients'),
                                               command=self.enable_clients, width=self.BUTTON_WIDTH)
        self.enable_clients_button.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.start_record_button = tk.Button(self.remote_cmd_frame, text=_('Start record'), command=self.enable_record,
                                             width=self.BUTTON_WIDTH)
        self.start_record_button.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.stop_record_button = tk.Button(self.remote_cmd_frame, text=_('Stop record'), command=self.stop_record,
                                            width=self.BUTTON_WIDTH)
        self.stop_record_button.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.take_capture_button = tk.Button(self.remote_cmd_frame, text=_('Take capture'), command=self.take_capture,
                                             width=self.BUTTON_WIDTH)
        self.take_capture_button.grid(row=4, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.shutdown_clients_button = tk.Button(self.remote_cmd_frame, text=_('Shutdown remote clients'),
                                                 command=self.shutdown_clients, width=self.BUTTON_WIDTH)
        self.shutdown_clients_button.grid(row=5, column=1, sticky=tk.W, ipadx=3, ipady=3)
        ########################################################
        # MESSAGE FRAME
        self.message_frame = tk.LabelFrame(self, text=_("Info"), relief=tk.RIDGE, width=self.FRAME_WIDTH)
        self.message_frame.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        self.messages_label = tk.Label(self.message_frame, text=_('Messages:'))
        self.messages_label.grid(row=1, column=0, sticky=tk.W, ipadx=3, ipady=3)

        self.messages_info = tk.Text(self.message_frame, width=34, height=5)
        self.messages_info.grid(row=2, column=0, sticky=tk.W)
        # ---------------
        self.quit_button = tk.Button(self, text=_('Quit'), command=self.quit_app, width=32)
        self.quit_button.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
        # ---------------
        self.ui_buttons_disable_all()
        # ---------------

    def update_tasks(self):
        execution_time_update = datetime.datetime.utcnow()
        # print(f"We make a task HERE!! {execution_time_update}")
        self.after(2000, self.update_tasks)

    def createMenuBars(self):
        self.menubar = tk.Menu(self)
        self.menu_help = tk.Menu(self.menubar, tearoff=False)  # delete dash lines
        self.menu_help.add_command(label=_('About...'), command=self.not_implemented_yet)
        self.menubar.add_cascade(menu=self.menu_help, label=_('About'), underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def ui_buttons_enable_all(self):
        self.enable_clients_button["state"] = "disabled"
        self.start_record_button["state"] = "active"
        self.stop_record_button["state"] = "disabled"
        self.take_capture_button["state"] = "active"
        self.shutdown_clients_button["state"] = "active"

    def ui_buttons_disable_all(self):
        self.enable_clients_button["state"] = "active"
        self.start_record_button["state"] = "disabled"
        self.stop_record_button["state"] = "disabled"
        self.take_capture_button["state"] = "disabled"
        self.shutdown_clients_button["state"] = "disabled"

    def ui_buttons_enable_record(self):
        self.enable_clients_button["state"] = "disabled"
        self.start_record_button["state"] = "disabled"
        self.stop_record_button["state"] = "active"
        self.take_capture_button["state"] = "disabled"
        self.shutdown_clients_button["state"] = "active"

    def ui_buttons_stop_record(self):
        self.enable_clients_button["state"] = "active"
        self.start_record_button["state"] = "active"
        self.stop_record_button["state"] = "disabled"
        self.take_capture_button["state"] = "active"
        self.shutdown_clients_button["state"] = "active"

    def ui_buttons_take_capture(self):
        # self.enableClientsButton["state"] = "disabled"
        # self.startRecordButton["state"] = "disabled"
        # self.stopRecordButton["state"] = "active"
        # self.takeCaptureButton["state"] = "disabled"
        # self.shutdownClientsButton["state"] = "active"
        print("Taking a capture!")

    def not_implemented_yet(self):
        print(_("Not implemented yet!!!"))
        about_windows = AboutWindow(self)
        about_windows.grab_set()

    def enable_clients(self):
        self.messages_info.insert("end", _("Enabling remote clients") + "\n")
        self.ui_buttons_enable_all()
        self.connection_obj.send_remote_cmd(CmdConfig.enable_remote_client)

    def enable_record(self):
        self.messages_info.insert("end", _("Enable recording") + "\n")
        self.ui_buttons_enable_record()
        self.connection_obj.send_remote_cmd(CmdConfig.start_record)

    def stop_record(self):
        self.messages_info.insert("end", _("Stop recording") + "\n")
        self.ui_buttons_stop_record()
        self.connection_obj.send_remote_cmd(CmdConfig.stop_record)

    def take_capture(self):
        self.messages_info.insert("end", _("Taking capture") + "\n")
        self.ui_buttons_take_capture()
        # if self.take_a_capture_flag == False:
        self.messages_info.insert("end", _("A capture was launch!!" + "\n"))
        self.connection_obj.send_remote_cmd(CmdConfig.take_capture)
        time.sleep(10)
        self.messages_info.insert("end", _("Capture time finished" + "\n"))
        self.connection_obj.send_remote_cmd(CmdConfig.enable_remote_client)
        time.sleep(5)
        # self.take_a_capture_flag = False

    def shutdown_clients(self):
        self.messages_info.insert("end", _("Shutting down remote clients") + "\n")
        self.ui_buttons_disable_all()
        self.connection_obj.send_remote_cmd(CmdConfig.stop_remote_client)

    def quit_app(self):
        # ---------------------------------------------
        # close token, close connection
        # ---------------------------------------------
        self.connection_obj.send_finalize_connection()
        # ---------------------------------------------
        self.quit
        self.destroy()
