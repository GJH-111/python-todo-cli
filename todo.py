FILE = "todo.txt"


def load():
    items = []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    items.append(line)
    except FileNotFoundError:
        pass
    return items


def save(items):
    with open(FILE, "w", encoding="utf-8") as f:
        for t in items:
            f.write(t + "\n")


def done(items):
    for i, t in enumerate(items, 1):
        print(i, t)
    num = input("完成第几个：")
    if num.isdigit() and 1 <= int(num) <= len(items):
        idx = int(num) - 1
        if not items[idx].startswith("[x]"):
            items[idx] = "[x] " + items[idx]
            save(items)
            print("已标记完成")
        else:
            print("这条已经完成了")
    else:
        print("序号不对")


items = load()

while True:
    print("\n1 添加  2 查看  3 删除  4 标记完成  0 退出")
    choice = input("选择：")

    if choice == "0":
        break
    elif choice == "1":
        text = input("输入待办：").strip()
        if text:
            items.append(text)
            save(items)
            print("已添加")
        else:
            print("内容不能为空")
    elif choice == "2":
        if not items:
            print("还没有待办")
        else:
            for i, t in enumerate(items, 1):
                print(i, t)
    elif choice == "3":
        if not items:
            print("没有可删的")
        else:
            for i, t in enumerate(items, 1):
                print(i, t)
            num = input("输入要删除的序号：")
            if num.isdigit() and 1 <= int(num) <= len(items):
                items.pop(int(num) - 1)
                save(items)
                print("已删除")
            else:
                print("序号不对")
    elif choice == "4":
        if not items:
            print("还没有待办")
        else:
            done(items)
    else:
        print("请输入 0/1/2/3/4")
