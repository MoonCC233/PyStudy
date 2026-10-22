# PyStudy in YLNU

Python 练习代码仓库。用于记录日常 Python 语法与功能的小练习示例。

## 环境要求

- Python 3.x（开发环境为 Python 3.14）
- 无第三方依赖，直接运行即可

## 运行方式

```bash
python practice1.py
```

## 练习列表

### practice1.py — 十进制转二进制

读取用户输入的十进制整数，输出其二进制表示。

```bash
$ python practice1.py
请输入一个十进制数字: 42
转换后的二进制是 0b101010
```

实现要点：

- `input()` 获取控制台输入
- `int(num)` 将字符串转换为整数
- `bin()` 返回二进制字符串，Python 会自带 `0b` 前缀

## 目录结构

```
PyStudy/
├── practice1.py    # 十进制转二进制
└── README.md
```
