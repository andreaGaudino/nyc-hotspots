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
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Seleziona un provider"))
            self._view.update_page()
            return

        soglia = self._view.txtInDistanza.value
        if soglia == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Distanza non inserita"))
            self._view.update_page()
            return
        try:
            sogliaFloat = float(soglia)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, soglia inserita non numerica"))
            self._view.update_page()
            return

        self._model.buildGraph(provider, sogliaFloat)
        n, e = self._model.graphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self.fillDDTarget()
        self._view.update_page()

    def handleAnalisiGrafo(self,e):
        n, e = self._model.graphDetails()
        if n == 0 and  e==0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, grafo vuoto"))
            self._view.update_page()
            return

        lista = self._model.getNodesMostVicini()
        #self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("\n\n\nNodi con più vicini:"))
        for l in lista:
            self._view.txt_result.controls.append(ft.Text(f"{l[0]} -- {l[1]}"))
        self._view.update_page()


    def handleCalcolaPercorso(self, e):
        target = self.choiceTarget
        substring = self._view.txtInString.value

        if substring == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, stringa non inserita"))
            self._view.update_page()
            return

        path, source = self._model.getCammino(target, substring)
        if path == []:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Non esiste cammino tra {source} e {target}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Ho trovato cammino tra {source} e {target}"))
        for i in path:
            self._view.txt_result.controls.append(ft.Text(f"{i}"))

        self._view.update_page()



    def fillDDProvider(self):
        providers = self._model.getProviders()
        providers.sort()
        providersDD = list(map(lambda x: ft.dropdown.Option(x), providers))
        self._view.ddProvider.options.extend(providersDD)
        self._view.update_page()

    def fillDDTarget(self):
        locations = self._model.getAllLocations()
        locationsDD = list(map(lambda x: ft.dropdown.Option(data=x, text=x.loc, on_click=self.getSelectedTarget), locations))
        self._view.ddTarget.options.extend(locationsDD)
        self._view.update_page()

    def getSelectedTarget(self, e):
        if e.control.data is None:
            self.choiceTarget = None
        else:
            self.choiceTarget = e.control.data
        print(self.choiceTarget)