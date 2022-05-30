"""
Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Adapted code from
Date: August 2021
Description:

Use:
"""

import sys
import os
from path import Path

def _add_dll_directory(path: Path):
    from ctypes import c_wchar_p, windll  # type: ignore
    from ctypes.wintypes import DWORD

    AddDllDirectory = windll.kernel32.AddDllDirectory
    AddDllDirectory.restype = DWORD
    AddDllDirectory.argtypes = [c_wchar_p]
    AddDllDirectory(str(path))

def kinect():
    if sys.platform != "win32":
        return
    env_path = os.getenv("KINECT_LIBS", None)
    if env_path:
        candidate = Path(env_path)
        dll = candidate / "k4a.dll"
        if dll.exists():
            _add_dll_directory(candidate)
            return
    # autodetecting
    program_files = Path("C:\\Program Files\\")
    for dir in sorted(program_files.glob("Azure Kinect SDK v*"), reverse=True):
        candidate = dir / "sdk" / "windows-desktop" / "amd64" / "release" / "bin"
        dll = candidate / "k4a.dll"
        if dll.exists():
            _add_dll_directory(candidate)
            return
