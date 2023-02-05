from psychoacoustics.plugins.skip import SkipTest
from psychoacoustics.plugins.multiprocess import MultiProcess

def setup_module():
    try:
        import multiprocessing
        if 'active' in MultiProcess.status:
            raise SkipTest("Multiprocess plugin is active. Skipping tests of "
                           "plugin itself.")
    except ImportError:
        raise SkipTest("multiprocessing module not available")
