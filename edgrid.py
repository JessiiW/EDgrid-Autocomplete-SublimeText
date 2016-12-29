import sublime
import sublime_plugin


edgrid_classes = [
"ed-container","ed-item","button","ed-video","main-nav-toggle","main-nav","main-menu","to-center",
"to-left","to-right","full","circle","clearfix","no-padding","no-padding-2","no-padding-3","sticky-footer",
"main-justify","main-distribute","main-center","main-start","main-end","cross-start","cross-center",
"cross-end","flex-reverse","flex-column","flex-column-reverse","abcenter","from-s","to-s","from-m","to-m",
"from-l","to-l","from-xl","to-xl","s-5","s-10","s-15","s-20","s-25","s-30","s-35","s-40","s-45","s-50",
"s-55","s-60","s-65","s-70","s-75","s-80","s-85","s-90","s-95","s-100","m-5","m-10","m-15","m-20","m-25",
"m-30","m-35","m-40","m-45","m-50","m-55","m-60","m-65","m-70","m-75","m-80","m-85","m-90","m-95","m-100",
"l-5","l-10","l-15","l-20","l-25","l-30","l-35","l-40","l-45","l-50","l-55","l-60","l-65","l-70","l-75",
"l-80","l-85","l-90","l-95","l-100","xl-5","xl-10","xl-15","xl-20","xl-25","xl-30","xl-35","xl-40","xl-45",
"xl-50","xl-55","xl-60","xl-65","xl-70","xl-75","xl-80","xl-85","xl-90","xl-95","xl-100"
]

class edgridCompletions(sublime_plugin.EventListener):
    def __init__(self):

        self.class_completions = [("%s \tEDgrid V2.0" % s, s) for s in edgrid_classes]

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
        elif view.match_selector(locations[0], 
        	"text.html meta.tag - text.html punctuation.definition.tag.begin"):

            return self.data_completions

        else:
            return []