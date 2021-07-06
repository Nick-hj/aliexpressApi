# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: send_freight
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/6 17:02
# Software: PyCharm

# 主函数

from routers import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8010)
