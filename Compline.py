import sublime, sublime_plugin, re

class ComplineCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		
		def target():
			line = self.view.line(self.view.sel()[0].begin())
			return self.view.substr(line)

		def foo(index):
			if(index > -1):
				line = self.view.line(self.view.sel()[0].begin())
				src = self.view.substr(line)
				position = 0
				match = re.search(r"\S+", src)
				if(match):
					length = match.end() - match.start()
				begin = self.view.sel()[0].begin()-length
				self.view.replace(edit, sublime.Region(begin, self.view.sel()[0].end()), matches[index])
		region = sublime.Region(0, self.view.size())
		lines = self.view.lines(region)
		target = target().strip()
		matches = [self.view.substr(line).lstrip() for line in lines if self.view.substr(line).lstrip().startswith(target)]
		sublime.active_window().show_quick_panel(matches, foo)
