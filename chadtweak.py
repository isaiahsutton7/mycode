#!/usr/bin/env python3


plate = ['broccoli','broccoli','broccoli','bean','bean']

slap = 0

for broccoli in plate:
    if broccoli == "broccoli":
        slap += 1

print(f"I found {slap} broccoli on your plate. That's {slap} slaps!")

for num in range(slap):
   print("SLAP!")
