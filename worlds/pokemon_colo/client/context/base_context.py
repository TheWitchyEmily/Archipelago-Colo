""" Pokemon Colosseum Base Context """

import asyncio, random, copy
import Utils

from .universal_context import UniversalContext, UniversalCommandProcessor, logger
from ...client.constants import *
from ..links.network_engine import ArchipelagoNetworkEngine

import dolphin_memory_engine as dme

class BaseContext(UniversalContext):
    network_engine: ArchipelagoNetworkEngine

    def __init__(self, server_address, password):
        """
        Initialize Pokemon Colosseum's Universal Context

        :param server_address: Address of the Archipelago server
        :param password: Password for server authentication
        """
        super().__init__(server_address, password)
        self.network_engine = ArchipelagoNetworkEngine(self)
        self.already_fired_events = False

    async def wait_for_next_loop(self, time_to_wait: float):
        await asyncio.sleep(time_to_wait)

    def on_connected(self, args):
        tags: list[str] = []
        # Added for when tags will be added later (like trap link or energy link)
        if len(tags) > 0:
            Utils.async_start(self.network_engine.update_client_tags_async(tags), name="UpdateClientTags")

        slot_data = args["slot_data"]

    def make_gui(self):
        from .pc_tab import build_gui, GameManager

        ui: GameManager = super().make_gui()
        class PCGuiWrapper(ui):
            base_title = f"Pokemon Colosseum {CLIENT_VERSION}"

            def build(self):
                container = super().build()

                self.base_title += " | AP"
                build_gui(self)

                return container
        return PCGuiWrapper

class BaseCommandProcessor(UniversalCommandProcessor):
    def __init__(self, ctx: BaseContext, server_address: str = None):
        if server_address:
            ctx.server_address = server_address
        super().__init__(ctx)
