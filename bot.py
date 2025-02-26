import random
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Устанавливаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class Minesweeper:
    def __init__(self, size=5, num_mines=3):
        self.size = size
        self.num_mines = num_mines  # Исправлено: раньше было num_mes
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.game_over = False
        self.setup_mines()

    def setup_mines(self):
        count = 0
        while count < self.num_mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in self.mines:
                self.mines.add((x, y))
                count += 1
                
        for x, y in self.mines:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.board[nx][ny] += 1

    def reveal(self, x, y):
        if self.game_over:
            return "Игра завершена."
        
        if (x, y) in self.mines:
            self.game_over = True
            return f"Ты нажал на мину! Игра окончена. Мины были на: {list(self.mines)}"
        else:
            return f"Ты открыл клетку: {self.board[x][y]} мин вокруг."

    def reset_game(self):
        self.game_over = False
        self.mines = set()
        self.setup_mines()
        return "Игра началась заново!"

# Команда старт
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Это игра Mines. Введи команду /play для начала.')

# Команда игры
def play(update: Update, context: CallbackContext) -> None:
    game = Minesweeper(size=5, num_mines=3)
    context.chat_data['game'] = game
    update.message.reply_text('Игра началась! Введи координаты клетки (например, 1 2), чтобы открыть её.')

# Обработка координат
def handle_coordinates(update: Update, context: CallbackContext) -> None:
    game = context.chat_data.get('game')
    if not game:
        update.message.reply_text("Запусти игру с помощью команды /play.")
        return
    
    try:
        coords = list(map(int, update.message.text.split()))
        if len(coords) != 2:
            update.message.reply_text("Введите две координаты (например, 1 2).")
            return
        x, y = coords
        if x < 0 or y < 0 or x >= game.size or y >= game.size:
            update.message.reply_text("Некорректные координаты. Попробуй снова.")
            return
        
        result = game.reveal(x, y)
        update.message.reply_text(result)
    except ValueError:
        update.message.reply_text("Введите числа для координат (например, 1 2).")

# Основная функция
def main() -> None:
    # Здесь нужно вставить свой токен, полученный от BotFather
    updater = Updater("7859031801:AAEwWRrHvMPGiIZv_21eEIwTElakReOaIuI", use_context=True)

    # Получаем диспетчер для обработки команд
    dispatcher = updater.dispatcher

    # Команды
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    # Обработка сообщений с координатами
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_coordinates))

    # Запуск бота
    updater.start_polling()

    # Ожидаем остановки бота
    updater.idle()

if __name__ == '__main__':
    main()
