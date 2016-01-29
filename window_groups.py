import sublime_plugin


class NextGroup(sublime_plugin.WindowCommand):

    def run(self):
        numGroups = self.window.num_groups()
        currentGroup = self.window.active_group()
        if currentGroup < numGroups - 1:
            newGroup = currentGroup + 1
        else:
            newGroup = 0
        self.window.focus_group(newGroup)


class PrevGroup(sublime_plugin.WindowCommand):

    def run(self):
        numGroups = self.window.num_groups()
        currentGroup = self.window.active_group()
        if currentGroup > 0:
            newGroup = currentGroup - 1
        else:
            newGroup = numGroups - 1
        self.window.focus_group(newGroup)