
import allure
import pytest

from interface.api_object.apis.department.department import Department


@allure.feature("企业微信部门管理测试")
class TestDepartment:

    def setup_class(self):
        self.department = Department()

    @allure.story("成功创建部门")
    @pytest.mark.parametrize("name", ["深圳研发中心", "深圳研发中心1", "深圳研发中心深圳研发中心深圳研发中心深圳研"])
    def test_create_success(self, name):
        with allure.step("拼接_id"):
            # 获取唯一名称的拼接
            _id = self.department.get_union_id()
        with allure.step("组装数据"):
            # 组装发起新建的数据
            data = {
                "name": f"{name}_{_id}",
                "name_en": f"RDGZ_{_id}",
                "parentid": 1,
            }
        with allure.step("发起新建部门请求"):
            r = self.department.create(data=data)
        with allure.step("断言创建的数据是不是在列表中"):
            assert self.department.is_in_depart_list(r.json().get("id"))

    @allure.story("创建部门失败")
    @pytest.mark.parametrize("name,expect", [("", 40058), ("深圳研发中心深圳研发中心深圳研发中心深圳研心深圳研心深圳研心深圳研", 60001)])
    def test_create_fail(self, name, expect):
        # 获取唯一名称的拼接
        _id = self.department.get_union_id()
        # 组装发起新建的数据
        data = {
            "name": f"{name}_{_id}" if name else "",
            "name_en": f"RDGZ_{_id}",
            "parentid": 1,
        }
        r = self.department.create(data=data)
        assert r.json().get("errcode") == expect
