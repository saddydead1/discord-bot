# DISCORD-BOT ON PYTHON

***!!! Это не готовый бот, а скорее шаблон для создания своего !!!***

# Start.bat (windows)
Для запуска бота запустите файл Start.bat


*@echo off*

*python <ИМЯ ФАЙЛА БОТА>.py*


# Start (Linux)
Для запуска на Linux создайте файл .sh с таким кодом:

*python <ИМЯ ФАЙЛА БОТА>.py*

после выдайте разрешение для файла командой: *sudo chmod +x <ИМЯ ФАЙЛА>.sh*

# Bot.py 

в *#connect* мы обращаемся к файлу *token.txt*, где лежит наш токен бота( конечно же перед этим нужно создать бота  тут -> *https://discord.com/developers* )
при успешном запуске бота в консоль будет выводить *Bot started*
в боте реализована простая команда *hello* и команда *mute*
