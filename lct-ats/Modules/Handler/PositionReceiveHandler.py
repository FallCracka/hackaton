import random

from Modules import BaseUDPReceiveHandler


class TwinPositionReceiveHandler(BaseUDPReceiveHandler):

    def __init__(self, context, host="0.0.0.0", port=10000):
        super().__init__(context, host, port)

    def _process_message(self, message):
        try:
            robot = self.context.robots.list[0]
            robot.move(message["position_x"] * 1000, message["position_y"] * 1000, message["rotation"])
        except Exception as e:
            self.context.lg.error(f"Ошибка обработки сообщения позиции робота: {e}")


class TwinAutobotReceiveHandler(BaseUDPReceiveHandler):

    def __init__(self, context, host="0.0.0.0", port=10004):
        super().__init__(context, host, port)

    def _process_message(self, message):
        try:
            robot = self.context.robots.list[1]
            robot.move(message["position_x"] * 1000, message["position_y"] * 1000, message["rotation"])
        except Exception as e:
            self.context.lg.error(f"Ошибка обработки сообщения позиции автробота: {e}")


class TwinFillReceiveHandler(BaseUDPReceiveHandler):
    def __init__(self, context, host="0.0.0.0", port=16500):
        super().__init__(context, host, port)

    def _process_message(self, message):
        self.context.field.filled = message
