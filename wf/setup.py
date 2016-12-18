# -*- coding: utf-8 -*-
# py -2 setup.py py2exe
from distutils.core import setup
import py2exe

setup(options={  
        'py2exe': {  
            'optimize': 2,  
            'bundle_files': 1,  
            'compressed': True,  
        },  
    },
    zipfile = None,
    console=["f.py"])
