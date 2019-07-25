SublimeLinter-contrib-standardrb
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [standardrb](https://github.com/testdouble/standard). It will be used with files that have the `ruby`, `ruby on rails`, `rspec`, `betterruby`, `better rspec`, `ruby experimental` or `cucumber steps` syntaxes.

## Installation
SublimeLinter must be installed in order to use this plugin.

This package is not yet available for installation va PackageControl. If you're unsure of what to do with this repository, please refer to [The Sublime Text package documentation](https://www.sublimetext.com/docs/3/packages.html).

Before using this plugin, you must ensure that `standard` is installed on your system. To install `standard`, do the following:

1. Install [Ruby](http://ruby-lang.org).

1. Install `standard` by typing the following in a terminal:
   ```
   [sudo] gem install standard
   ```

1. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.com/en/latest/troubleshooting.html#adjusting-shell-startup-files) for more information.

In order for `standard` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

You can configure standard exactly the way you would from the command line, using `.standard.yml` configuration files. For more information, see the [standard documentation](https://github.com/testdouble/standard#what-you-might-do-if-youre-clever).

To override the config file path, you would add this to the Sublime Linter User Settings:

```json
{
    "settings": {
        "SublimeLinter.linters.standard.args": ["--rails", "--no-display-cop-names"]
    }
}
```

### Bundler
If you are using Bundler and would like to use the locked standard version, you must set `use_bundle_exec` to true:

```json
{
    "settings": {
        "SublimeLinter.linters.standard.use_bundle_exec": true
    }
}
```

### Playing Nice With SublimeLinter-Rubocop
It's likely that you'll want to use Standard as your linter for some projects and Rubocop directly for others. Since Standard is a [wrapper on top of Rubocop](https://github.com/testdouble/standard#what-you-might-do-if-youre-really-clever) and both linters will lint the same files, having both enabled can give you some conflicting results (such as allowing neither single nor double quoted string literals).
One option for dealing with this overlap is to globally disable standard in your `Preferences.sublime-settings` file:

```json
{
    "SublimeLinter.linters.standard.disable": true
}
```

This will prevent SiblimeLinter from using Standard while continuing to allow Rubocop. For any project you'd like to lint with Standard instead of Rubocop, you can then add the following to your `*.sublime-project` settings, which will disable the Rubocop linter and enable Standard instead:

```json
{
    "settings": {
        "SublimeLinter.linters.rubocop.disable": true,
        "SublimeLinter.linters.standard.disable": false
    }
}

```
-----

This plugin is largely based on [SublimeLinter-Rubocop](https://github.com/SublimeLinter/SublimeLinter-rubocop)
