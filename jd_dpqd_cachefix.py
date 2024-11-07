
"""
1 1 1 1 1 jd_dpqd_cachefix.py
new Env('清空缓存-手动');
"""
#!/usr/bin/env python3
# coding: utf-8

import os

def pullfix():
    print('\n清空缓存，从头再来，会清空所有缓存数据，包括助力数据！！\n')
    print('\n开始执行。。。\n')
    dir_path = os.path.dirname(os.path.abspath(__file__))
    cache=dir_path+'/cache'

    if os.path.isdir(cache):
        os.system('rm -rf '+cache)
    else:
        print('不存在缓存数据，无需清理\n')
        # os.system('find /ql -maxdepth 2 -type d')
        return False
    return True

if pullfix():
    print('清理完成，手动运行一次 jd_dpqd_cache.js 再跑其他脚本！！！！！')