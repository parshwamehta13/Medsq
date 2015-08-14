#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ID.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 3c873b68ce8825b7e217afa99bd6461b933af4ee

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
