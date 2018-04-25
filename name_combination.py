def main():
    with open('assets/important_words_PRE.txt', 'r', encoding='utf8') as source:
        PRE = [content.strip() for content in source.readlines()[:10]]

    with open('assets/important_words_MIDPRE.txt', 'r', encoding='utf8') as source:
        MIDPRE = [content.strip() for content in source.readlines()[:10]]

    with open('assets/important_words_MIDPOST.txt', 'r', encoding='utf8') as source:
        MIDPOST = [content.strip() for content in source.readlines()[:10]]

    with open('assets/important_words_POST.txt', 'r', encoding='utf8') as source:
        POST = [content.strip() for content in source.readlines()[:10]]

    result = [pre + midpre + midpost + post for pre in PRE for midpre in MIDPRE for midpost in MIDPOST for post in POST]
    print(result)

if __name__ == '__main__':
    main()
