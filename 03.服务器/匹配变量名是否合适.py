import re


def main():
    names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "age#1", "___"]
    for name in names:
        # ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name)
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)  # 开头结尾
        if ret:
            print("变量名是：%s 符合要求．．．通过正则匹配到：%s" % (name, ret.group()))
        else:
            print("变量名是：%s 不符合要求．.." % name)


if __name__ == '__main__':
    main()