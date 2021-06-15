#!~/.asdf/shims/python
import sys

# #指令系統
#
# + scripts/
# +-------- commands/               # 指令集的根目錄
# +----------------- world/          # 指令的 target 模組
# +---------------------- __init__.py # 在 __init__.py 模組檔內定義 action 函式如 hello/0
#
# 在此架構下
if __name__ == '__main__':

    action, target, key, value = [None,None,None,None]
    try:
        action, target, key, value = sys.argv[1:5]
    except ValueError:
        action, target, key = sys.argv[1:4]

    try:
        import commands
        __import__(f'commands.{target}')
    except ModuleNotFoundError as e:
        print(f'oops #1: {type(e)} {str(e)}')
        print(commands.__doc__)
    else:
        try:
            if value:
                eval(f'commands.{target}.{action}({key},{value})')
            elif key:
                eval(f'commands.{target}.{action}({key})')
            else:
                eval(f'commands.{target}.{action}()')
        except (ModuleNotFoundError, AttributeError, TypeError) as e:
            print(f'oops #2: {type(e)} {str(e)}')
            print(commands.__doc__)
