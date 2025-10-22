import wikipedia

def get_wikipedia_info(query):
    """Fetch information from Wikipedia."""
    try:
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia:")
        print(results)
    except Exception as e:
        print("Sorry, I couldn't find information on that topic.")
        print(e)

def main():
    """Main function to handle commands."""
    print("Hello! How can I assist you today?")
    while True:
        query = input("You: ").lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            get_wikipedia_info(query.strip())
        elif 'exit' in query or 'stop' in query:
            print("Goodbye!")
            break
        else:
            print("I can search Wikipedia for you. Please tell me what you would like to know.")

if __name__ == "__main__":
    main()
