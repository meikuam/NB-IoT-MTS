import os
import sys

import json
import pandas as pd
from datetime import datetime
import logging

import asyncio
import aiocoap.resource as resource
import aiocoap

sys.path.append("..")
from src.bd.engine.postgres import engine
from src.bd.base import push_data


def data2bd(data):
    push_data(data, "telemetry", engine)


class BlockResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.visible = True

    async def render_post(self, request):
        logging.info(f"POST payload {request.payload}, {request.mtype}")
        payload = request.payload.decode("ascii")
        payload = payload.replace("'", "\"")
        try:
            data = json.loads(payload)
            data["date"] = datetime.now()
            data_df = pd.DataFrame.from_records([data], index=["date"])
            logging.info(f"got: {data_df}")
            data2bd(data_df)
        except Exception as e:
            logging.error(f"render_post {e}")
        return aiocoap.Message(payload="Ok".encode("ascii"))


logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():
    root = resource.Site()

    root.add_resource([".well-known", "core"], resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(["api", "telemetry"], BlockResource())

    asyncio.Task(
        aiocoap.Context.create_server_context(
            root,
            bind=("0.0.0.0", 8889)
        )
    )
    logging.info("CoAP server started")
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
