elapsed = 7835

hours = elapsed // (60 ** 2)
minutes = (elapsed - (hours * (60 ** 2))) // 60
seconds = (elapsed - (hours * (60 ** 2))) % 60

print(hours, minutes, seconds)

