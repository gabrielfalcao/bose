"""
Lists builtin plugins.
"""
plugins = []
builtins = (
    ('psychoacoustics.plugins.attrib', 'AttributeSelector'),
    ('psychoacoustics.plugins.capture', 'Capture'),
    ('psychoacoustics.plugins.logcapture', 'LogCapture'),
    ('psychoacoustics.plugins.cover', 'Coverage'),
    ('psychoacoustics.plugins.debug', 'Pdb'),
    ('psychoacoustics.plugins.deprecated', 'Deprecated'),
    ('psychoacoustics.plugins.doctests', 'Doctest'),
    ('psychoacoustics.plugins.isolate', 'IsolationPlugin'),
    ('psychoacoustics.plugins.failuredetail', 'FailureDetail'),
    ('psychoacoustics.plugins.prof', 'Profile'),
    ('psychoacoustics.plugins.skip', 'Skip'),
    ('psychoacoustics.plugins.testid', 'TestId'),
    ('psychoacoustics.plugins.multiprocess', 'MultiProcess'),
    ('psychoacoustics.plugins.xunit', 'Xunit'),
    ('psychoacoustics.plugins.allmodules', 'AllModules'),
    ('psychoacoustics.plugins.collect', 'CollectOnly'),
    )

for module, cls in builtins:
    try:
        plugmod = __import__(module, globals(), locals(), [cls])
    except KeyboardInterrupt:
        raise
    except:
        continue
    plug = getattr(plugmod, cls)
    plugins.append(plug)
    globals()[cls] = plug

