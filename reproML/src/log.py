import logging
import os
from collections.abc import Callable
from inspect import signature
from types import FunctionType

from logdecorator import log_on_end, log_on_start

logging.basicConfig(
    level=os.getenv("LOGLEVEL", logging.DEBUG),
    format="{asctime}\t{levelname}\t{message}",
    style="{",
)


def log(callable: Callable) -> Callable:
    """Decorates the function with autmatic logging on start and end.
    With log-level `INFO` start and end times are logged.
    With log-level `DEBUG` arguments and return values are logged additionally.


    Args:
        callable (Callable): Function

    Returns:
        Callable: Decorated function
    """
    if isinstance(callable, FunctionType):
        name = f"{callable.__module__}.{callable.__name__}"
    else:
        name = f"{callable.__module__}.{{callable}}"

    arguments = ", ".join(
        [f"{arg}={{{arg}!r}}" for arg, _ in signature(callable).parameters.items()]
    )
    log_start = log_on_start(
        log_level=logging.INFO,
        message=f"{name} START",
    )
    log_inputs = log_on_start(
        log_level=logging.DEBUG,
        message=f"{name} INPUTS: {arguments}",
    )
    log_end = log_on_end(
        log_level=logging.INFO,
        message=f"{name} END",
    )
    log_ouput = log_on_end(
        log_level=logging.DEBUG,
        message=f"{name} OUTPUT: {{result!r}}",
    )
    callable = log_inputs(callable)
    callable = log_start(callable)
    callable = log_end(callable)
    callable = log_ouput(callable)
    return callable
