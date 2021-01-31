seq_numbers=""
for number in range(2000,3200):
    if number%7 == 0 and number%5 !=0:
        seq_numbers+=str(number)+","
print(seq_numbers.rstrip(","))



