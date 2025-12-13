from kvui import GameManager, MDBoxLayout

def build_gui(ui: GameManager):
    ui.pc_layout = MDBoxLayout(orientation="vertical")

    ui.add_client_tab("Pokemon Colosseum", ui.pc_layout)
