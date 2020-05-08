#!/usr/bin/env python3

class ProjectMain:

    data = dict()

    def __init__(self):
        pass

    def get_greeting(self):
        return self.data.get('greeting')

    def set_greeting(self, greeting = 'Hello user!'):
        self.data.setdefault('greeting', greeting)
