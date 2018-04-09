tbs example
===========

A project to demonstrate tbs capabilities with some sample scripts and
some basic configuration.

Use [pipenv](https://docs.pipenv.org/) to install the dependencies and
run it with [fabric](http://www.fabfile.org/) (`fab run`) in the root
directory of this project.

The run function goes over a few environment variables and set them for
you. If you want to use this in production, make sure that the variables
are set before running fabric.

For more instructions on what each variable does check the
[tbs README](https://github.com/marceloslacerda/tbs/blob/master/README.rst).

Once your bot is up and running search for it on telegram and start
talking to it. Talking in private should always work.

To talk to it in a group you have to add it to the group and make it
admin, otherwise it will not be able to read your messages. You also
have to begin all your commands with it's name and it's aliases, it
will inform you what are those when you send him --help or -h.

The bot always takes interprets as case insensitive unless if you wrap
some term with quotes (single or double). For instance:

When you send `mybot hello` the bot will respond with `Hi!` but if you
send `mybot "Hello"` it will inform you that Hello is not a valid
command.

License
-------

Copyright (C) 2018  Marcelo de Sena Lacerda <marceloslacerda@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
