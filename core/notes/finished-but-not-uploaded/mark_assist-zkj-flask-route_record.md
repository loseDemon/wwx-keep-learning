# 记快速帮助zkj解答flask相关使用问题

## 1. 网页搜索

1. [flask app.router - Google 搜索](https://www.google.com.hk/search?q=flask+app.router&newwindow=1&ei=Fi79YYbYM4TXhwPhwJWwAg&ved=0ahUKEwiGu5DEl-b1AhWE62EKHWFgBSYQ4dUDCA4&uact=5&oq=flask+app.router&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBggAEA0QHjIGCAAQDRAeMgYIABANEB46BwgAEEcQsAM6CAgAEAcQChAeOgYIABAHEB46CAgAEAgQBxAeOgoIABAIEAcQChAeSgQIQRgASgQIRhgAUIwFWLcJYLwLaAJwAngAgAFviAGXBJIBAzAuNZgBAKABAcgBCsABAQ&sclient=gws-wiz)
2. [Quickstart — Flask Documentation (2.0.x)](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

![picture 7](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/mark_assist-zkj-flask-route_record-1643984483891-0f7187484cd422c30d6de18e2cb2aea19786dc3e95b84c40a596c4b9ab13c55a.png)  

3. [pallets/flask: The Python micro framework for building web applications.](https://github.com/pallets/flask)

```mermaid
flowchart LR

1 --> 2 --> 3
```

## 2. 文本搜索

```sh
# download the source code
git clone https://github.com/pallets/flask

# locate the src
cd flask
cd src

# first try of searching `route`
grep route -r .

# re-locate the src further
cd flask

# check deeper in the first optional file
vim app.py

# second try of searching `route` more precisely
grep "def route" -r .
```

![picture 8](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/mark_assist-zkj-flask-route_record-1643984501881-353e063db98e0814a2518a78bf7d6f248ac95a121d2d504cdb549923a0188f3d.png)  

```sh
# located the final target code/implementation
vim scaffold.py
```

![picture 9](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/mark_assist-zkj-flask-route_record-1643984527294-dc1519301a720fef8331182e24f6b0a25a330e097586649d85ab79142d8ab537.png)  

## 3. 结论交流

![picture 10](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/mark_assist-zkj-flask-route_record-1643984554572-c9ddd502db33eda584f0ccd0c6f80b72d49022c6a49b3e8fcda40b30462f7257.png)  

![picture 11](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/mark_assist-zkj-flask-route_record-1643984564863-d51a90365cd121eb3ee341f6b2b35a015d05d2a36b455860904686851af9e5b2.png)  

![picture 12](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/mark_assist-zkj-flask-route_record-1643984573740-342a7594c01d3182231c565bccae26505114d2ab78da4e624ae1005f6ccee2c5.png)  
