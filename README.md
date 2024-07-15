# Hello Gunara

## 简介

Gunara 是一个基于 Python 和 React 的高仿 ChatGPT UI 项目。仅供学习交流。

## 功能

- 基本的对话功能
- 支持自定义模型
- 体验地址 [Gunara](https://chat.liushuiyin.com)

## 环境要求

- Python 3.11+
- Django 5.0+

## 安装

### 克隆项目

```bash
git clone https://github.com/orglen/gunara.git
cd gunara
```

### 创建虚拟环境

建议使用 `virtualenv` 创建一个虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate
```

### 安装依赖

使用 `pip` 安装所有依赖项：

```bash
pip install -r requirements.txt
```

### 数据库迁移

执行以下命令来应用数据库迁移：

```bash
python manage.py migrate
```


### 启动开发服务器

运行以下命令启动开发服务器：

```bash
python manage.py runserver
```

### 📝Docker 部署

#### 前提条件

1. 安装 Docker 和 Docker Compose。
2. 确保 `Dockerfile` 和 `docker-compose.yml` 文件已经存在于项目根目录中。
3. 确保 `run.sh` 文件已经存在并具有执行权限。

#### 配置环境变量
在项目根目录下，创建一个名为 `.env` 的文件并添加以下内容：

```.env
# .env 文件内容
OPENAI_API_KEY=sk-Zv4RIpllri6===========476bF74d14B5F20eD7CbBa346b
ENDPOINT=https://api.liushuiyin.com
MODELS_JSON=[
    {
        "slug": "gpt-3.5-turbo-1106",
        "max_tokens": 8191,
        "title": "ChatGPT",
        "model": "GPT-3.5",
        "version": "3.5",
        "description": "Great for everyday tasks",
        "msg": "",
        "image_url": "image_url",
        "professional": false,
        "tags": [
            "gpt3.5"
        ],
        "capabilities": {},
        "product_features": {}
    },
    {
        "slug": "text-davinci-003",
        "max_tokens": 8191,
        "title": "ChatGPT",
        "model": "text-davinci-003",
        "version": "text-davinci-003",
        "description": "自然语言生成模型",
        "msg": "",
        "image_url": "image_url",
        "professional": false,
        "tags": [
            "gpt3.5"
        ],
        "capabilities": {},
        "product_features": {}
    },
    {
        "slug": "gpt-4-1106-preview",
        "max_tokens": 8191,
        "title": "ChatGPT",
        "model": "GPT-4",
        "version": "4-preview",
        "description": "gpt-4-1106-preview 模型",
        "msg": "测试中",
        "image_url": "image_url",
        "professional": false,
        "tags": [
            "gpt3.5"
        ],
        "capabilities": {},
        "product_features": {}
    },
    {
        "slug": "yi-34b-chat-0205",
        "max_tokens": 8191,
        "title": "零一万物",
        "model": "零一万物",
        "version": "PRO",
        "description": "零一万物-AI2.0大模型技术和应用的全球公司",
        "msg": "Limit 40 messages / 3 hours",
        "image_url": "image_url",
        "professional": false,
        "tags": [
            "gpt3.5"
        ],
        "capabilities": {},
        "product_features": {}
    },
    {
        "slug": "gemini-pro",
        "max_tokens": 8191,
        "title": "Gemini",
        "model": "Gemini",
        "version": "pro-vision",
        "description": "谷歌 Gemini 大模型",
        "msg": "Limit 40 messages / 3 hours",
        "image_url": "image_url",
        "professional": false,
        "tags": [
            "gpt3.5"
        ],
        "capabilities": {},
        "product_features": {}
    },
    {
        "slug": "deepseek-chat",
        "max_tokens": 8191,
        "title": "Deepseek",
        "model": "Deepseek",
        "version": "chat",
        "description": "Deepseek 大模型",
        "msg": "Limit 40 messages / 3 hours",
        "image_url": "image_url",
        "professional": false,
        "tags": [
            "gpt3.5"
        ],
        "capabilities": {},
        "product_features": {}
    }
]
```

你也可以修改`run.sh`文件中的环境变量, 然后执行 `./run.sh` 启动应用程序。

服务器启动后，可以在浏览器中访问 `http://127.0.0.1:8000/` 查看应用程序。

## 配置

`config/.env`  配置api_key 和代理url

`Gunara/config.py` 自定义模型

## 代理

OpenAI 接口聚合管理，支持多种渠道包括 [ORGLEN API](https://orglen.com)

价格低至 1:1

### 数据库

默认情况下，Gunara 使用 SQLite 作为数据库。如果你想使用其他数据库（例如 PostgreSQL 或 MySQL），请在 `settings.py` 文件中修改 `DATABASES` 配置。

### 静态文件

确保在生产环境中正确配置静态文件。参考 Django 文档获取更多信息。

### 欢迎加群

QQ群:823830031
