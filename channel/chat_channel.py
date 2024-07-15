
from common.utils.CreateNode import ep

class AddNode:
    def __init__(
        self,
        messages,
        parent_message_id,
    ):
        self.messages = messages
        self.parent_message_id = parent_message_id

    def create_system(
        self,
    ):
        system_node = ep()
        system_parent_node = ep()
        system = {
            system_node: {
                "id": system_node,
                "message": {
                    "id": system_node,
                    "author": {"role": "system", "name": None, "metadata": {}},
                    "create_time": None,
                    "update_time": None,
                    "content": {"content_type": "text", "parts": [""]},
                    "status": "finished_successfully",
                    "end_turn": True,
                    "weight": 0.0,
                    "metadata": {"is_visually_hidden_from_conversation": True},
                    "recipient": "all",
                },
                "parent": system_parent_node,
                "children": [self.messages[0].get("id")],
            },
            system_parent_node: {
                "id": system_parent_node,
                "message": None,
                "parent": None,
                "children": [system_node],
            },
        }
        return system

    def create_user_message(self, role):
        user_message_node = {
            self.messages[0].get("id"): {
                "id": self.messages[0].get("id"),
                "message": {
                    "id": self.messages[0].get("id"),
                    "author": {"role": role, "name": None, "metadata": {}},
                    "create_time": 1716137342.828762,
                    "update_time": None,
                    "content": {
                        "content_type": "text",
                        "parts": self.messages[0]["content"]["parts"],
                    },
                    "status": "finished_successfully",
                    "end_turn": None,
                    "weight": 1.0,
                    "metadata": {
                        "request_id": "886593f779ad51e2-DEN",
                        "message_source": None,
                        "timestamp_": "absolute",
                        "message_type": None,
                    },
                    "recipient": "all",
                },
                "parent": self.parent_message_id,
                "children": ["99f8ad4b-d28f-4293-a873-2f3cc809a2c5"],
            },
        }
        return user_message_node

    def create_assistant_message(
        self, id=None, role=None, messages=None, parent_message_id=None
    ):
        assistant_message_node = {
            id: {
                "id": id,
                "message": {
                    "id": id,
                    "author": {"role": role, "name": None, "metadata": {}},
                    "create_time": 1716137342.828762,
                    "update_time": None,
                    "content": {
                        "content_type": "text",
                        "parts": [messages],
                    },
                    "status": "finished_successfully",
                    "end_turn": None,
                    "weight": 1.0,
                    "metadata": {
                        "request_id": "886593f779ad51e2-DEN",
                        "message_source": None,
                        "timestamp_": "absolute",
                        "message_type": None,
                    },
                    "recipient": "all",
                },
                "parent": self.parent_message_id,
                "children": ["99f8ad4b-d28f-4293-a873-2f3cc809a2c5"],
            },
        }
        return assistant_message_node

    def Initialization(self):
        """
        对对话内容初始化
        """
        message_node = self.create_user_message("user")
        system_node = self.create_system()
        system_node.update(message_node)
        return system_node
