SublimeLinter-contrib-standardrb
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [StandardRB](https://github.com/testdouble/standard). It will be used with files that have the `ruby`, `ruby on rails`, `rspec`, `betterruby`, `better rspec`, `ruby experimental` or `cucumber steps` syntaxes.

## Installation

You need to have **SublimeLinter** and **StandardRB** installed in order to use this plugin.

If you you already have those requirements met, great! 🎉. You can use [Package Control](https://packagecontrol.io) to install the `SublimeLinter-contrib-standardrb` plugin.

If you _haven't_ installed SublimeLinter and StandardRB, see below:

### Install SublimeLinter

Refer to the [SublimeLinter Docs](http://www.sublimelinter.com/en/stable/) for installation instructions.

### Install StandardRB

Before using this plugin, you must ensure that `standard` is installed on your system. To install `standard`, do the following:

1. Install [Ruby](http://ruby-lang.org).

1. Install `standard` by typing the following in a terminal:

       ```
       gem install standard
       ```

1. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.com/en/latest/troubleshooting.html#adjusting-shell-startup-files) for more information.

### PATH Configuration

In order for `standard` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The SublimeLinter docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

To understand SublimeLinter settings in general, check out:

- [SublimeLinter Settings](http://sublimelinter.com/en/latest/settings.html)
- [Linter Settings](http://sublimelinter.com/en/latest/linter_settings.html)

### Bundler
If you are using Bundler and would like to use the locked version of StandardRB, you will need to set `use_bundle_exec` to true:

```json
{
    "settings": {
        "SublimeLinter.linters.standardrb.use_bundle_exec": true
    }
}
```

## Playing Nice With SublimeLinter-Rubocop

_Assuming you also have the SublimeLinter-Rubocop plugin enabled..._

It's likely that you'll want to use Standard as your linter for some projects and Rubocop directly for others. Since Standard is a [wrapper on top of Rubocop](https://github.com/testdouble/standard#what-you-might-do-if-youre-really-clever) and both linters will lint the same files, having both enabled can give you some conflicting results (such as allowing neither single nor double quoted string literals). There are a couple of ways to prevent conflicts between the two linters.

#### Option 1: Manually Toggle Between Linters

You can use "Disable Package" / "Enable Package" from the command palette to turn linter plugins on or off. You can also use your settings file to enable or disable linter plugins globally. Both of these are pretty terrible user experiences and you really should use one of the other options below.

#### Option 2: Using `.sublime-project` Files

One option for dealing with linter conflicts is to disable one linter in your [global settings file](https://www.sublimetext.com/docs/3/settings.html) and then override the setting on a per-project basis. For example, assuming you want to enable StandardRB globally and use Rubocop only on specific projects, you would first globally disable the rubocop linter in your `Preferences.sublime-settings` file:

```json
{
    "SublimeLinter.linters.rubocop.disable": true
}
```

This will prevent SiblimeLinter from using the Rubocop linter while continuing to allow the SublimeRB linter.

Then, for any project you'd like to lint with Rubocop instead of StandardRB, you can then add the following to your `*.sublime-project` settings:

```json
{
    "settings": {
        "SublimeLinter.linters.rubocop.disable": false,
        "SublimeLinter.linters.standard.disable": true
    }
}

```

The above settings will disable the StandardRB linter and enable Rubocop instead.

This approach works well if you are a heavy user of `.sublime-project` files. The drawback to this approach is that it may not select the linter you want if the project is opened without using the `*.sublime-project` file (e.g. executing `subl ~/path/to/ruby/project` from a terminal prompt).

#### Option 3: Using The `prefer_standard` setting to check for config files

(👆 - Hint: This is probably the one you want.)

A more intelligent (and opinionated) option is to use the `prefer_standard` option. Enabling this option will cause the StanrdardRB linter plugin to selectively enable either the StandardRB or Rubocop linter based on the presence of a corresponding linter config file. The project directory (first folder in the project) and each of it's parent directories are searched first for a `.standard.yml` file, and then for a `.rubocop.yml` file. The corresponding linter will be activated for the first config file found. If no config file is found, StandardRB will be used.

To use the `prefer_standard` option, you'll need to add the following to your global preferences:

```json
{
    "settings": {
        "SublimeLinter.linters.rubocop.disable": null,
        "SublimeLinter.linters.standardrb.disable": null,
        "SublimeLinter.linters.standardrb.prefer_standard": true,
    }
}

```

Note that both linters have their `disable` setting set to `null`, **not** `false`. `true` and `false` are explicit decisions which `prefer_standard` will gladly honor. `null` means you're OK with making no decision and letting `prefer_standard` decide for you.

## Help Us Improve

If you run into problems, please open an [Issue](https://github.com/testdouble/SublimeLinter-contrib-standardrb/issues) or a [Pull Request](https://github.com/testdouble/SublimeLinter-contrib-standardrb/pulls).

## Code of Conduct
This project follows Test Double's [code of conduct](https://testdouble.com/code-of-conduct) for all community interactions, including (but not limited to) one-on-one communications, public posts/comments, code reviews, pull requests, and GitHub issues. If violations occur, Test Double will take any action they deem appropriate for the infraction, up to and including blocking a user from the organization's repositories.

-----

This plugin is largely based on [SublimeLinter-Rubocop](https://github.com/SublimeLinter/SublimeLinter-rubocop)
