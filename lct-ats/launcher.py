import time
import cv2
import numpy as np

from Modules import HandlerDispatcher
from Modules import Context

def detect_barrier(frame):
    # Анализ шлагбаума: поиск красной линии или объекта
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    if cv2.countNonZero(mask) > 1000:  # Порог для обнаружения
        return True  # Шлагбаум закрыт
    return False

def detect_pedestrians(frame):
    # Анализ пешеходов: простой детектор движения или цвета
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Порог для пешехода
            return True
    return False

def detect_traffic_light(frame):
    # Анализ светофора: поиск красного, желтого, зеленого
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Красный
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    if cv2.countNonZero(mask_red) > 500:
        return 'red'
    # Зеленый
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    if cv2.countNonZero(mask_green) > 500:
        return 'green'
    return 'unknown'

def detect_forbidden_zone(frame):
    # Анализ запрещенных зон: поиск синих или красных областей
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    if cv2.countNonZero(mask_blue) > 1000:
        return True
    return False

# Сбрасывается в случае обнаружения критических ошибок
init_ok = True

CTX = Context(init_ok)
HD = HandlerDispatcher(CTX, init_ok)

try:
    while init_ok:
        time.sleep(0.5)
    CTX.lg.error("Завершение работы: ошибка инициализации.")
except KeyboardInterrupt as e:
    CTX.lg.log("KeyboardInterrupt, остановлено пользователем.")
except Exception as e:
    CTX.lg.error(f"Runtime error: {e}")
    init_ok = False
