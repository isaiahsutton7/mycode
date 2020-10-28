#!/usr/bin/env python3

#section1: For every [broccoli] I find on your [plate] I'm going to [slap you].
slap= 0
plate = ['broccoli','broccoli','broccoli','bean','bean']

for broccoli in plate:
    if broccoli == 'broccoli':
        slap += 1

print(f"I found {slap} broccoli on your plate. That's {slap} slaps!")

for num in range(slap):
   print("SLAP!")

#section2: For every [toy] I find in the [hallway] I'm going to [throw them away]!
toys= ['truck','ball','rattle','xbox','blocks']
hallway= ['truck','ball','xbox']

print(f"\nFor every toy I find in the hallway I'm going to throw it away!")

for toys in hallway:
    print("I found your " + toys, "I'm taking it away.")

#section3: 

