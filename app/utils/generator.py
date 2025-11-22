def gerar_resposta(humor):
    if humor >= 8:
        return "Você parece muito bem hoje! Continue aproveitando esse bom momento. 😊"
    elif humor >= 5:
        return "Você está estável, talvez um pouco cansado. Que tal um momento para relaxar? 🌿"
    elif humor >= 3:
        return "Parece que o dia está difícil. Respire fundo, vai passar. 💪"
    else:
        return "Sinto que você não está bem. Lembre-se: pedir ajuda é um sinal de força. ❤️"
