import random

person = ["Ethan", "Massimo", "Nicolas", "Eric", "Ryan", "Jordan"]
friends = ["Allen", "Micheal", "Joseph", "Adriano", "Alec", "Anthony"]
emotions = ["is kind to", "is inspired by", "trusts", "is forgiving to", "is happy with", "optimistic with"]


for p in person:
    print person[random.randint(0,5)], emotions[random.randint(0,5)], friends[random.randint(0,5)]