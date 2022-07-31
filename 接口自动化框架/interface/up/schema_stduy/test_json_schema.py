
import json

from genson import SchemaBuilder
from jsonschema import validate, ValidationError, SchemaError


def test_genson():
    builder = SchemaBuilder()
    builder.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
    builder.add_object({"a": "1", "b": "bbb", "c": 1})
    json.dump(builder.to_schema(), open("demo_schema.json", "w", encoding="utf-8"))


def schema_validate(obj, schema):
    try:
        validate(instance=obj, schema=schema)
    except ValidationError as e:
        print(f"schema 验证失败 ，出错位置 {e.path},出错信息 {e.message}")
        return False
    except SchemaError as e:
        print(f"schema 验证失败 ，出错位置 {e.path},出错信息 {e.message}")
        return False
    except Exception as e:
        print(e)
        return False
    else:
        print("schema 校验成功")
        return True


def test_schema_valid():
    _schema = json.load(open("demo_schema.json", encoding="utf-8"))
    obj = {"a": 1, "b": "None", "c": 2}
    assert schema_validate(obj, _schema)
    # assert validate(obj,_schema)
