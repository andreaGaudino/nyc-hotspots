import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        provider = self._view.ddProvider.value
        if provider is None:
            print("Seleziona un provider")
            self._view._txt_results.controls.clear()
            self._view._txt_results.controls.append(ft.Text("Seleziona un provider"))
            self._view.update_page()
            return
        self._model.buildGraph(provider)
        n, e = self._model.graphDetails()
        self._view._txt_results.controls.clear()
        self._view._txt_results.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self._view.update_page()

    def handleAnalisiGrafo(self,e):
        pass

    def handleCalcolaPercorso(self, e):
        pass

    def fillDDProvider(self):
        providers = self._model.getProviders()
        providers.sort()
        providersDD = list(map(lambda x: ft.dropdown.Option(x), providers))
        self._view.ddProvider.options.extend(providersDD)
        self._view.update_page()