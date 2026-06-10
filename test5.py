import uuid

def generate_browser_id():
    # 生成标准UUID，去掉横杠，转小写
    uid = str(uuid.uuid4()).replace("-", "").lower()
    return uid

# 调用示例
if __name__ == "__main__":
    bid = generate_browser_id()
    print(bid)