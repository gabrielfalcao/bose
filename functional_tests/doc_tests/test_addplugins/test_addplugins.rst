Using custom plugins without setuptools
---------------------------------------

If you have one or more custom plugins that you'd like to use with psychoacoustics, but
can't or don't want to register that plugin as a setuptools entrypoint, you
can use the ``addplugins`` keyword argument to :func:`psychoacoustics.core.main` or
:func:`psychoacoustics.core.run` to make the plugins available.

To do this you would construct a launcher script for psychoacoustics, something like::

  from psychoacoustics import main
  from yourpackage import YourPlugin, YourOtherPlugin

  if __name__ == '__main__':
      psychoacoustics.main(addplugins=[YourPlugin(), YourOtherPlugin()])

Here's an example. Say that you don't like the fact that the collect-only
plugin outputs 'ok' for each test it finds; instead you want it to output
'maybe.' You could modify the plugin itself, or instead, create a Maybe plugin
that transforms the output into your desired shape.

Without the plugin, we get 'ok.'

>>> import os
>>> support = os.path.join(os.path.dirname(__file__), 'support')
>>> from psychoacoustics.plugins.plugintest import run_buffered as run
>>> argv = [__file__, '-v', support] # --collect-only
>>> run(argv=argv)
test.test ... ok
<BLANKLINE>
----------------------------------------------------------------------
Ran 1 test in ...s
<BLANKLINE>
OK

Without '-v', we get a dot.

>>> run(argv=[__file__, support])
.
----------------------------------------------------------------------
Ran 1 test in ...s
<BLANKLINE>
OK

The plugin is simple. It captures and wraps the test result output stream and
replaces 'ok' with 'maybe' and '.' with '?'.

>>> from psychoacoustics.plugins.base import Plugin
>>> class Maybe(Plugin):
...     def setOutputStream(self, stream):
...         self.stream = stream
...         return self
...     def flush(self):
...         self.stream.flush()
...     def writeln(self, out=""):
...         self.write(out + "\n")
...     def write(self, out):
...         if out == "ok\n":
...             out = "maybe\n"
...         elif out == ".":
...             out = "?"
...         self.stream.write(out)

To activate the plugin, we pass an instance in the addplugins list.

>>> run(argv=argv + ['--with-maybe'], addplugins=[Maybe()])
test.test ... maybe
<BLANKLINE>
----------------------------------------------------------------------
Ran 1 test in ...s
<BLANKLINE>
OK

>>> run(argv=[__file__, support, '--with-maybe'], addplugins=[Maybe()])
?
----------------------------------------------------------------------
Ran 1 test in ...s
<BLANKLINE>
OK

