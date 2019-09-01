import re

# 读取一个文件
# 正则匹配url


def main():
    all = list()
    for i in range(1, 11):
        f = open("abcd/" + str(i) + ".js")
        content = f.read()
        urls = re.findall(r"https://[^\"]+", content)
        all += urls

    new_f = open("urls.txt", "w")
    urls = str(urls)
    # new_f.write(urls)
    # new_f.close()
    print(all)


if __name__ == '__main__':
    main()
