import flet as ft
from controllers.userController import AuthController
from controllers.TareaController import TareaController
from views.login import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):

    def route_change(e):
        page.views.clear()

        # Caso de seguridad: Si algo falla, mostrar texto de error
        if not page.views:
            page.views.append(
                ft.View(
                    "/",
                    [ft.Text("Error: Ruta no encontrada o vista vacía")]
                )
            )

        page.update()

    page.on_route_change = route_change

    # Forzamos la navegación inicial
    page.go("/")


def main():
    # Ejecución de la app
    ft.app(target=start)


if __name__ == "__main__":
    main()