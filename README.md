# PyStudy

Python 练习代码仓库。用于记录日常 Python 语法与功能的小练习示例。

## 环境要求

- Python 3.x（开发环境为 Python 3.14）
- 无第三方依赖，直接运行即可

## 运行方式

```bash
python practice1.py
python practice_list.py
```

## 练习列表

### practice1.py — 十进制转二进制

读取用户输入的十进制整数，输出其二进制表示。

```bash
$ python practice1.py
请输入一个十进制数字：42
转换后的二进制是 0b101010
```

实现要点：

- `input()` 获取控制台输入
- `int(num)` 将字符串转换为整数
- `bin()` 返回二进制字符串，Python 会自带 `0b` 前缀

### practice_list.py — 列表操作

演示 Python 列表的创建、增加、删除与切片等常用操作。

```bash
$ python practice_list.py
=== 1. 列表实操 ===
原列表: [3, 5, 7, 9, 11]
字符串转列表: ['h', 'e', 'l', 'l', 'o']
增加元素后: [3, 4, 5, 7, 9, 11, 13, 15, 17]
删除后: [7, 9, 11, 13, 15, 17] | pop 弹出的值: 4
逆序: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
步长为 2: [0, 2, 4, 6, 8]
切片替换后: ['a', 'b', 'c', 3, 4, 5, 6, 7, 8, 9]
```

实现要点：

- `append` / `insert` / `extend` 的原地修改
- `remove` / `pop` / `del` 的删除方式
- 切片的读取、步长与原地替换

## 目录结构

```
PyStudy/
├── practice1.py        # 十进制转二进制
├── practice_list.py    # 列表操作
├── .gitignore
├── LICENSE
└── README.md
```

## 许可证

本项目采用 [MIT License](./LICENSE)。
