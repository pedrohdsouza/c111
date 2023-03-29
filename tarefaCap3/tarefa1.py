times = ["Real Madrid", "Barcelona", "São Paulo", "Liverpool", "Milan"]

print("Primeiros 3 colocados:")
for i in range(len(times)):
    if i < 3:
        print(times[i])

print()

print("Ultimos 2 colocados:")
for i in range(len(times)):
    if i >= 3:
        print(times[i])

print()
print("Barcelona está na " + str((times.index("Barcelona") + 1)) + " colocação")

times.sort()
print()
print("Times em ordem alfabética:" + str(times))