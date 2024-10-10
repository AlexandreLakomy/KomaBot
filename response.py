def handle_response(message) -> str:
    resp_message = message.lower()

    if resp_message == "hello":
        return "Hi !"

    if resp_message == "comment tu vas ?":
        return "Super bien et toi ?"

    # Retour par défaut si aucun message ne correspond
    return "Je ne comprends pas ce que tu veux dire."

async def send_message(message, user_message, is_private):
    try:
        response = handle_response(user_message)
        
        if response:  # Vérifie que la réponse n'est pas vide
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
        else:
            print("Réponse vide, aucun message envoyé.")
    except Exception as e:
        print(e)
