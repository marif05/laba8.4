import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # Проверяем, есть ли указанный друг в словаре DATABASE
    if friend in DATABASE:
        # Получаем город проживания друга
        city = DATABASE[friend]
        
        # Проверяем, есть ли указанный город в словаре UTC_OFFSET
        if city in UTC_OFFSET:
            # Получаем текущее время в UTC
            utc_now = dt.datetime.utcnow()
            
            # Получаем смещение для указанного города
            offset = UTC_OFFSET[city]
            
            # Вычисляем текущее время в указанном городе
            local_time = utc_now + dt.timedelta(hours=offset)
            
            # Возвращаем время в формате строки
            return local_time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return 'Город друга не найден в словаре UTC_OFFSET'
    else:
        return 'Друг не найден в словаре DATABASE'

print(what_time('Соня'))
