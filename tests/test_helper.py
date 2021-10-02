"""Helper function to run tests."""

import os
import subprocess  # nosec


def run_me(*args, supress_exception=False, cwd=None):
    """Helper to test the django project with the chosen options."""
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        with subprocess.Popen(  # nosec
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as proc:

            out, err = proc.communicate()
            out = out.decode("utf-8")
            err = err.decode("utf-8")
            if err and not supress_exception:
                raise Exception(err)
            if err and supress_exception:
                return out

            return out

    finally:
        os.chdir(cur_dir)
