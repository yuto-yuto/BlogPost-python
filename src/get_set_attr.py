from typing import Any


class Product:
    def __init__(self):
        self.count: int = 0
        self.name: str = ""
        self.price: int = 0
        self.remark: str = ""


product_list: list[dict[str, Any]] = [
    {"count": 3, "name": "Item 1", "price": 55},
    {},
    {"count": 56, "name": "Item 2", "remark": "Remark for item 2"},
    {"name": "Item 3", "price": 10, "remark": "No stock"},
]


def run1():
    result: list[Product] = []
    for item in product_list:
        new_item = Product()
        count = item.pop("count", None)
        if count is not None:
            new_item.count = count
        name = item.pop("name", None)
        if name is not None:
            new_item.name = name
        price = item.pop("price", None)
        if price is not None:
            new_item.price = price
        remark = item.pop("remark", None)
        if remark is not None:
            new_item.remark = remark
        result.append(new_item)

    for item in result:
        print(
            f"name: {item.name}, count: {item.count}, price: {item.price}, remark: {item.remark}"
        )


def run2():
    result: list[Product] = []
    for item in product_list:
        new_item = Product()
        for key in ["count", "name", "price", "remark"]:
            value = item.pop(key, None)
            if value is not None:
                setattr(new_item, key, value)
        result.append(new_item)

    for item in result:
        print(
            f"name: {item.name}, count: {item.count}, price: {item.price}, remark: {item.remark}"
        )

def get_set_test():
    item = Product()
    print(item.__getattribute__("count")) # 0
    print(getattr(item, "count")) # 0
    setattr(item, "count", 12)
    print(item.count) # 12
    item.__setattr__("count",66)
    print(item.count) # 66
