#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from demoproject2.crew import Demoproject2
from utils.throttling import throttled_task

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with throttling.
    """
    inputs = {
        'company': 'KANINI',
    }

    try:
        throttled_task(Demoproject2().crew().kickoff, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
