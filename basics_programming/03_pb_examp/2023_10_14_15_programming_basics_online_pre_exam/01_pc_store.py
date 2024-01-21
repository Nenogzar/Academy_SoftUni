cpu_price = float(input())
gpu_price = float(input())
ram_price = float(input())
ram_number = int(input())
discount = float(input())

usd = 1.57
cpu_price = cpu_price * usd
gpu_price = gpu_price * usd
ram_price = ram_price * usd
total_ram = ram_price * ram_number

gpu_price = gpu_price - gpu_price * discount
cpu_price = cpu_price - cpu_price * discount
total = gpu_price + cpu_price + total_ram

print(f"Money needed - {total:.2f} leva.")
