"""
Test script to verify the updated "Novo" dialog with photo placeholder.
This launches the profile page and automatically opens the create post dialog.
"""
import flet as ft


def main(page: ft.Page):
    """Launch profile page with dialog for testing."""
    page.title = "Test - Nova Publicação Dialog"
    page.bgcolor = "#f5f5f5"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def close_dialog(e):
        dialog.open = False
        page.update()

    def add_photos_placeholder(e):
        photo_status.value = "📸 Função de adicionar fotos em breve..."
        photo_status.color = "#666"
        page.update()

    def submit_post(e):
        status_text.value = "Post criado com sucesso! ✓"
        status_text.color = "#4CAF50"
        page.update()

    # Dialog fields
    post_title = ft.TextField(
        label="Título",
        hint_text="Ex: Bicicleta usada, Aula de violão...",
        width=400,
        border_radius=10,
    )

    post_description = ft.TextField(
        label="Descrição",
        hint_text="Descreva o que você oferece ou procura",
        width=400,
        multiline=True,
        min_lines=3,
        max_lines=5,
        border_radius=10,
    )

    # Photo upload placeholder
    photo_status = ft.Text("", size=12, italic=True)
    
    add_photos_button = ft.Container(
        content=ft.Column(
            [
                ft.Icon(
                    ft.Icons.ADD_PHOTO_ALTERNATE,
                    size=40,
                    color="#4CAF50",
                ),
                ft.Text(
                    "Adicionar Fotos",
                    size=14,
                    color="#4CAF50",
                    weight=ft.FontWeight.W_500,
                ),
                photo_status,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        ),
        on_click=add_photos_placeholder,
        border=ft.border.all(2, "#4CAF50"),
        border_radius=10,
        padding=20,
        width=400,
        ink=True,
    )

    status_text = ft.Text("", size=12)

    # Dialog
    dialog = ft.AlertDialog(
        title=ft.Text("Criar Nova Publicação"),
        content=ft.Column(
            [
                post_title,
                post_description,
                add_photos_button,
                status_text,
            ],
            tight=True,
            spacing=15,
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=close_dialog),
            ft.ElevatedButton(
                "Publicar",
                bgcolor="#4CAF50",
                color="white",
                on_click=submit_post,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(dialog)
    dialog.open = True
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
