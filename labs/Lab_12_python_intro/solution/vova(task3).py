def text_histogram(input_text):
    count_ch = {}
    for char in input_text:
        if char not in (' ', '\n'):
            count_ch[char] = count_ch.get(char, 0) + 1

    max_count = max(count_ch.values())
    histogram = []

    for i in range(max_count, 0, -1):
        row = ''.join('#' if count_ch[char] >= i else ' ' for char in sorted(count_ch.keys()))
        histogram.append(row)

    histogram.append(''.join(sorted(count_ch.keys())))
    return '\n'.join(histogram)


def process_file(file_name):
    with open(file_name, 'r') as file:
        input_text = file.read()
        print(text_histogram(input_text))


if __name__ == '__main__':
    files = ['2.txt', '1.txt']
    for file_name in files:
        process_file(file_name)
