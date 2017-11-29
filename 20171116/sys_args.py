#coding:utf-8
import sys

#练习1，倒叙打印命令行参数
args=sys.argv[1:]  #得到除了脚本名外的所有参数
args.reverse()
print ' '.join(args)

