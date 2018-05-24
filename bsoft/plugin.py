from pyworkflow.plugin import Plugin
from bibtex import _bibtex

import os

BSOFT_HOME = 'BSOFT_HOME'


class BsoftPlugin(Plugin):  #### Extend plugin class, change class name!!!

    def __init__(self):
        # change your default configVars!!!
        configVars = {BSOFT_HOME: os.path.join(os.environ['EM_ROOT'], 'bsoft-1.9.0') }

        Plugin.__init__(self, 'bsoft', # change plugin Name!!
                              version="1.0.0", # change version
                              logo="bsoft_logo.png", # change logo!
                              configVars=configVars, # change your default env vars!!!
                              bibtex=_bibtex # if you don't have bibtex, remove this!
                        )
    def registerPluginBinaries(self, env):
        env.addPackage('bsoft', version='1.8.8',
                       tar='bsoft1_8_8_Fedora_12.tgz')

        env.addPackage('bsoft', version='1.9.0',
                       tar='bsoft1_9_0_Fedora_20.tgz',
                       default=True)

# VERY IMPORTANT TO LEAVE THE VARIABLE NAME "_plugin" !!!!
_plugin = BsoftPlugin()  # Instantiate your class as named above :)