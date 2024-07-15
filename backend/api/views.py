from django.http import (
    HttpResponse,
    StreamingHttpResponse,
    JsonResponse,
    HttpResponseServerError,
)
from common.log import logger
from common.utils.datatools import InstantiatingObjects
from channel.openai.chat_gpt import ChatGPT
import json

# import asyncio
from asgiref.sync import sync_to_async
from ..models import Conversation

from ..serializers import ConversationSerializer, Conversations
from channel.openai.completion import ChatTitle

# 将数据库查询操作转换为异步方法
async_get_conversation = sync_to_async(Conversation.objects.get)


async def conversation(request, conversation_id=None):
    """
    处理POST聊天内容
    """
    if request.method == "POST":
        body = request.body.decode()
        data = json.loads(body)
        # print(data)
        request_data = InstantiatingObjects(**data)  # 将请求数据对象化
        logger.info("正在使用模型 {}".format(request_data.model))
        try:
            chat_stream = ChatGPT(request_data).get_chat()
            response = StreamingHttpResponse(
                chat_stream, content_type="text/event-stream"
            )
            return response
        except:
            return HttpResponseServerError("<h1>Internal Server Error</h1>")

    """
    处理GET聊天内容 
    """
    if conversation_id:
        # obj = Conversation.objects.get(conversation_id=conversation_id)
        obj = await async_get_conversation(conversation_id=conversation_id)
        serializer = ConversationSerializer(obj)
        # print(vars(obj))
        # print(serializer.data)
        # UUIDMSG = {
        #     "title": "简单 CSS 示例",
        #     "create_time": 1716137342.826116,
        #     "update_time": 1716137346.355992,
        #     "mapping": obj.mapping,
        #     "moderation_results": [],
        #     "current_node": "99f8ad4b-d28f-4293-a873-2f3cc809a2c5",
        #     "plugin_ids": None,
        #     "conversation_id": "9f3d395f-b42a-4373-a603-cd8f084fbc55",
        #     "conversation_template_id": None,
        #     "gizmo_id": None,
        #     "is_archived": False,
        #     "safe_urls": [],
        #     "default_model_slug": obj.default_model_slug,
        # }
        return JsonResponse(serializer.data)

    return JsonResponse({"erroe": "error"})


def get_title(request, conversation_id=None):
    try:
        obj = Conversation.objects.get(conversation_id=conversation_id)
        logger.info(f"Messages: {obj.messages}")

        title = ChatTitle(obj.messages, model=obj.default_model_slug)
        obj.title = title
        obj.save()
        return JsonResponse({"code": 200, "data": title, "msg": "ok!"})

    except Exception as e:
        logger.error(f"Error in get_title: {str(e)}")
        return JsonResponse({"code": 500, "msg": "Internal Server Error"})


def get_conversations(request):
    if request.method == "POST":
        body = request.body.decode()
        data = json.loads(body)
        # print(data)
        obj = Conversation.objects.filter(user_id=data["user_id"]).order_by("-id")[0:10]
        serializer = Conversations(obj, many=True)
        get_titles = [
            {
                "items": serializer.data,
                "total": 10,
                "limit": 28,
                "offset": 0,
                "has_missing_conversations": False,
            }
        ]
        # print(get_titles)

        return JsonResponse({"code": 200, "data": get_titles, "msg": "ok!"})

    return JsonResponse({"ERROR": 1})


def del_title(request):
    if request.method == "POST":
        body = request.body.decode()
        data = json.loads(body)
        conversation_id = data["conversation_id"]
        Conversation.objects.get(conversation_id=conversation_id).delete()

        return JsonResponse({"code": 200, "data": "ok", "msg": "ok!"})
