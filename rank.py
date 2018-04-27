from operator import itemgetter

def main():
    with open('assets/cosine_values_only_value.txt', 'r', encoding='utf8') as source:
        contents = [content.strip() for content in source.readlines()]
        contents.sort(reverse=True)
        print(contents[:10])

if __name__ == '__main__':
    main()
