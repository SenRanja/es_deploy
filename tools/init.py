# encoding=utf-8

import requests as rq
from urllib.parse import urljoin

# GLOBAL
session = None

def create_new_admin(url, port):
    global session
    socket_address = "{URL}:{PORT}".format(URL=url, PORT=port)
    url = urljoin(socket_address, "api/register/")
    print("querying url", url)
    create_admin_data = {
        "password": "admin",
        "name": "管理员",
        "stu_id": "001",
        "tel": "1853624622912",
        "id_card": "14121349904230017",
        "email": "se3nra4nj2a@gmail.com",
        "super": True,
        "role": "admin"
    }
    res = session.post(url, json=create_admin_data)
    print("[HTTP STATUS]", res.status_code)
    print("[HTTP TEXT]", res.text)

def session_login(url):
    global session
    url = urljoin(url, "api/login/")
    session_login_data = {
            "login_name": "001",
            "password": "admin"
        }
    res = session.post(url, json=session_login_data)
    print("[HTTP STATUS]", res.status_code)
    print("[HTTP TEXT]", res.text)

def import_excel_of_modules(socket_address):
    global session

    url = urljoin(socket_address, "/api/import_menu_excel/")
    file = open('modules.xlsx', 'rb')
    files = {'exam_file': file}
    # 以 JSON 格式发送数据，并附加文件
    res = session.post(url, files=files)
    print("[HTTP STATUS]", res.status_code)
    print("[HTTP TEXT]", res.text)
    file.close()

def init_system_setting_parameter(socket_address):
    global session

    url = urljoin(socket_address, "api/system_manage/")
    json_data = {
            "main_title": "五色石考试系统",
            "vice_title": "中国高等教育学生考试系统",
            "login_title": "山西大学计算机学院",
            "cheat_mouse_out": 10,
            "cheat_page_out": 10
        }
    res = session.post(url, json=json_data)
    print("[HTTP STATUS]", res.status_code)
    print("[HTTP TEXT]", res.text)

if __name__ == '__main__':
    # URL(without port)
    url = "http://192.227.167.113"
    # port
    port = 8000
    socket_address = "{URL}:{PORT}".format(URL=url, PORT=port)

    session = rq.Session()
    session.timeout = 50
    session.verify = False

    # create new admin
    print("="*50)
    print("[FUNCTION] create_new_admin")
    create_new_admin(url, port)
    print("="*50)

    # session login
    print("="*50)
    print("[FUNCTION] session login")
    session_login(url)
    print("="*50)

    # import excel of modules
    print("=" * 50)
    print("[FUNCTION] import excel of modules")
    import_excel_of_modules(socket_address)
    print("=" * 50)

    # init system setting parameter
    print("=" * 50)
    print("[FUNCTION] init system setting parameter")
    init_system_setting_parameter(socket_address)
    print("=" * 50)