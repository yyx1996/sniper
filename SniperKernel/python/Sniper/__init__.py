import sys
sys.setdlopenflags( 0x100 | 0x2 ) # RTLD_GLOBAL | RTLD_NOW

from libSniperPython import *
from PyAlgBase import PyAlgBase
