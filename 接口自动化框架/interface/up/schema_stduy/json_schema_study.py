

from genson import SchemaBuilder

builder = SchemaBuilder()
builder.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
builder.add_object({"a": "1", "b": "bbb", "c": 1})
print(builder.to_schema())
print(builder.to_json(indent=2))