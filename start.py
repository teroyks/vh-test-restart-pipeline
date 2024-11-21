"""First step of a pipeline.

Parses two inputs and passes them on to the next step.
- count: how many pipeline runs there have been
- trigger: URL of the webhook that triggered the pipeline
"""

import valohai

# Parameters are used to initially start the pipeline.
default_parameters = {
    "count": 0,
    # "trigger": "https://valohai.com/webhooks/1234567890",
}


valohai.prepare(
    step="start-pipeline",
    image="python:3.13-slim",
    default_parameters=default_parameters,
)

# Get the count of the current run
count = valohai.parameters("count").value

print(f"This is run number {count}")
