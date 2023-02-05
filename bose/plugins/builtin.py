"""
Lists builtin plugins.
"""
plugins = []
builtins = (
    ('bose.plugins.attrib', 'AttributeSelector'),
    ('bose.plugins.capture', 'Capture'),
    ('bose.plugins.logcapture', 'LogCapture'),
    ('bose.plugins.cover', 'Coverage'),
    ('bose.plugins.debug', 'Pdb'),
    ('bose.plugins.deprecated', 'Deprecated'),
    ('bose.plugins.doctests', 'Doctest'),
    ('bose.plugins.isolate', 'IsolationPlugin'),
    ('bose.plugins.failuredetail', 'FailureDetail'),
    ('bose.plugins.prof', 'Profile'),
    ('bose.plugins.skip', 'Skip'),
    ('bose.plugins.testid', 'TestId'),
    ('bose.plugins.multiprocess', 'MultiProcess'),
    ('bose.plugins.xunit', 'Xunit'),
    ('bose.plugins.allmodules', 'AllModules'),
    ('bose.plugins.collect', 'CollectOnly'),
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

