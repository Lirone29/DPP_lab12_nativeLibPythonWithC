import sys
from cx_Freeze import setup, Executable

setup(
    name = "DPP lib",
    version = "1.0",
    description = "Any",
    executables = [Executable("useLib.py")]

)