import sys

import conz
from fabric.api import local
from fabric.context_managers import shell_env

cn = conz.Console(verbose=True)


def run():
    if 'TOKEN' not in sys.argv:
        token = cn.rvpl('Telegram token not set in the environment variable,'
                        ' please input one:')
    else:
        token = sys.argv['TOKEN']
    if 'DEFAULT_CHANNEL' not in sys.argv:
        yes = cn.yesno('Do you want to specify a default channel?')
        if yes:
            default_channel = cn.rvpl('Default channel:')
        else:
            default_channel = '999999'
    else:
        default_channel = sys.argv['DEFAULT_CHANNEL']
    with shell_env(
            TOKEN=token,
            DEFAULT_CHANNEL=default_channel
    ):
        local('PYTHONPATH="$(pwd):$PYTHONPATH" python -m tbs.main')
