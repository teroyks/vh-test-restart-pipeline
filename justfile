# run the pipeline start script locally
# pass the count value as a commadn line argument
local-start count='1':
    python start.py --count={{count}}

# run the webhook entry script locally
# parses the payload from 'payload.json'
# and outputs to stdout
local-restart:
    python webhook-entry.py


# run the process script locally
# pass the count value as a commadn line argument
# default value = no restart
local-process count='0':
    python process.py --count={{count}}

# start the pipeline in adhoc mode
pipeline-start:
    vh pipeline run restart --count=1 --adhoc
