from agents.gilbert import GilbertAgent


gilbert = GilbertAgent()


print(gilbert.name)

print(
    gilbert.execute(
        "Explique como funciona Python"
    )
)
