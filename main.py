from agents.gilbert import GilbertAgent


def main():
    gilbert = GilbertAgent()

    resposta = gilbert.execute(
        "Explique como funciona o Project Gilbert"
    )

    print(resposta)


if __name__ == "__main__":
    main()
