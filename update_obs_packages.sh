#!/bin/bash

PROJECT="home:nukeddd:JetbrainsIDE"


# 1. Проверяем, что мы находимся в Git-репозитории
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Ошибка: Скрипт должен быть запущен из корневой папки вашего Git-репозитория."
    exit 1
fi

echo "==> 1. Обновление локального репозитория..."
OLD_HEAD=$(git rev-parse HEAD)
git pull

if [ $? -ne 0 ]; then
    echo "Ошибка: 'git pull' не удался. Проверьте ваше соединение и настройки git."
    exit 1
fi

NEW_HEAD=$(git rev-parse HEAD)

if [ "$OLD_HEAD" == "$NEW_HEAD" ]; then
    echo "Новых изменений в репозитории нет. Завершение работы."
    exit 0
fi

echo "==> 2. Поиск измененных .spec файлов..."

PACKAGES_TO_UPDATE=$(git diff --name-only "$OLD_HEAD" "$NEW_HEAD" | grep '\.spec$' | xargs -n 1 dirname | sort -u)


if [ -z "$PACKAGES_TO_UPDATE" ]; then
    echo "В последнем обновлении не было изменений в .spec файлах."
    exit 0
fi

echo "==> 3. Запуск обновления для следующих пакетов на OBS:"
echo "----------------------------------------------------"
echo "$PACKAGES_TO_UPDATE"
echo "----------------------------------------------------"

# 4. Запускаем remoterun для каждого найденного пакета
for PACKAGE_DIR in $PACKAGES_TO_UPDATE; do
    # Получаем чистое имя папки (на случай если путь был ./clion)
    PACKAGE_NAME=$(basename "$PACKAGE_DIR")
    
    echo "-> Запускаем 'osc service remoterun' для пакета [$PACKAGE_NAME]..."
    osc service remoterun "$PROJECT" "$PACKAGE_NAME"
    
    if [ $? -eq 0 ]; then
        echo "   ...Успешно запущено для пакета [$PACKAGE_NAME]."
    else
        echo "   ...Ошибка при запуске для пакета [$PACKAGE_NAME]."
    fi
done

echo "==> Готово."
