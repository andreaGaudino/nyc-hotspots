import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "NYC Wi-Fi hotspot"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        # self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(ft.Text("NYC Wi-Fi hotspot", color="blue", size=24))

        #row 1
        self.ddProvider = ft.Dropdown(label="Provider")
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([ft.Container(self.ddProvider, width=300), ft.Container(self.btnCreaGrafo, width=200)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #row 2
        self.txtInDistanza = ft.TextField(label="Distanza")
        self.btnAnalisiGrafo = ft.ElevatedButton(text="Analisi grafo", on_click=self._controller.handleAnalisiGrafo)
        row2 = ft.Row([
            ft.Container(self.txtInDistanza, width=300),
            ft.Container(self.btnAnalisiGrafo, width=200)], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        #row 3
        self.txtInString = ft.TextField(label="Stringa")
        self.btnCalcolaPercorso = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handleCalcolaPercorso)
        row3 = ft.Row([ft.Container(self.txtInString, width=300),
                       ft.Container(self.btnCalcolaPercorso, width=200)], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row3)

        #row4
        self.ddTarget = ft.Dropdown(label='Target')
        row4 = ft.Row([ft.Container(self.ddTarget, width=300), ft.Container(None, width=200)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
