import openai

openai.api_key = 'api key'  # Replace with your actual API key

def translate_text(text, source_language, target_language):
    if source_language.lower() == "brain rot" and target_language.lower() == "english":
        system_content = (
            "You are a translator between Brain Rot and English. "
            "Brain Rot is English but with word modifications, internet slang, meme references, and absurdist humor. "
            "Here are some examples of Brain Rot terms and phrases:\n\n"
            "- skibidi gyatt rizz\n"
            "- sussy imposter\n"
            "- sigma male grindset\n"
            "- goofy ahh\n"
            "- quirked up white boy busting it down sexual style\n"
            "- amogus\n"
            "- bing chilling\n\n"
            "Your task is to translate between Brain Rot and standard English. "
            "When translating from Brain Rot to English, explain the meaning and context of the terms. "
            "When translating from English to Brain Rot, use appropriate slang and references. "
            "Be prepared to explain internet culture, memes, and current trends as needed."
            "gyatt means butt"
        )
    elif source_language.lower() == "english" and target_language.lower() == "brain rot":
        system_content = (
            "You are a translator between English and Brain Rot. "
            "Brain Rot is English but with word modifications, internet slang, meme references, and absurdist humor. "
            "Here are some examples of Brain Rot terms and phrases:\n\n"
            "- skibidi gyatt rizz\n"
            "- sussy imposter\n"
            "- sigma male grindset\n"
            "- goofy ahh\n"
            "- quirked up white boy busting it down sexual style\n"
            "- amogus\n"
            "- bing chilling\n\n"
            "Your task is to translate between Brain Rot and standard English. "
            "When translating from Brain Rot to English, explain the meaning and context of the terms. "
            "When translating from English to Brain Rot, use appropriate slang and references. "
            "Be prepared to explain internet culture, memes, and current trends as needed."
            "gyatt means butt"
        )
    else:
        system_content = "You are a helpful translator."

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": f"Please translate the following text from {source_language} to {target_language}:\n\n{text}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use 'gpt-4' if you have access
            messages=messages,
            max_tokens=1000,
            temperature=0.5,
        )

        translation = response.choices[0].message.content.strip()
        return translation

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

def get_translation_direction():
    while True:
        print("\nSelect translation direction:")
        print("1. English to Brain Rot")
        print("2. Brain Rot to English")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            return ("English", "Brain Rot")
        elif choice == '2':
            return ("Brain Rot", "English")
        elif choice == '3':
            return (None, None)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    print("Welcome to Lingo Bridge!")
    print("Bridging the Gap between Generations One word at the Time")

    while True:
        source_language, target_language = get_translation_direction()

        if not source_language:
            print("Goodbye!")
            break

        text_to_translate = input(f"\nEnter the text to translate from {source_language} to {target_language}:\n> ").strip()

        if not text_to_translate:
            print("No text entered. Please try again.")
            continue

        translated_text = translate_text(text_to_translate, source_language, target_language)

        if translated_text:
            print(f"\nTranslated text:\n{translated_text}\n")
        else:
            print("Translation failed. Please try again.")

if __name__ == "__main__":
    main()
