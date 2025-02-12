import flet as ft
import random

def main(page: ft.Page):
    page.title = "Typing Accuracy Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    word_list = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "horse", "iguana", "jacket",
                 "kite", "lemon", "monkey", "nest", "orange", "penguin", "quail", "rabbit", "snake", "tiger"]
    random.shuffle(word_list)
    current_word_index = 0
    total_words = min(15, len(word_list))

    word_display = ft.Text(value=word_list[current_word_index], size=30, weight=ft.FontWeight.BOLD)
    page.add(word_display)

ft.app(target=main)




