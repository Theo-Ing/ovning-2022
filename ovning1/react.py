import random
import time
# Invänta slumpmässig tid
wait_time = random.randint(1, 10)
time.sleep(wait_time)

# Presentera texten tryck enter
print("Tryck Enter!!")

# Invänta enter, ta tiden
start = time.time()
input()
end = time.time()

react_time = round(end - start, 3)

# Ange reaktionstid
print("Reaction time (s):", react_time)
