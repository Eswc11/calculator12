import json
import os
import pygame

user_points = 0
levels = ['easy', 'medium', 'hard']

# Инициализация Pygame
pygame.init()

# Установки окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Викторина")

# Шрифты
font = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 28)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 255)
BUTTON_HOVER_COLOR = (100, 150, 255)


# Чтение данных из файла
def read_file():
    if os.path.exists('questions.json'):
        with open('questions.json', 'r', encoding="UTF-8") as f:
            questions = json.load(f)
            return questions
    else:
        return None


questions = read_file()


# Функция для записи изменений в файл
def write_file():
    with open('questions.json', 'w', encoding="UTF-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)


# Получение вопросов по выбранному уровню
def get_question_by_level(level):
    if level in questions:
        return questions[level]
    else:
        return None


# Добавление очков в зависимости от уровня сложности
def add_points(level):
    global user_points
    if level == "easy":
        user_points += 1
    elif level == "medium":
        user_points += 2
    elif level == "hard":
        user_points += 3


# Функция для отображения текста на экране
def draw_text(text, x, y, font=font, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# Функция для отображения кнопок
def draw_button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(x, y, w, h)

    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, rect)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, rect)

    pygame.draw.rect(screen, BLACK, rect, 2)
    draw_text(text, x + 15, y + 10)

    return False


# Функция для получения вопросов и отображения их с таймером
def get_questions(level):
    global user_points
    questions_level = get_question_by_level(level)

    if questions_level:
        current_question = 0
        input_text = ""
        start_time = pygame.time.get_ticks()  # Время начала вопроса
        time_limit = 10000  # Таймер в миллисекундах (10 секунд)

        while current_question < len(questions_level):
            screen.fill(WHITE)  # Очистка экрана
            question = questions_level[current_question]
            draw_text(f"Вопрос: {question['question']}", 50, 100)
            draw_text("Введите ваш ответ:", 50, 200)

            # Текстовое поле для ввода
            pygame.draw.rect(screen, (200, 200, 255), (50, 250, 700, 50))
            draw_text(input_text, 60, 260, font_small)

            # Отображение текущих очков
            draw_text(f"Очки: {user_points}", 50, 20)

            # Отображение времени, оставшегося на ответ
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, time_limit - elapsed_time)
            draw_text(f"Осталось времени: {remaining_time // 1000} секунд", 50, 300)

            # Если время истекло, переход к следующему вопросу
            if elapsed_time >= time_limit:
                print(f"Время вышло! Ответ не был дан.")
                current_question += 1
                input_text = ""  # Очистить поле ввода
                continue

            pygame.display.update()

            # Обработка ввода с клавиатуры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_text.strip().lower() == question['answer'].lower():
                            add_points(level)
                            print(f"Правильный ответ! Ваши очки: {user_points}")
                        else:
                            print(f"Неправильный ответ. Ваши очки: {user_points}")

                        current_question += 1  # Переход к следующему вопросу
                        input_text = ""  # Очистить поле ввода
                        start_time = pygame.time.get_ticks()  # Сбросить таймер для следующего вопроса
                    else:
                        input_text += event.unicode

            pygame.time.Clock().tick(30)  # Ограничиваем частоту обновлений

    else:
        print("Нет вопросов для выбранного уровня")


# Функция для отображения меню
def show_menu():
    screen.fill(WHITE)  # Очистка экрана
    draw_text("Выберите уровень сложности", 150, 50)

    if draw_button("Легкий", 200, 150, 200, 60):
        get_questions("easy")

    if draw_button("Средний", 200, 250, 200, 60):
        get_questions("medium")

    if draw_button("Сложный", 200, 350, 200, 60):
        get_questions("hard")

    pygame.display.update()


# Главная функция
def main():
    global levels
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        show_menu()  # Показать меню
        pygame.display.update()



main()
