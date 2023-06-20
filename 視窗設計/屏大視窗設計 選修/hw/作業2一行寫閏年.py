# 題目 一行判斷潤平年
year = input("input number:")
print("閏年" if ((int(year) % 4 == 0 and int(year) %
      100 != 0) or int(year) % 400 == 0) else "平年")
