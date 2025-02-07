# 使用 Python 运行环境
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制当前目录的文件到容器
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行 API 服务器
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
