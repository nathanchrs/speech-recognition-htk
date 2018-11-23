import glob


def read_file_string(path):
    with open(path, encoding='utf8', errors='ignore') as f:
        return f.read()


def write_file(path, array):
    with open(path, 'a') as the_file:
        for i in range(len(array)):
            the_file.write(
                array[i] + " " + array[i].replace("train", "train_mfc").replace("wav", "mfc") + "\n")
        # l.append([array[i], array[i].replace(
        #     "train", "train_mfc").replace("wav", "mfc")])

    # print(l)


def write_train_file(path, array):
    with open(path, 'a') as the_file:
        for i in range(len(array)):
            the_file.write(array[i] + "\n")
        # l.append([array[i], array[i].replace(
        #     "train", "train_mfc").replace("wav", "mfc")])

    # print(l)


if __name__ == '__main__':
    arr = glob.glob("./train/*.wav")
    arr = sorted([int(x.replace("./train/sample", "").replace(".wav", ""))
                  for x in arr])

    train = []
    test = []
    for i in range(0, len(arr), 4):
        for j in range(0, 3):
            train.append("./train_mfc/sample" + str(arr[i+j]) + ".mfc")

        test.append("./train_mfc/sample" + str(arr[i+3]) + ".mfc")

    # print(test)
    # write_file('./codetr.scp', arr)
    write_train_file('./train.scp', train)
    write_train_file('./test.scp', test)

    # content = [x.strip()
    #            for x in read_file_string('./raw_prompts.txt').split('\n')]

    # for i in range(len(content)):
    #     print(i)

    # print(content)
