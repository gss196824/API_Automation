import requests
from anaconda_project.internal.conda_api import result

r = requests.get("https://atrenew.feishu.cn/wiki/UDXTw0IH6iVbUlk2Pp8c6R9onkg")

print(r.headers)
print(r.headers['Content-Type'])

import jmespath


data = {
    "foo": {
        "bar": "baz",
        "numbers": [1, 2, 3],
        "objects": [
            {"name": "one", "value": 1},
            {"name": "two", "value": 2}
        ]
    }
}
result = jmespath.search("foo.bar",data)
result2 = jmespath.search("foo.numbers[*]",data)
result3 = jmespath.search("foo.objects[1] | values(@)",data)

print(result3)