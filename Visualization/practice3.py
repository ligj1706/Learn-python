name = input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？:')

if name == str('需要') :
    m = int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询:'))
    if m == 1 :
        print('去存取款窗口')
    elif m == 3 :
        print('去咨询窗口')
    else:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        N = float(input('请问您需要兑换多少金加隆呢？:'))
        M = float(N * 51.3)
        print('好的，我知道了，您需要兑换' + str(N) + '金加隆。')
        print('那么，您需要付给我' + str(M) + '人民币。')
else:
    print('好的，再见。')