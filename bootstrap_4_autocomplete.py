import sublime_plugin
import sublime
from .bootstrap_4_data import classes as bs4_classes

class Bootstrap4Completions(sublime_plugin.EventListener):

    def __init__(self):

        self.class_completions = [("%s \tBootstrap 4.4 Class" % s, s) for s in bs4_classes]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "text.html string.quoted"):


            LIMIT  = 250

            cursor = locations[0] - len(prefix) - 1

            start  = max(0, cursor - LIMIT - len(prefix))

            line   = view.substr(sublime.Region(start, cursor))

            parts  = line.split('=')

            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

            return self.data_completions

        else:

            return []
