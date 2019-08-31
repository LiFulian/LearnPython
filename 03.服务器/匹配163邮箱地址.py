import re
# 匹配.?-等需要加\进行转义

def main():
    while True:
        email = input("请输入您的163邮箱:")
        ret = re.match(r"^[a-zA-Z][a-zA-Z0-9_]{5,17}@163\.com$", email)  # 开头结尾
        if ret:
            print("变量名是：%s 符合要求．．．通过正则匹配到：%s" % (email, ret.group()))
        else:
            print("变量名是：%s 不符合要求．.." % email)


if __name__ == '__main__':
    main()