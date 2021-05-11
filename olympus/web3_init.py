import os

for envvar in ('WEB3_INFURA_PROJECT_ID', 'WEB3_INFURA_API_SECRET'):
    if envvar not in os.environ:
        raise RuntimeError(
            f"Envvar {envvar} must be set. If you do not have an Infura"
            " set up, please go to https://infura.io/ to get started."
            " Don't forget to enable 'Require project secret for all requests.'"
        )

from web3.auto.infura import w3