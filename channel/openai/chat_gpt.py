import json
from .completion import ChatMessages
from bridge.reply import Reply
from common.utils.CreateNode import ep
from common.log import logger
from backend.models import Conversation
from ..chat_channel import AddNode


class ChatGPT:
    def __init__(self, data):
        self.role = None
        self.action = data.action
        self.model = data.model
        self.messages = data.messages
        self.parent_message_id = data.parent_message_id
        self.msg_content = ""
        self.node = None
        self.conversation_id = getattr(data, "conversation_id", None)
        self.user = data.user_id

    def save_sql(self, conversation_id, messages, system_node):
        Conversation.objects.create(
            conversation_id=conversation_id, 
            messages=messages, 
            mapping=system_node,
            default_model_slug=self.model,
            user_id=self.user
        )

    def get_chat(self):
        add_node = AddNode(
            self.messages,
            self.parent_message_id,
        )
        self.node = ep()

        if self.conversation_id is None:
            system_node = add_node.Initialization()
            system = [{"role": "system", "content": "你是一个有用的助手。"}]
            system.append(
                {"role": "user", "content": self.messages[0]["content"]["parts"][0]}
            )
            self.conversation_id = ep()
            self.save_sql(self.conversation_id, system, system_node)
        else:
            msg = add_node.create_user_message(role="user")
            obj = Conversation.objects.get(conversation_id=self.conversation_id)
            obj.messages.append(
                {"role": "user", "content": self.messages[0]["content"]["parts"][0]}
            )
            obj.mapping.update(msg)
            # print(obj.messages)
            system = obj.messages
            obj.save()

        # print(self.messages[0]['content']['parts'][0])
        content = ChatMessages(system, self.model).get_messages()

        if content.status_code != 200:
            logger.warning("HPPT {} 请求状态异常 ".format(content.status_code))
            # print(content.text)
            reply = Reply("发生异常")
            
            # 发生错误。您请求的引擎不存在，或者在处理您的请求时出现其他问题。如果此问题仍然存在，请通过我们的帮助中心（gunara.cn）与我们联系。
            # An error has occurred. You requested a model text-davinci-003 exception, or other issues while processing your request, http request status code: 503. If this issue persists, please contact us through our Help Center (gunara.cn).
            error = "An error has occurred. You requested a model {} exception,or other issues while processing your request,the current HTTP request status code: {} .  If this issue persists, please contact us through our Help Center (gunara.cn).".format(
                self.model, content.status_code
            )
            yield from reply.get_reply(
                role=self.role,
                node_id=self.node,
                parent_id=self.parent_message_id,
                model=self.model,
                conversation_id=self.conversation_id,
                error=error,
            )
            return

        logger.info("HPPT {} 请求成功 ".format(content.status_code))
        for line in content.iter_lines():
            if not line:
                continue

            data = line.decode("utf-8").replace("data: ", "")
            if data == "[DONE]":
                msg = add_node.create_assistant_message(
                    id=self.node, role="assistant", messages=self.msg_content
                )
                obj = Conversation.objects.get(conversation_id=self.conversation_id)
                obj.messages.append({"role": "assistant", "content": self.msg_content})
                obj.mapping.update(msg)
                obj.save()
                break
            try:
                parsed_data = json.loads(data)
            except:
                print(data)
            yield from self.get_stream(parsed_data.get("choices")[0])

    def get_stream(self, content):
        if content.get("finish_reason") == "stop":
            reply = Reply(self.msg_content)
            yield from reply.get_reply(
                role=self.role,
                node_id=self.node,
                parent_id=self.parent_message_id,
                model=self.model,
                end_turn=True,
                conversation_id=self.conversation_id,
            )
            return

        if content.get("delta").get("role"):
            role = content.get("delta").get("role")
            self.role = role

        if content.get("delta").get("content"):
            self.msg_content += content["delta"]["content"]
        reply = Reply(self.msg_content)

        yield from reply.get_reply(
            role=self.role,
            node_id=self.node,
            parent_id=self.parent_message_id,
            model=self.model,
            conversation_id=self.conversation_id,
        )

