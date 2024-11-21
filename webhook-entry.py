"""Webhook entrypoint for a restarted pipeline.

Gets the parameters in the input payload.
"""

import json
import valohai

default_inputs = {"payload": "payload.json"}

valohai.prepare(
    step="webhook-entry",
    image="python:3.13-slim",
    default_inputs=default_inputs,
)

print(valohai.inputs("payload").path())
with open(valohai.inputs("payload").path()) as payload_file:
    parameters = json.load(payload_file)

print(f"Received parameters: {parameters}")

# pass the parameters to the next step
print(json.dumps(parameters))
