#-*- coding: utf-8-*-
#@Time : 2020/6/15 22:00
#@Author : beibei
#@Email : libei0106@qq.com
#@File : class_lianxi.py
import requests
def http_request(url, data, token=None, method='post'):  # 登录于注册函数
    # 判断get请求还是post请求
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Authorization': token}
    if method == 'get':
        result = requests.get(url, json=data, headers=header)
    else:
        result = requests.post(url, json=data, headers=header)
    return result.json()  # 结束返回结果
    # 调用函数
    # 请求头


# 注册
# reg_url = "http://120.78.128.25:8766/futureloan/member/register"
# reg_data = {'mobile_phone': 18733112222, 'pwd': 12345678}
# http_register_login(reg_url,reg_data)
if __name__ == '__main__':

    # 登录
    log_url = "http://120.78.128.25:8766/futureloan/member/login"
    log_data = {'mobile_phone': 18733112222, 'pwd': 12345678}
    response = http_request(log_url, log_data)  # 登录返回josn结果
    print('登录:{}'.format(response))


    # 充值
    token = response['data']['token_info']['token']
    rec_url = "http://120.78.128.25:8766/futureloan/member/recharge"
    rec_data = {'member_id': 194923, 'amount': 1000}
    if __name__ == '__main__':
        print(http_request(rec_url, rec_data, "Bearer " + token))


