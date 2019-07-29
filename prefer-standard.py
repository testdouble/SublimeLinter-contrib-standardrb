import sys
import os
import sublime
import sublime_plugin

class StandardRBPreferStandardListener(sublime_plugin.EventListener):
  def on_activated_async(self, view):
    self.view = view
    self.rubocop_installed = 'SublimeLinter-rubocop' in sys.modules
    self.rubocop_disabled = view.settings().get('SublimeLinter.linters.rubocop.disable')
    self.standard_disabled = view.settings().get('SublimeLinter.linters.standardrb.disable')
    self.should_prefer_standard = view.settings().get('SublimeLinter.linters.standardrb.prefer_standard', False)

    # Don't proceed if we shouldn't be selecting a linter in the first place
    if not self.should_select_linter_to_activate():
      return

    the_linter_we_should_use = self.the_linter_we_should_use()
    if the_linter_we_should_use == 'standard':
      view.settings().set('SublimeLinter.linters.standardrb.disable', False)
      view.settings().set('SublimeLinter.linters.rubocop.disable', True)
    elif the_linter_we_should_use == 'rubocop':
      view.settings().set('SublimeLinter.linters.standardrb.disable', True)
      view.settings().set('SublimeLinter.linters.rubocop.disable', False)
    else:
      view.settings().set('SublimeLinter.linters.standardrb.disable', False)
      view.settings().set('SublimeLinter.linters.rubocop.disable', True)

  def should_select_linter_to_activate(self):
    # If rubocop is not installed we assume the user will set their settings as
    # desired for using standardrb. We can return without doing any decision making
    if not self.rubocop_installed:
      return False

    # If rubocop is explicitly enabled / disabled we respect the user's
    # preference and leave things alone
    if self.rubocop_disabled != None:
      return False

    # If the user has not said that they want us to prefer standardrb then
    # we assume they want to switch between the linters manually
    if not self.should_prefer_standard:
      return False

    return True

  def the_linter_we_should_use(self):
    closest_config = self.get_closest_config_file_path()
    if closest_config == 'standard':
      return 'standard'
    elif closest_config == 'rubocop':
      return 'rubocop'
    else:
      return None

  def get_closest_config_file_path(self):
    project_folders = self.view.window().folders()

    if not project_folders:
      return None

    project_folder = project_folders[0]
    dirs_to_check = []
    current_subpath = []
    path_segments = project_folder.split("/")
    path_segments.remove("")
    for part in path_segments:
      current_subpath.append(part)
      d = os.path.normpath("/" + "/".join(current_subpath))
      dirs_to_check.append(d)

    dirs_to_check.reverse()

    for dir in dirs_to_check:
      print(dir)

    for dir in dirs_to_check:
      standard_config = dir + "/.standard.yml"
      rubocop_config = dir + "/.rubocop.yml"
      if os.path.exists(standard_config):
        return "standard"
      if os.path.exists(rubocop_config):
        return "rubocop"

    return None
