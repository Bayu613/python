def power(voltage, currrent):
    circuit_power = voltage * currrent
    print(circuit_power)

voltage = int(input("masukkan nilai voltage = "))
current = int(input("masukkan nilai current = "))

power(voltage, current)