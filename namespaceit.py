import sublime
import sublime_plugin
import string

class NamespaceitCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    module_tmpl = string.Template("$name::")
    namespace = ''
    modules = self.view.find_all('module(\s\w+)', sublime.IGNORECASE)
    klass = self.view.find('class(\s\w+)', sublime.IGNORECASE)
    for x in modules:
      mod_name = self.view.substr(x)[7:]
      namespace += module_tmpl.substitute(name=mod_name)
    klass_name = self.view.substr(klass)
    if klass_name is '':
      namespace = namespace[:-2]
    else:
      namespace += klass_name[6:]
    sublime.set_clipboard(namespace)
    # self.view.insert(edit, 0, list)
