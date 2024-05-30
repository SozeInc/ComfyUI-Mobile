from server import PromptServer
from aiohttp import web
import time

class Cancelled(Exception):
    pass

class FlowControl:
    cancelled = False
    allowProceed = False

    # @classmethod
    # def start(cls, allowProceed):
    #     cls.cancelled = False
    #     cls.allowProceed = allowProceed

    @classmethod
    def proceed(cls):
        cls.cancelled = False
        cls.allowProceed = True

    @classmethod
    def cancel(cls):
        cls.allowProceed = False
        cls.cancelled = True

    @classmethod
    def waitToProceed(cls, period = 0.1):
        while not (cls.allowProceed):
            if cls.cancelled:
                cls.cancelled = False
                raise Cancelled()
            time.sleep(period)
        if cls.cancelled:
            cls.cancelled = False
            raise Cancelled()
        return True

routes = PromptServer.instance.routes
@routes.post('/settings_launcher_flow_control_proceed')
async def make_image_selection(request):
    post = await request.post()
    FlowControl.proceed()
    return web.json_response({})

@routes.post('/settings_launcher_flow_control_cancel')
async def make_image_selection(request):
    post = await request.post()
    FlowControl.cancel()
    return web.json_response({})