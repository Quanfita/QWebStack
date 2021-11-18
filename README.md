# QWebStack

一个Django版本的WebStack导航站点，包含后台管理、数据库，后台使用SimpleUI主题

[WebStack](https://github.com/WebStackPage/WebStackPage.github.io)

## 运行环境

- Python3.6
- Django2.x
- sqlite3/MySQL
- SimpleUI

## 安装运行

> git clone https://github.com/Quanfita/QWebStack.git  
> 
> cd QWebStack  
> 
> pip install -r requirements.txt  
> 
> python manage.py runserver

默认使用sqlite，已有数据，如需要导出到MySQL或者其他数据库，使用以下命令导出

> python manage.py dumpdata > data.json

然后，修改QWebStack/settings.py，将DATABASES修改为MySQL的相关配置，然后使用以下命令

> python manage.py makemigrations
> 
> python manage.py migrate
> 
> python manage.py loaddata data.json

最后运行即可

> python manage.py runserver

## 致谢
感谢 [Viggo](http://viggoz.com/) 的前端设计和数据提供。
