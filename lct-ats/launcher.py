import time
import sys
import os

import sys
print(sys.path)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modules import HandlerDispatcher
from Modules import Context

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
