from core.memory import Memory


memory = Memory("test_memory.json")


memory.save(
    "preferences",
    "Python"
)


memory.save(
    "history",
    "Primeiro teste de memória do Gilbert"
)


print(memory.load())
