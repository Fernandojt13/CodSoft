import random
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why don't programmers like nature? It has too many bugs.",
        "What do you call cheese that isn't yours? Nacho cheese!"]
    return random.choice(jokes)
def random_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "A group of flamingos is called a 'flamboyance'.",
        "Wombat poop is cube-shaped. This helps it stay in place and mark its territory.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than a year on Venus."]
    return random.choice(facts)
def handle_query(query):
    query = query.lower()
    if "hello" in query or "hi" in query:
        return "How can I assist you today?"
    elif "joke" in query:
        return tell_joke()
    elif "fact" in query:
        return random_fact()
    elif "bye" in query:
        return "Ok, Sir, see you soon!"
    else:
        return "I couldn't understand your query. Can you please rephrase?"
print("Hi, I am Nexus, a ChatBot 😊 who can tell you a joke or fact")
while True:
    print("USER : ", end="")
    query = input()
    response = handle_query(query)
    print("BOT : ", end="")
    print(response)
    
    if "bye" in query:
        break