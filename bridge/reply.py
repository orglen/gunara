"""
统一流式推送格式
"""
import json
import time
class Reply:
    def __init__(self, content):
        self.content = content

    def get_reply(
        self,
        role = None,
        node_id=None,
        parent_id=None,
        conversation_id=None,
        end_turn=None,
        error=None,
        model=None
    ):
            
        message = {
            "message": {
                "id": node_id,
                "author": {"role": role, "name": None, "metadata": {}},
                "create_time": 1708270228.201246,
                "update_time": None,
                "content": {"content_type": "text", "parts": [self.content,]},
                "status": "in_progress",
                "end_turn": end_turn,
                "weight": 1.0,
                "metadata": {
                    "citations": [],
                    "gizmo_id": None, 
                    "message_type": "next",
                    "model_slug": model,
                    "parent_id": parent_id,
                },
                "recipient": "all",
            },
            "conversation_id": conversation_id,
            "error": error,
        }
        reply = "data: " + str(json.dumps(message)) + "\n"
        
        yield reply
        yield '\n'
        # time.sleep(0.02)
    
            
