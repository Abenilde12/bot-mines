import telebot
import random

# Configurações
TOKEN = "8300830672:AAFHavzHl5Ku5MaIOR5H3Neurn3RLw1uYWE"
CANAL_ID = -1006265306618

bot = telebot.TeleBot(TOKEN)
historico = {}

def gerar_sinal():
    # Gera 4 casas seguras aleatórias (entre 1 e 25)
    casas = random.sample(range(1, 26), 4)
    return casas

@bot.message_handler(commands=['start_mines'])
def start_mines(message):
    chat_id = message.chat.id
    historico[chat_id] = []
    bot.reply_to(message, "🔎 Sessão iniciada! Envie as minas da última rodada (ex: 2,7,15).")

@bot.message_handler(func=lambda msg: True)
def receber_rodada(message):
    chat_id = message.chat.id
    if chat_id not in historico:
        return

    # Armazena rodada no histórico
    historico[chat_id].append(message.text)

    # Gera sinal simulado
    casas = gerar_sinal()
    sinal = (
        "🚨💎 SINAL MINES 💎🚨\n"
        f"🎯 Casas seguras: {', '.join(str(c) + '️⃣' for c in casas)}\n"
        "📅 Válido para: Próxima rodada\n"
        "⚠️ Jogue rápido antes de expirar!"
    )

    # Envia sinal para o canal
    bot.send_message(CANAL_ID, sinal)

    # Confirma para o usuário
    bot.reply_to(message, "✅ Rodada registrada e sinal enviado no canal!")

print("🤖 Bot rodando...")
bot.polling(non_stop=True)
