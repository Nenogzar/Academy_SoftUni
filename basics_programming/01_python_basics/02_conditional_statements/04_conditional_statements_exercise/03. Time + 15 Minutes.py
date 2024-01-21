h = int(input())
m = int(input())
after = 15

hm = h *60

all_times = hm + m + after
hh = all_times // 60
mm = all_times % 60

if hh == 24 and mm < 10:
    print((f"0:0{mm}"))
elif mm < 10 :
    print(f"{hh}:0{mm}")
elif hh >= 24:
    print((f"0:{mm}"))
else:
    print(f"{hh}:{mm}")

