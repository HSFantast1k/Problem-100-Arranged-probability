all_disk = 1_000_000
while True:
    all_disk += 1
    blue_disk = int(all_disk * 0.7)
    while True:
        blue_disk += 1
        if blue_disk * (blue_disk - 1) == (all_disk * (all_disk - 1)) // 2:
            print(f"blue_disk {blue_disk}, all_disk {all_disk}")
        elif blue_disk * (blue_disk - 1) >= (all_disk * (all_disk - 1)) // 2:
            break
    if all_disk % 1000 == 0:
        print(f'all_disk {all_disk}')