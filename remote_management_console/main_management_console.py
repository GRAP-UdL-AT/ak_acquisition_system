"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Remote Management Console, this sends commands to the central server. It offers a basic interface
    to manage the acquisition system.
Use:

    python ui_console_manager.py

"""

import locale
import gettext
import os
from src.desktop_gui.gui_classes import DesktopConsole



if __name__ == '__main__':
    current_locale, encoding = locale.getdefaultlocale()
    LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
    locale_path = os.path.join(LOCAL_PATH, 'src/locale')
    language = gettext.translation('gui_classes', locale_path, ['en_US'])
    language.install()

    app = DesktopConsole()
    app.mainloop()

    # INTERNATIONALIZATION
    # base file for translation is located in /base/
    # Use xgettext https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html
    # xgettext -d gui_classes -o locale/gui_classes.pot gui_classes/gui_classes.py