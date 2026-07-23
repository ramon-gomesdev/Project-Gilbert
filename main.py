from agents.gilbert import GilbertAgent


def main():
    gilbert = GilbertAgent()

    resposta = gilbert.execute(
        "Mostre informações do sistema"
    )

    print(resposta)


if __name__ == "__main__":
    main()
