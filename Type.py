import flet as ft
import random

def main(page: ft.Page):
    page.title = "Typing Accuracy Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    word_list = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "horse", "iguana", "jacket",
                 "kite", "lemon", "monkey", "nest", "orange", "penguin", "quail", "rabbit", "snake", "tiger",
                 "orange", "nurse","black", "money"]
    random.shuffle(word_list)
    current_word_index = 0
    total_words = min(15, len(word_list))
    correct_count = 0
    incorrect_count = 0

    word_display = ft.Text(value=word_list[current_word_index], size=30, weight=ft.FontWeight.BOLD)
    status_label = ft.Text(size=20)
    input_field = ft.TextField(hint_text="Type the word", on_submit=check_word)

    def check_word(e):
        nonlocal current_word_index, correct_count, incorrect_count

        user_input = input_field.value.strip()
        if user_input == word_list[current_word_index]:
            status_label.value = "Correct"
            status_label.color = ft.colors.GREEN
            correct_count += 1
        else:
            status_label.value = "Incorrect"
            status_label.color = ft.colors.RED
            incorrect_count += 1

        input_field.value = ""
        page.update()

    page.add(
        ft.Column(
            [
                ft.Row([word_display], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([status_label], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([input_field], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)

