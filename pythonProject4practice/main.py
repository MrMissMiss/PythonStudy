# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import jionlp


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def sp_address(addr):
    # 分解地址为json字符串
    return jionlp.parse_location(addr,town_village=True)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    raw_addr = "浙江省温州市苍南县灵溪镇灵堡村灵堡小区"
    sp_addr = sp_address(raw_addr)
    print(sp_addr)
    raw_addr = "上海市松江区方松街道檀香花苑社区居委会"
    sp_addr = sp_address(raw_addr)
    print(sp_addr)
    raw_addr = "北京海淀万寿路街道翠微路社区居委会"
    sp_addr = sp_address(raw_addr)
    print(sp_addr)


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
