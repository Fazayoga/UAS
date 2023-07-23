import time

def iteratif_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def rumus_sum(n):
    return n * (n + 1) // 2

n = 1500000
iterasi = 20
batas_waktu = 1/1000000000  # 1 nanosekon = 1/1000000000 detik

print(f"Jumlah iterasi: {iterasi}")
print(f"n = {n}")

for i in range(iterasi):
    start_time = time.time()
    total_iteratif = iteratif_sum(n)
    end_time = time.time()
    waktu_iteratif = end_time - start_time

    start_time = time.time()
    total_rumus = rumus_sum(n)
    end_time = time.time()
    waktu_rumus = end_time - start_time

    print(f"Iterasi-{i+1}:")
    print(f"  Hasil Iteratif: {total_iteratif}, Waktu: {waktu_iteratif} detik")
    print(f"  Hasil Rumus: {total_rumus}, Waktu: {waktu_rumus} detik")
    print()

    if waktu_iteratif > batas_waktu or waktu_rumus > batas_waktu:
        print("Batasi waktu tercapai.")
        break
