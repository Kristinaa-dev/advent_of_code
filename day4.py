total = 0
n = 199
arr_cnt = [1]*n
for i in range(0,n):
    card = input()
    card_value = 0
    card = card.split(":")
    # print(card)
    card = card[1].strip()
    card = card.split(" | ")
    # print(card)
    winning = card[0].split(" ")

    all_cards = card[1].split(" ")
    all_cards = [int(x) for x in all_cards if x != ""]
    winning = [int(x) for x in winning if x != ""]
    cnt = 0
    for j in winning:
        if j in all_cards:
            cnt += 1
    print(i,cnt)
    for j in range(i+1,i+cnt+1):
        if j > n:
            arr_cnt.append(arr_cnt[j] + arr_cnt[i])
        else:
            
            arr_cnt[j] = arr_cnt[j] + arr_cnt[i]
    print(arr_cnt)       
print(sum(arr_cnt))