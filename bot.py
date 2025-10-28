#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Telegram бот для массажного салона
"""

import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота (из переменной окружения или напрямую)
TOKEN = os.environ.get("BOT_TOKEN", "8303617974:AAHs-XXzV9iB6QYJdeHLengGoEMxDbdvmU4")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    
    # Создаём кнопку-ссылку на канал
    keyboard = [
        [InlineKeyboardButton("Каталог «массажисток» доступен 24/7", url="https://t.me/lovelovesteppe")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = "Твой идеальный вечер с «оКончанием» начинается здесь"
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    logger.info(f"User {user.id} ({user.username}) started the bot")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    # Создаём кнопку-ссылку на канал
    keyboard = [
        [InlineKeyboardButton("Каталог «массажисток» доступен 24/7", url="https://t.me/lovelovesteppe")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    response = "Твой идеальный вечер с «оКончанием» начинается здесь"
    
    await update.message.reply_text(response, reply_markup=reply_markup)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    keyboard = [
        [InlineKeyboardButton("Каталог «массажисток» доступен 24/7", url="https://t.me/lovelovesteppe")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    help_text = "Твой идеальный вечер с «оКончанием» начинается здесь"
    await update.message.reply_text(help_text, reply_markup=reply_markup)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    logger.error(f"Update {update} caused error {context.error}")


def main():
    """Запуск бота"""
    logger.info("🤖 Запуск бота массажного салона...")
    
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)
    
    logger.info("✅ Бот успешно запущен!")
    logger.info("📱 Бот готов к работе: @masagekzbot")
    
    # Запускаем polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if name == "__main__":
    main()
