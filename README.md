# light_of_grace_dota2
Это удалятор доты 2(стимовской) с вашего пк
- Если вам просто нужно активировать другу, скачивайте только .exe файлы
- Doka2_deleter.exe - добавляет в автозагрузку(без консоли)
- Doka2_enabler.exe - убирает из автозагрузки(с консолью)
Нужна для урродов которые немогут удалить её сами
- Перейменовывать .exe файлы НЕЛЬЗЯ!
- Работа происходит без консоли и окон - в процессе
- Добавляется в автозагрузку через ярлык
- Легко убрать, запустите Doka2_enabler.exe чтобы убрать из автозапуска

# Чтото изменить, доработать
Нужные библиотеки:

pip install pyinstaller winreg pytest-shutil winshell pypiwin32

Создать .exe файл

С консолью:
pyinstaller.exe -F -i ./icon.ico Doka2_enabler.py

Спрятать консоль:
pyinstaller.exe -w -F -i ./icon.ico Doka2_deleter.py

- .exe файл будет лежать в папке /dist

