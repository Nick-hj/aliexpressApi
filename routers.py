# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: routers
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/8 14:55
# Software: PyCharm

# 注册路由

from apps.ae_freight import views as ae_views
from apps.goodsApi import views as goods_views
from fastapi import FastAPI
def create_app():
    app = FastAPI()
    app.include_router(ae_views.router, prefix="/aliexpress", tags=["aliexpress"])
    app.include_router(goods_views.router, prefix="/goodsApi", tags=["goodsApi"])
    return app
