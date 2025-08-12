import os
import random
import telebot

# Pega o token do bot nas variáveis de ambiente
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Função para gerar o tabuleiro do Mines
def generate_mines_grid(size=5, mines=5):
    grid = [["⬜" for _ in range(size)] for _ in range(size)]
    mine_positions = set()

    while len(mine_positions) < mines:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        mine_positions.add((x, y))

    for (x, y) in mine_positions:
        grid[x][y] = "💣"

    return "\n".join("".join(row) for row in grid)

# Comando /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Bot Mines está ativo! Envie /mine para gerar um jogo.")

# Comando /mine
@bot.message_handler(commands=["mine"])
def send_mines(message):
    grid = generate_mines_grid()
    bot.send_message(message.chat.id, f"💎 *Mines Game* 💎\n\n{grid}", parse_mode="Markdown")

if __name__ == "__main__":
    print("Bot rodando...")
    bot.infinity_polling()
