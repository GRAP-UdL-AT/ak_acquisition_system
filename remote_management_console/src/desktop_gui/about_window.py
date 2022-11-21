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
        self.geometry('350x480')
        self.title(_('About...'))
        self.resizable(width=False, height=False)  # do not change the size
        self.attributes('-topmost', True)
        # aboutLabel = tk.Label(self, text='About')
        about_label = tk.Label(self, text=_('Management Console'))
        about_label.config(bg="#00ffff", font=("Verdana", 12))
        about_label.pack(anchor=tk.CENTER)
        tinfo = tk.Text(self, width=80, height=15)

        about_text_info = f' \n' \
                          f'Created by: Juan Carlos Miranda\n' \
                          f'Site: https://github.com/juancarlosmiranda\n' \
                          f'November 2021 \n' \
                          f' \n' \
                          f'PAgFRUIT project RTI2018-094222-B-I00\n' \
                          f'http://www.pagfruit.udl.cat/\n' \
                          f' \n' \
                          f'Research Group on AgroICT & Precision Agriculture\n' \
                          f'GRAP Universitat de Lleida\n' \
                          f'Agrotecnio - CERCA Center\n' \
                          f'https://www.grap.udl.cat/\n'

        tinfo.insert("1.0", about_text_info)
        tinfo.pack(anchor=tk.CENTER)
        button_close = tk.Button(self, text='Close', command=self.destroy)
        button_close.pack(expand=True)
