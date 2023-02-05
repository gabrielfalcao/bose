"""
psytests setuptools command
----------------------------

The easiest way to run tests with bose is to use the `psytests` setuptools
command::

  python setup.py psytests

This command has one *major* benefit over the standard `test` command: *all
bose plugins are supported*.

To configure the `psytests` command, add a [psytests] section to your
setup.cfg. The [psytests] section can contain any command line arguments that
psytests supports. The differences between issuing an option on the command
line and adding it to setup.cfg are:

* In setup.cfg, the -- prefix must be excluded
* In setup.cfg, command line flags that take no arguments must be given an
  argument flag (1, T or TRUE for active, 0, F or FALSE for inactive)

Here's an example [psytests] setup.cfg section::

  [psytests]
  verbosity=1
  detailed-errors=1
  with-coverage=1
  cover-package=bose
  debug=bose.loader
  pdb=1
  pdb-failures=1

If you commonly run psytests with a large number of options, using
the psytests setuptools command and configuring with setup.cfg can
make running your tests much less tedious. (Note that the same options
and format supported in setup.cfg are supported in all other config
files, and the psytests script will also load config files.)

Another reason to run tests with the command is that the command will
install packages listed in your `tests_require`, as well as doing a
complete build of your package before running tests. For packages with
dependencies or that build C extensions, using the setuptools command
can be more convenient than building by hand and running the psytests
script.

Bootstrapping
-------------

If you are distributing your project and want users to be able to run tests
without having to install bose themselves, add bose to the setup_requires
section of your setup()::

  setup(
      # ...
      setup_requires=['bose>=1.0']
      )

This will direct setuptools to download and activate bose during the setup
process, making the ``psytests`` command available.

"""
try:
    from setuptools import Command
except ImportError:
    Command = psytests = None
else:
    from bose.config import Config, option_blacklist, user_config_files, \
        flag, _bool
    from bose.core import TestProgram
    from bose.plugins import DefaultPluginManager


    def get_user_options(parser):
        """convert a optparse option list into a distutils option tuple list"""
        opt_list = []
        for opt in parser.option_list:
            if opt._long_opts[0][2:] in option_blacklist: 
                continue
            long_name = opt._long_opts[0][2:]
            if opt.action not in ('store_true', 'store_false'):
                long_name = long_name + "="
            short_name = None
            if opt._short_opts:
                short_name =  opt._short_opts[0][1:]
            opt_list.append((long_name, short_name, opt.help or ""))
        return opt_list


    class psytests(Command):
        description = "Run unit tests using psytests"
        __config = Config(files=user_config_files(),
                          plugins=DefaultPluginManager())
        __parser = __config.getParser()
        user_options = get_user_options(__parser)

        def initialize_options(self):
            """create the member variables, but change hyphens to
            underscores
            """

            self.option_to_cmds = {}
            for opt in self.__parser.option_list:
                cmd_name = opt._long_opts[0][2:]
                option_name = cmd_name.replace('-', '_')
                self.option_to_cmds[option_name] = cmd_name
                setattr(self, option_name, None)
            self.attr  = None

        def finalize_options(self):
            """nothing to do here"""
            pass

        def run(self):
            """ensure tests are capable of being run, then
            run bose.main with a reconstructed argument list"""
            if getattr(self.distribution, 'use_2to3', False):
                # If we run 2to3 we can not do this inplace:

                # Ensure metadata is up-to-date
                build_py = self.get_finalized_command('build_py')
                build_py.inplace = 0
                build_py.run()
                bpy_cmd = self.get_finalized_command("build_py")
                build_path = bpy_cmd.build_lib

                # Build extensions
                egg_info = self.get_finalized_command('egg_info')
                egg_info.egg_base = build_path
                egg_info.run()

                build_ext = self.get_finalized_command('build_ext')
                build_ext.inplace = 0
                build_ext.run()
            else:
                self.run_command('egg_info')

                # Build extensions in-place
                build_ext = self.get_finalized_command('build_ext')
                build_ext.inplace = 1
                build_ext.run()

            if self.distribution.install_requires:
                self.distribution.fetch_build_eggs(
                    self.distribution.install_requires)
            if self.distribution.tests_require:
                self.distribution.fetch_build_eggs(
                    self.distribution.tests_require)

            ei_cmd = self.get_finalized_command("egg_info")
            argv = ['psytests', '--where', ei_cmd.egg_base] 
            for (option_name, cmd_name) in self.option_to_cmds.items():
                if option_name in option_blacklist:
                    continue
                value = getattr(self, option_name)
                if value is not None:
                    argv.extend(
                        self.cfgToArg(option_name.replace('_', '-'), value))
            TestProgram(argv=argv, config=self.__config)

        def cfgToArg(self, optname, value):
            argv = []
            long_optname = '--' + optname
            opt = self.__parser.get_option(long_optname)
            if opt.action in ('store_true', 'store_false'):
                if not flag(value):
                    raise ValueError("Invalid value '%s' for '%s'" % (
                        value, optname))
                if _bool(value):
                    argv.append(long_optname)
            else:
                argv.extend([long_optname, value])
            return argv
