# In[1]:
# from jmespath import search
#
# In[2]: data = {
#     ...: "alpha": {
#     ...: "one": "jia",
# ...: "two": "bai"
# ...:},
# ...: "beta": {
#     ...: "one": "ping",
# ...: "two": "pang"
# ...:},
# ...: "Gamma": {"two": "Gado"}
# ...:}
#
# In[3]: search('alpha.*', data)
# Out[3]: ['jia', 'bai']
#
# In[4]: search('*.two', data)
# Out[4]: ['bai', 'pang', 'Gado']

from jmespath import search
json1 = {"name":"gss",
         "data":"study"}

search("name",json1)

if __name__ == '__main__':
    print(search("name",json1))

import jmespath

data = {
    "name": "张三",
    "age": 26,
    "gender": "男",
    "grade": {
        "Chinese": 96,
        "Math": 99
    },
    "records": [
        {
            "Chinese": 95,
            "Math": 100
        },
        {
            "Chinese": 98,
            "Math": 98
        }
    ]
}

# 获取键值对值
search_cond = '{NAME:name, AGE:age, RECORDS:records}'
res = jmespath.search(search_cond, data)
print(res)

# 获取对象值
search_name = 'name'
res_name = jmespath.search(search_name, data)
print(res_name)

search_records = 'records'
res_records = jmespath.search(search_records, data)
print(res_records)

# 使用子表达式获取值，若值不存在返回null
search_sub_value = 'grade.Chinese'
res_sub_value = jmespath.search(search_sub_value, data)
print(res_sub_value)

search_sub_value1 = 'records[0].Chinese'
res_sub_value1 = jmespath.search(search_sub_value1, data)
print(res_sub_value1)

search_sub_value2 = 'records[2].Chinese'
res_sub_value2 = jmespath.search(search_sub_value2, data)
print(res_sub_value2)

# 列表取值,索引从0开始，若是
search_list1 = 'records[1].Chinese'
res_list1 = jmespath.search(search_list1, data)
print(res_list1)

search_list2 = 'records[2].Chinese'
res_list2 = jmespath.search(search_list2, data)
print(res_list2)

search_list3 = 'records[-1].Chinese'
res_list3 = jmespath.search(search_list3, data)
print(res_list3)