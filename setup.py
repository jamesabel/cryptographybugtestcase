
import distutils.core
import py2exe
import cx_Freeze

use_cx_freeze = True  # False for py2exe

if use_cx_freeze:

    # make sure cx_freeze picks up these packages
    build_exe_options = {"packages": ["cryptography.fernet", "cryptography.hazmat", "distutils"]}

    cx_Freeze.setup(
        name="testcase",
        version="0.0",
        options={"build_exe": build_exe_options},
        executables=[cx_Freeze.Executable("testcase.py", base="Console")],
    )

else:
    distutils.core.setup(
        console=['testcase.py'],
        name="testcase",
        version="0.0",
    )
