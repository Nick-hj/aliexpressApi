# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: routers
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/8 14:55
# Software: PyCharm

# 注册路由

from apps.goodsApi import views as goods_views
from fastapi import FastAPI
def create_app():
    app = FastAPI()
    app.include_router(goods_views.router, prefix="/api/aliexpress", tags=["aliexpress"])
    return app
