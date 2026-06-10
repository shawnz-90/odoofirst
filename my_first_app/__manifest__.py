{
    'name': '我的第一个 Odoo 模块',
    'version': '1.0',
    'summary': '这是一个用来向世界问好的专业自定义模块',
    'category': 'Custom',
    'author': '你的名字',
    'depends': ['base'],       # 依赖 Odoo 的核心基础模块
    'data': [
        'views/views.xml',     # 告诉 Odoo 记得去加载你的界面文件
    ],
    'installable': True,
    'application': True,       # 声明这是一个独立的应用，会在列表里大图显示
}