"""Restart the pipeline if conditions are met.

Pipeline is restarted using a webhook trigger.
Current run count and the trigger URL are passed on to the next iteration.
"""

import valohai

# Set the limit for pipeline runs
MAX_RUNS = 2

default_parameters = {
    "count": 0,  # default: do not restart
    # "trigger": "https://valohai.com/webhooks/1234567890",
}

valohai.prepare(
    step="process",
    image="python:3.13-slim",
    default_parameters=default_parameters,
)

print("Running the pipeline...")

current_count = valohai.parameters("count").value
if not current_count:
    print("No run count parameter passed from previous node. Exiting.")
    exit()

print(f"Current run count: {current_count}")
if current_count >= MAX_RUNS:
    print("Reached the maximum number of runs. Exiting.")
    exit()

print("TODO: Restart the pipeline using the trigger URL.")
