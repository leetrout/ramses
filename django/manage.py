#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # put out project on the py path
    proj_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'ramses',
    )
    sys.path.insert(0, proj_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ramses.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
