from __future__ import unicode_literals, print_function
from libraries.lambda_handlers.lint_handler import LintHandler
from libraries.linters.obs_linter import ObsLinter


def handle(event, context):
    """
    Invoked by webhook client to run the linter
    :param dict event:
    :param context:
    :return dict:
    """
    return LintHandler(ObsLinter).handle(event, context)
