import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8862547276:AAE0ffYLs60xRY_EOI-41XfgbjH-VmLkCd8"
MAYAN_LINK = "https://t.me/+Ch68WkNbVB5lMmM0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    
    if not args:
        await update.message.reply_text(
            "به ربات سینما لنز خوش آمدید! 🎬\n"
            "لطفاً برای دریافت فیلم‌ها، روی دکمه‌های دانلود در کانال اصلی کلیک کنید."
        )
        return

    code = args[0].strip()
    await update.message.reply_text(f"🔍 در حال پردازش درخواست برای کد {code} ... لطفاً چند لحظه شکیبا باشید.")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
