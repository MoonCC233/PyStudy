print("=== 1. 列表实操 ===")

# 1. 创建与类型转换
a_list = [3, 5, 7, 9, 11]
print("原列表:", a_list)
print("字符串转列表:", list('hello'))

# 2. 元素的增加 (重点体验原地修改 vs 创建新列表)
a_list.append(13)          # 尾部追加，原地操作
a_list.insert(1, 4)        # 指定位置插入
a_list.extend([15, 17])    # 扩展可迭代对象
print("增加元素后:", a_list)

# 3. 元素的删除
a_list.remove(5)           # 删除首次出现的指定元素
pop_val = a_list.pop(1)    # 删除并返回指定下标(这里删除了4)的元素
del a_list[0]              # 删除下标为 0 的元素
print("删除后:", a_list, "| pop 弹出的值:", pop_val)

# 4. 切片操作 (极其重要)
b_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("逆序:", b_list[::-1])
print("步长为 2:", b_list[::2])
b_list[:3] = ['a', 'b', 'c'] # 切片原地替换
print("切片替换后:", b_list)