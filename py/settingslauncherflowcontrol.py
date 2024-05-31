from server import PromptServer # type: ignore
from aiohttp import web # type: ignore
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
        try:
            cls.cancelled = False
            cls.allowProceed = True
        except Exception as e:
            print("[ComfyMobile][FlowControl.proceed] " + str(e))

    @classmethod
    def cancel(cls):
        try:
            cls.allowProceed = False
            cls.cancelled = True
        except Exception as e:
            print("[ComfyMobile][FlowControl.cancel] " + str(e))

    @classmethod
    def waitToProceed(cls, period = 0.1)->bool:
        try:
            cls.allowProceed = False
            cls.cancelled = False
            while not (cls.allowProceed):
                if cls.cancelled:
                    return False
                time.sleep(period)
            if cls.cancelled:
                return False
            return True
        except Exception as e:
            print("[ComfyMobile][FlowControl.waitToProceed] " + str(e))
            return False


routes = PromptServer.instance.routes
@routes.post('/settings_launcher_flow_control_proceed')
async def flowcontrolproceed(request):
    FlowControl.proceed()
    return web.json_response({})

@routes.post('/settings_launcher_flow_control_cancel')
async def flowcontrolcancel(request):
    FlowControl.cancel()
    return web.json_response({})