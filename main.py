import os
import random
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Função para gerar um sinal Mines
def gerar_sinal_mines():
    minas = random.randint(2, 5)  # número de minas
    posicoes_seguras = random.sample(range(1, 26), 5)  # 5 posições seguras
    multiplicador = round(random.uniform(1.5, 5.0), 2)  # multiplicador estimado
    sinal = (
        "🎯 *Sinal Mines* 🎯\n"
        f"💣 Minas: {minas}\n"
        f"🟦 Clique nas posições: {' '.join(str(p) for p in posicoes_seguras)}\n"
        f"📈 Multiplicador alvo: x{multiplicador}"
    )
    return sinal

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Bot de Sinais Mines ativo! Use /sinal para gerar um.")

@bot.message_handler(commands=["sinal"])
def enviar_sinal(message):
    sinal = gerar_sinal_mines()
    bot.send_message(message.chat.id, sinal, parse_mode="Markdown")

if __name__ == "__main__":
    print("Bot rodando...")
    bot.infinity_polling()
