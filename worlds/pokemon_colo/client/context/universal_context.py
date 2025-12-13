import Utils

from CommonClient import CommonContext, ClientCommandProcessor, logger

class UniversalCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext, server_addr: str = None):
        if server_addr:
            ctx.server_address = server_addr
        super().__init__(ctx)

class UniversalContext(CommonContext):
    def __init__(self, server_addr: str, passwd: str):
        """
        Initialize the universal context for Pokemon Colosseum

        :param server_addr: The address of the AP server
        :param passwd: The password for the server, if required
        """
        super().__init__(server_addr, passwd)

    def _main(self):
        pass
