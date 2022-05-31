"""
# Project: Fruit Size Estimation https://github.com/GRAP-UdL-AT/ak_acquisition_system
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:

Use:
from gui_frame_ext.about_window import AboutWindow

    def open_about_data(self):
        about_windows = AboutWindow(self)
        about_windows.grab_set()
"""
import tkinter as tk


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # self.geometry(GUIFrameExtractorConfig2.geometry_about)
        self.geometry('320x480')
        self.title(_('About...'))
        self.resizable(width=False, height=False)  # do not change the size
        self.attributes('-topmost', True)
        # aboutLabel = tk.Label(self, text='About')
        about_label = tk.Label(self, text=_('Management Console'))
        about_label.config(bg="#00ffff", font=("Verdana", 12))
        about_label.pack(anchor=tk.CENTER)
        tinfo = tk.Text(self, width=40, height=5)

        about_text_info = f'Size estimation project.\n' \
                          f'Juan Carlos Miranda\n' \
                          f'https://github.com/juancarlosmiranda\n' \
                          f'November 2021 \n' \
                          f'Software under development v0.1\n'

        tinfo.insert("1.0", about_text_info)
        tinfo.pack(anchor=tk.CENTER)
        button_close = tk.Button(self, text='Close', command=self.destroy)
        button_close.pack(expand=True)
