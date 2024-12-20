def meme_quiz():
    print("Welcome to the Meme Quiz!")
    print("Answer the questions below to find out which meme you are!\n")

    questions = [
        {
            "question": "What is your go-to weekend activity?",
            "options": ["a) Scrolling through social media", "b) Hanging out with friends", "c) Watching Netflix", "d) Sleeping"],
            "scores": ["relatable", "wholesome", "distracted", "lazy"]
        },
        {
            "question": "Choose your favorite snack:",
            "options": ["a) Chips", "b) Pizza", "c) Ice cream", "d) Salad"],
            "scores": ["chaotic", "funny", "sweet", "unexpected"]
        },
        {
            "question": "What's your spirit animal?",
            "options": ["a) Cat", "b) Dog", "c) Frog", "d) Sloth"],
            "scores": ["sassy", "loyal", "random", "lazy"]
        },
        {
            "question": "Pick a color:",
            "options": ["a) Red", "b) Blue", "c) Green", "d) Yellow"],
            "scores": ["bold", "calm", "quirky", "happy"]
        },
    ]

    score_counts = {
        "relatable": 0,
        "wholesome": 0,
        "distracted": 0,
        "lazy": 0,
        "chaotic": 0,
        "funny": 0,
        "sweet": 0,
        "unexpected": 0,
        "sassy": 0,
        "loyal": 0,
        "random": 0,
        "bold": 0,
        "calm": 0,
        "quirky": 0,
        "happy": 0,
    }

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your choice (a/b/c/d): ").lower()
        while answer not in ['a', 'b', 'c', 'd']:
            print("Please choose a valid option: a, b, c, or d.")
            answer = input("Your choice (a/b/c/d): ").lower()

        index = ['a', 'b', 'c', 'd'].index(answer)
        selected_score = q["scores"][index]
        score_counts[selected_score] += 1

    result = max(score_counts, key=score_counts.get)

    memes = {
        "relatable": "You are the 'Relatable Content' meme! Always hitting close to home.",
        "wholesome": "You are the 'Wholesome Doggo' meme! Pure and uplifting.",
        "distracted": "You are the 'Distracted Boyfriend' meme! Easily caught off guard.",
        "lazy": "You are the 'Lazy Sloth' meme! Nap enthusiast.",
        "chaotic": "You are the 'This is Fine' meme! Embracing chaos.",
        "funny": "You are the 'Surprised Pikachu' meme! Always delivering unexpected laughs.",
        "sweet": "You are the 'Baby Yoda' meme! Adorable and heartwarming.",
        "unexpected": "You are the 'Galaxy Brain' meme! Surprising in the best ways.",
        "sassy": "You are the 'Grumpy Cat' meme! Sarcasm is your love language.",
        "loyal": "You are the 'Doge' meme! Much wow, very loyal.",
        "random": "You are the 'Pepe the Frog' meme! A wildcard of emotions.",
        "bold": "You are the 'Woman Yelling at a Cat' meme! Unapologetically loud.",
        "calm": "You are the 'Chill Drake' meme! Taking life easy.",
        "quirky": "You are the 'Mocking Spongebob' meme! Always a little eccentric.",
        "happy": "You are the 'Blurry Mr. Krabs' meme! Optimistic and energetic."
    }

    print("\nQuiz Complete! Calculating results...")
    print(memes[result])

if __name__ == "__main__":
    meme_quiz()