a = [3, 1, 221, 33, 1]


def chain(alist):
    link_list = [None for i in range(len(alist))]
    per = 0
    chains_list = []
    flag = 0
    for i in range(len(alist)):
        per = alist[i] % len(alist)
        if link_list[per] != None:
            flag = 1
        else: flag = 0
        if flag == 0:
            chains_list.append([alist[i],None])
            link_list[per] = len(chains_list)-1
        else:
            chains_list.append([alist[i], None])
            temp = link_list[per]
            while chains_list[temp][1] is not None:
                temp = chains_list[temp][1]
            chains_list[link_list[per]][1] = len(chains_list)-1
    print(link_list)
    print(chains_list)

chain(a)