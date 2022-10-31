from unicodedata import name

ok = 0
ng = 0


print("〜ワクワクサン〜")

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

name = int(input('1働き蜂の性別は？1～3のうちどれか一つ選んで入力してください?1,メス 2,オス 3,両方'))

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

if name == 1:
    print(name,"正解です")
    ok = ok + 1
elif name == 2:
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は1のメスです!")
    ng = ng + 1
else: 
    print(name,"正解は1のメスです!")
    ng = ng + 1

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

name = int(input('2お酢に卵を殻ごと入れると卵はどうなるでしょうか？1,透明な卵になる 2,硬い石のような卵になる 3,卵が溶けてなくなる'))

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

if name == 1:
    print(name,"正解です")
    ok = ok + 1
elif name == 2:
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は1の透明な卵になるです!")
    ng = ng + 1
else: 
    print(name,"正解は1の透明な卵になるです!")
    ng = ng + 1

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

name = int(input('3シロクマ（ホッキョクグマ）の肌の色は何色？1,白色 2,肌色 3,黒色'))

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

if name == 1:
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は3の黒色です")
    ng = ng + 1
elif name == 2:
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は3の黒色です!")
    ng = ng + 1
else: 
    print(name,"正解です!")
    ok = ok + 1

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

name = int(input('4アニメの作品数は？1, 175,655  2, 14,710  3, 61,172'))

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

if name == 1:
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は2の14,710です")
    ng = ng + 1
elif name == 2:
    print(name,"正解です!")
    ok = ok + 1
else: 
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は2の14,710です!")
    ng = ng + 1

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

name = int(input('5 次の式の答えはなに？1, 31.4159  2, 50  3, 34.2711'))

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

if name == 1:
    print(name,"正解です!")
    ok = ok + 1
elif name == 2:
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は1の31.4159です!")
    ng = ng + 1
else: 
    print(name,"惜しい!!なんで間違えたか明日までに考えといてください!正解は1の31.4159です!")
    ng = ng + 1

if name == 2:
      print("|")
      print("|")
      print("↓")
      print('T')
elif name :
      print("|")
      print("|")
      print("↓")
      print('F')

print("終了！ーーーーーー　あなたの正解数は", ok, "正答率は、",ok/(ok+ng)*100, "%です")

