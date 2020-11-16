ans_list = []
f = open('A', 'r')
datalist = f.readlines()
it = iter(datalist)
# print(datalist)
for index, s in enumerate(datalist):
    _list = []
    if (index+1)%2!=0:
      num = int(s)
    else:
      s =s.rstrip("\n")
      for i in s:
        try:
          _list.append(int(i))
        except:
          e = 0
    if len(_list)!=0:
      if num != 0:
        box = ([0]*4)
        count = 0
        for l in range(len(_list)-3):
          box[0] = _list[l]
          box[1] = _list[l+1]
          box[2] = _list[l+2]
          box[3] = _list[l+3]
          if box[0]==2 and box[1]==0 and box[2]==2 and box[3]==0:
            count += 1
        ans_list.append(count)
        # print(ans_list)
for answer in ans_list:
    print(answer)