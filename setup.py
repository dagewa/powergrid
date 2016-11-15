from distutils.core import setup
import py2exe

# python setup.py py2exe > build.log
setup(
    windows=[{'script': 'powergrid.pyw',
             "icon_resources": [(1, "hal_9000.ico")]}],
    )
