import flet as ft

def Login(page, auth_controller):
    email_input = ft.TextField(label="Correo electrónico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=350, border_radius=10)

    def login_click(e):
        user = auth_controller.login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error de autenticación"))
            page.snack_bar.open = True
        page.update()

    return ft.View(
        "/login",
        [
            ft.AppBar(
                title=ft.Text("SIGE - Login"),
                bgcolor=ft.colors.BLUE_GREY_800,
                color="white"
            ),
            ft.Column(
                [
                    
                    ft.Text("Acceso al Sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    ft.ElevatedButton("Entrar", on_click=login_click, width=350),
                    ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )