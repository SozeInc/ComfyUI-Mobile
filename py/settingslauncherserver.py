# from server import PromptServer
# from aiohttp import web
# import time

# class Cancelled(Exception):
#     pass

# class MessageHolder:
#     messages = {}
#     cancelled = False
    
#     @classmethod
#     def addMessage(cls, id, message):
#         if message=='__cancel__':
#             cls.messages = {}
#             cls.cancelled = True
#         elif message=='__start__':
#             cls.messages = {}
#             cls.cancelled = False
#         else:
#             cls.messages[str(id)] = message
    
#     @classmethod
#     def waitForMessage(cls, id, period = 0.1):
#         print("[ComfyMobile][waitForMessage] Waiting for message with id: " + str(id))
#         sid = str(id)
#         while not (sid in cls.messages) and not ("-1" in cls.messages):
#             if cls.cancelled:
#                 cls.cancelled = False
#                 print("[ComfyMobile][waitForMessage] Cancelled Called")
#                 raise Cancelled()
#             time.sleep(period)
#         if cls.cancelled:
#             cls.cancelled = False
#             print("[ComfyMobile][waitForMessage] Cancelled Called")
#             raise Cancelled()
#         message = cls.messages.pop(str(id),None) or cls.messages.pop("-1")
#         print("[ComfyMobile][waitForMessage] return message: " + int(message.strip()))
#         return int(message.strip())

# routes = PromptServer.instance.routes
# @routes.post('/settings_launcher_message')
# async def make_image_selection(request):
#     post = await request.post()
#     MessageHolder.addMessage(post.get("id"), post.get("message"))
#     return web.json_response({})