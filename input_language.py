""" This program inputs a list of return values """


from languages import language_name_list
every_language = []

# prints out the possible langauge 
for i in range(len(language_name_list)):
    every_language.append(language_name_list[i][1]) 
    print(language_name_list[i][1])



# UI - allow send message on input so that user finds language easier
import readline

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

completer = MyCompleter(every_language)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

# asks for the langauge you want
language = input("Select a language: ")
# name = shortcut

name = language_name_list[every_language.index(language)][0]

print('%s , %s' % (language,name))
