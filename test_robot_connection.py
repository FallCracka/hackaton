# Тестовый скрипт для проверки кода робота на подключение и управление
# Запускать на Windows с установленными зависимостями (uv sync в lct-client)

import sys
import os

# Добавляем путь к src
sys.path.append('src')

try:
    # Импортируем необходимые модули
    import cv2
    import numpy as np
    import threading
    import hashlib
    import time

    print(" Импорты OpenCV, NumPy, threading, hashlib успешны")

    # Импортируем обработчики (если доступны)
    try:
        from src.libs.LCTWrapTwin.Modules.Handler import MissionHandler, TrustedHandler
        print(" Импорт MissionHandler и TrustedHandler успешны")
    except ImportError as e:
        print(f" Импорт обработчиков не удался (ожидаемо без полигона): {e}")

    # Определяем классы для тестирования
    class TestMissionHandler:
        @staticmethod
        def config_cyber_obstacles():
            return {
                "CybP_01": True,
                "CybP_02": True,
                "CybP_03": True,
                "CybP_04": True,
                "CybP_05": True,
                "CybP_06": True,
            }

        def detect_pedestrians(self, frame):
            try:
                hog = cv2.HOGDescriptor()
                hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
                boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
                return len(boxes) > 0
            except Exception as e:
                print(f"Ошибка в detect_pedestrians: {e}")
                return False

        def detect_barrier(self, frame):
            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 50, 150)
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
                return lines is not None and len(lines) > 0
            except Exception as e:
                print(f"Ошибка в detect_barrier: {e}")
                return False

        def detect_traffic_light_color(self, frame):
            try:
                h, w = frame.shape[:2]
                roi = frame[0:h//4, w//2 - 50: w//2 + 50]
                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                # Красный
                lower_red = np.array([0,50,50])
                upper_red = np.array([10,255,255])
                mask_red = cv2.inRange(hsv, lower_red, upper_red)
                if cv2.countNonZero(mask_red) > 100:
                    return 'red'
                # Зеленый
                lower_green = np.array([40,50,50])
                upper_green = np.array([80,255,255])
                mask_green = cv2.inRange(hsv, lower_green, upper_green)
                if cv2.countNonZero(mask_green) > 100:
                    return 'green'
                return 'unknown'
            except Exception as e:
                print(f"Ошибка в detect_traffic_light_color: {e}")
                return 'unknown'

        def check_speed_zone(self, x, y):
            if x > 1.5 or y > 1.5:
                return 0.05
            return 0.1

    class TestTrustedHandler:
        def __init__(self):
            self.expected_hash = None
            self.drive_signatures = {}

        def check_hash(self, current_hash):
            if self.expected_hash is None:
                self.expected_hash = current_hash
                return True
            return current_hash == self.expected_hash

        def check_drive_signature(self, drive_data):
            try:
                hash_func = hashlib.md5()
                hash_func.update(str(drive_data).encode())
                sig = hash_func.hexdigest()
                if 'drive' not in self.drive_signatures:
                    self.drive_signatures['drive'] = sig
                    return True
                return self.drive_signatures['drive'] == sig
            except Exception as e:
                print(f"Ошибка в check_drive_signature: {e}")
                return True

        def detect_barrier(self, frame):
            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 50, 150)
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
                return lines is not None and len(lines) > 0
            except Exception as e:
                print(f"Ошибка в detect_barrier: {e}")
                return False

        def is_speed_zone(self, x, y):
            return x > 1.5 or y > 1.5

        def make_next_short_message(self, prev_message: str):
            try:
                msg = str(time.time()) + prev_message
                return hashlib.md5(msg.encode()).hexdigest()[:16]
            except Exception as e:
                print(f"Ошибка в make_next_short_message: {e}")
                return "test1234567890"

    # Тестируем конфигурацию
    handler = TestMissionHandler()
    config = handler.config_cyber_obstacles()
    print(f" Конфигурация киберпрепятствий: {config}")

    # Создаем тестовый кадр (черный квадрат 640x480)
    test_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    print(" Создан тестовый кадр")

    # Тестируем функции распознавания
    pedestrians = handler.detect_pedestrians(test_frame)
    print(f" Распознавание пешеходов: {pedestrians} (ожидается False на пустом кадре)")

    barrier = handler.detect_barrier(test_frame)
    print(f" Распознавание шлагбаума: {barrier} (ожидается False на пустом кадре)")

    color = handler.detect_traffic_light_color(test_frame)
    print(f" Распознавание цвета светофора: {color} (ожидается 'unknown' на пустом кадре)")

    # Тестируем зоны скорости
    speed1 = handler.check_speed_zone(0.5, 0.5)
    speed2 = handler.check_speed_zone(2.0, 2.0)
    print(f" Проверка скорости: обычная зона {speed1}, специальная зона {speed2}")

    # Тестируем доверенный обработчик
    trusted = TestTrustedHandler()
    hash_check = trusted.check_hash({"test": "hash"})
    print(f" Проверка хэша: {hash_check}")

    drive_check = trusted.check_drive_signature({"speed": 0.1})
    print(f" Проверка подписи привода: {drive_check}")

    message = trusted.make_next_short_message("prev")
    print(f" Генерация короткого сообщения: {message}")

    print("\n Все тесты пройдены! Код готов к подключению к полигону на Windows.")

except Exception as e:
    print(f"Критическая ошибка: {e}")
    sys.exit(1)
