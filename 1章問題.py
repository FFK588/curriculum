

#問題① 問1-1
print("/////////////////////////")
print("問題① 問1-1")
for i in["1","3","5","7"]:
    print((int(i))*(int(i)))

#問題① 問1-2
print("/////////////////////////")
print("問題① 問1-2")
for j in range(1,8,2):
    print(j*j)

#問題② 問2-1
print("/////////////////////////")
print("問題② 問2-1")
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place:
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

#問題② 問2-2
print("/////////////////////////")
print("問題② 問2-2")
tousen = get_place + wait_place
tousen_keka = ('{0}と{1}と{2}のチケットが当選しました！')
print(tousen_keka.format(tousen[0],tousen[1],tousen[2]))

print("/////////////////////////")
