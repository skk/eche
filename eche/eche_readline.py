# noinspection PyPep8Naming
import os
import readline

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import style_from_dict
from pygments.token import Token


class ReadLine(object):

    last_result = None

    @staticmethod
    def get_bottom_toolbar_tokens(_):
        '''
        Return toolbar to edit subcommand.

        Args:
            _:

        Returns:

        '''
        return [(Token.Toolbar, u'Press Escape+Enter to end editing.')]


    @staticmethod
    def get_rprompt_tokens(_):
        tokens = [
            (Token, ' '),
        ]
        if ReadLine.last_result:
            last_result = ReadLine.last_result if ReadLine.last_result else 'N/A'
            last_result = f"Last Eval: {last_result}"
            tokens.append((Token.RPrompt, last_result))
        return tokens

    def __init__(self):
        self.history_loaded = False
        self.histfile = os.path.expanduser('~/.eche-history')

    def notty_readline(self, prompt_msg='user> '):
        rl = input

        if not self.history_loaded:
            self.history_loaded = True
            try:
                with open(self.histfile, 'r') as hf:
                    for line in hf.readlines():
                        readline.add_history(line.rstrip('\r\n'))
                        pass
            except IOError:
                pass

        try:
            line = rl(prompt_msg)
            readline.add_history(line)
            with open(self.histfile, 'a') as hf:
                hf.write(line + '\n')
        except IOError:
            pass
        except EOFError:
            return None
        return line

    def tty_readline(self, prompt_msg='user> ', style=None, history_filename=None,
                     previous_result=None, vi_mode=True):

        ReadLine.last_result = previous_result

        if style is None:
            style = style_from_dict({
                Token.Toolbar: '#ffffff bg:#333333',
                Token.RPrompt: '#ffffff bg:#333333',
            })

        if history_filename is None:
            history_filename = self.histfile

        history = FileHistory(history_filename)

        text = prompt(prompt_msg,
                      get_rprompt_tokens=ReadLine.get_rprompt_tokens,
                      get_bottom_toolbar_tokens=ReadLine.get_bottom_toolbar_tokens,
                      style=style,
                      history=history,
                      multiline=True,
                      vi_mode=vi_mode,
                      default='')
        return text


def getline(prompt_msg, previous_result=None):
    rl = ReadLine()
    if os.isatty(0):
        return rl.tty_readline(prompt_msg, previous_result=previous_result)
    else:
        return rl.notty_readline(prompt_msg)
