# bitcoin = int(input())
# chn = float(input())
# fee = float(input())
#
# bitcoin_price = 1168
# chn_price = chn * 0.15
# usd_price = 1.76
# euro_price = 1.95
# fee_number = fee / 100
#
# bitcoin_total = bitcoin_price * bitcoin
# chn_price = chn_price * usd_price
# total_eur = (bitcoin_total + chn_price) / euro_price
# fee_total_eur = total_eur * fee_number
# total_result = total_eur - fee_total_eur
#
# print("{:.2f}".format(total_result))

bitcoins_num = int(input())
china_coin_num = float(input())
commission = float(input())
commission_purcent = (1 - commission / 100)

bitcoin = 1168      # lv
china_coin = 0.15   # $
dolar = 1.76        #lv
euro = 1.95         # lv

china_coin_bg = china_coin * dolar  # china to bg

total_bitcoins = bitcoins_num * bitcoin
total_china_coin = china_coin_num * china_coin_bg
change = (total_bitcoins + total_china_coin)/euro
change_whit_commission = change * commission_purcent

print(f"{change_whit_commission:.2f}")
