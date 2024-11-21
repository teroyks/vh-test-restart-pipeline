"""First step of a pipeline.

Parses two inputs and passes them on to the next step.
- count: how many pipeline runs there have been
- trigger: URL of the webhook that triggered the pipeline

Inputs can be received either as parameters (when starting the pipeline)
or as inputs (when restarting the pipeline with a webhook).
"""

import json
import valohai

# Parameters are used to initially start the pipeline.
start_parameters = {
    "count": 0,
    # "trigger": "https://valohai.com/webhooks/1234567890",
}

# 'payload.json' is just for testing the entrypoint locally
webhook_inputs = {"payload": "payload.json"}

valohai.prepare(
    step="start-pipeline",
    image="python:3.13-slim",
    default_parameters=start_parameters,
    default_inputs=webhook_inputs,
)

def parse_parameters():
    # On first run, parameters are passed as arguments
    count = valohai.parameters("count").value
    if count:
        return {
            "count": count,
        }

    # On runs triggered by a webhook, parameters are passed as inputs
    with open(valohai.inputs("payload").path()) as payload_file:
        return json.load(payload_file)


parameters = parse_parameters()

print(f"This is run number {parameters.get('count')}")

# pass the parameters to the next step
print(json.dumps(parameters))
