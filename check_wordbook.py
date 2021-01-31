with open('vocabulary.txt', 'r', encoding="utf-8") as f:
    for line in f:
        vocab = line.split(": ")
        meaning = input(f'{vocab[1].strip()}: ')
        if meaning == vocab[0]:
            print("맞았습니다!")
        else:
            print(f'아쉽습니다. 정답은 {vocab[0]}입니다.')