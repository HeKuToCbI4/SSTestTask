from collections import namedtuple


class Message(namedtuple('Message', 'author body date_posted')):
    def __str__(self):
        return f'author: {self.author} body: {self.body} posted at: {self.date_posted}'
