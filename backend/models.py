from django.db import models

# Create your models here.


class Conversation(models.Model): 
    '''
    用户对话内容 
    ''' 
    title = models.CharField(verbose_name="标题", max_length=100)
    
    create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True) 
    update_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)
    moderation_results = models.JSONField(default=list)
    current_node = models.CharField(verbose_name="当前节点", max_length=100)
    conversation_id = models.CharField(verbose_name="对话ID", max_length=100)
    messages = models.JSONField(verbose_name="对话列表",default=list)
    mapping = models.JSONField(verbose_name="对话内容")
    default_model_slug = models.CharField(verbose_name="模型", max_length=100)
    user_id = models.CharField(verbose_name="当前节点", max_length=100)
    
# {
#             "title": "简单 CSS 示例",
#             "create_time": 1716137342.826116,
#             "update_time": 1716137346.355992,
#             "mapping": obj.mapping, 
#             "moderation_results": [],
#             "current_node": "99f8ad4b-d28f-4293-a873-2f3cc809a2c5",
#             "plugin_ids": None,
#             "conversation_id": "9f3d395f-b42a-4373-a603-cd8f084fbc55",
#             "conversation_template_id": None,
#             "gizmo_id": None,
#             "is_archived": False,
#             "safe_urls": [],
#             "default_model_slug": "text-davinci-002-render-sha",
#         }