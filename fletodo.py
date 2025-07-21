import flet as ft


def main(page: ft.Page):
    page.title = "Flet Todo App"
    page.theme_mode = "light"
    page.window.width = 1024
    page.window.height = 768

    new_task = ft.TextField(label="New task", expand=True)
    tasks_column = ft.Column(scroll="auto")

    def add_task(e):
        if not new_task.value:
            return
        task_row = ft.Row([
            ft.Checkbox(label=new_task.value),
            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: tasks_column.controls.remove(task_row))
        ])
        tasks_column.controls.append(task_row)
        new_task.value = ""
        page.update()

    page.add(
        ft.Text("📝 My Todo List", style="headlineMedium"),
        ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_task)]),
        tasks_column
    )


if __name__ == '__main__':
    ft.app(target=main)
