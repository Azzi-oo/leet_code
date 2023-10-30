def create_phone_number(n):
    area_code = ''.join(map(str, n[:3]))
    # Преобразуем следующие три числа в формат XXX-
    first_part = ''.join(map(str, n[3:6]))
    # Преобразуем последние четыре числа в формат XXXX
    second_part = ''.join(map(str, n[6:]))
    
    # Возвращаем строку в формате (XXX) XXX-XXXX
    return f"({area_code}) {first_part}-{second_part}"
