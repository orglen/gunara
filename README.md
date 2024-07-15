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