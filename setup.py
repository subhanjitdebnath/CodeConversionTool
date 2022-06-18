application_title = 'PerconversionTool'
mainfile='AnalysisPreconversion.py'

import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform =="win32":
        base="Win32GUI"

includes =["atexit","re"]

setup (
        name =application_title,
        version="0.1",
        description="CodeAnalysisTool",
        options={"build_exe":{"includes":includes}},
        executables={Executable(mainfile,base=base)}
)