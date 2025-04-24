import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# گرفتن اطلاعات از متغیرهای محیطی
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.environ.get("ADMIN_CHAT_ID"))

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! لطفاً درخواست استعلام قیمت خود را وارد کنید.")

# دریافت پیام از کاربر و ارسال به ادمین
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    message = f"📩 استعلام قیمت جدید:\n\n👤 {user.full_name} (@{user.username})\n📝 {text}"

    # ارسال پیام به ادمین
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)
    # پاسخ به کاربر
    await update.message.reply_text("پیام شما دریافت شد. در اسرع وقت پاسخ داده خواهد شد.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات فعال است...")
    app.run_polling()
