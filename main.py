def total_calc(bill_amount,tip_perc):
    #define funtion to caculate the tip on bill_
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print("Please pay $(total)",total)

total_calc(150,20)