
from interface.api_object.apis.wework import WeWork
from interface.api_object.utils.file_tools import FileTool


class Department(WeWork):
    # corpid = "ww75abb8519b57cec6"
    # corpsecret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"

    def __init__(self):
        # 获取 corp_info 的yaml数据
        yaml_data = FileTool.read_yaml("corp_info")
        # 提取 corpid 和 corpsecret
        corpid = yaml_data.get("corp_id").get("yinian")
        corpsecret = yaml_data.get("corpsecret").get("department")
        self.get_access_token(corpid, corpsecret)

    def create(self, data):
        '''
        创建部门
        :return:
        '''
        # 新建部门的url
        create_url = "/department/create"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("POST", create_url, json=data, params=parms)
        # 将返回的响应返回出去
        return r

    def delete(self, depart_id):
        '''
        删除部门
        :return:
        '''
        # 删除部门的url
        delete_url = "/department/delete"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 删除部门param的信息拼接
        parms.update({"id": depart_id})
        # 调用base 封装的 send 发起请求
        r = self.send("GET", delete_url, params=parms)
        # 将返回的响应返回出去
        return r

    def update(self, data):
        '''
        修改部门
        :return:
        '''
        # 更新部门的url
        update_url = "/department/update"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("POST", update_url, json=data, params=parms)
        # 将返回的响应返回出去
        return r

    def search(self):
        '''
        查询部门
        :return:
        '''
        # 发起查询的url
        search_url = "/department/list"
        # 获取 access_token
        parms = {"access_token": self.access_token}
        # 调用base 封装的 send 发起请求
        r = self.send("GET", search_url, params=parms)
        # 将返回的响应返回出去
        return r

    def is_in_depart_list(self, depart_id):
        '''
        是否在部门列表中
        :return:
        '''
        # 调用查询接口
        r = self.search()
        # 拼接jsonpath 用到的 参数
        json_obj = r.json()
        expr = "$..id"
        # 使用封装的jsonpath进行json数据的匹配
        flag = self.my_jsonpath(json_obj, expr)
        # 如果没有匹配到数据就直接返回false
        if flag:
            # 有数据的话，使用depart_id进行列表的数据判断
            if depart_id in flag:
                return True
            else:
                return False
        else:
            return False
