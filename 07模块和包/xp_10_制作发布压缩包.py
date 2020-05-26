# 1、创建setup.py文件
from distutils.core import setup
setup(name="xp_message",  
      version=1.0,
      description="xp's发送和接收消息模块",
      long_description="完整的发送和接收消息模块",
      author="xp",
      author_email="xp.com",
      url="www.xp.com",
      py_modules=["xp_message.send message",
                  "xp_message.receive message"])
# 2、构建模块
# $python3 setuo.py build
# 3、生成发布压缩包
# $python setup.py sdist