import os
import sys

import psychoacoustics
from psychoacoustics.plugins.multiprocess import MultiProcess
from psychoacoustics.config import Config
from psychoacoustics.plugins.manager import PluginManager

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "USAGE: %s TEST_FILE LOG_FILE KILL_FILE" % sys.argv[0]
        sys.exit(1)
    os.environ['PSY_ECHOS_TICKS_MP_LOG']=sys.argv[2]
    os.environ['PSY_ECHOS_TICKS_MP_KILL']=sys.argv[3]
    psychoacoustics.main(
            defaultTest=sys.argv[1], argv=[sys.argv[0],'--processes=1','-v'],
            config=Config(plugins=PluginManager(plugins=[MultiProcess()])))
