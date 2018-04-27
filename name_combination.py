def main():
    with open('areport-third-test/assets/important_words/important_words_pos_1.txt', 'r', encoding='utf8') as source:
        PRE = [content.strip() for content in source.readlines()[:10]]

    with open('areport-third-test/assets/important_words/important_words_pos_2.txt', 'r', encoding='utf8') as source:
        MIDPRE = [content.strip() for content in source.readlines()[:10]]

    with open('areport-third-test/assets/important_words/important_words_pos_3.txt', 'r', encoding='utf8') as source:
        MIDPOST = [content.strip() for content in source.readlines()[:10]]

    with open('areport-third-test/assets/important_words/important_words_pos_4.txt', 'r', encoding='utf8') as source:
        POST = [content.strip() for content in source.readlines()[:10]]

    result = [pre + midpre + midpost + post for pre in PRE for midpre in MIDPRE for midpost in MIDPOST for post in POST]
    with open('areport-third-test/result.txt', 'w', encoding='utf8') as outp:
        outp.write('\n'.join(result))
    

if __name__ == '__main__':
    main()
