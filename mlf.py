import glob


def read_file_string(path):
    with open(path, encoding='utf8', errors='ignore') as f:
        return f.read()


def write_file_prompts(path):
    # array_slide = ['SATU', 'DUA', 'TIGA', 'EMPAT', 'LIMA',
    #                'ENAM', 'TUJUH', 'DELAPAN', 'SEMBILAN', 'SATU NOL'] * 4

    # array_slide = [[x] * 4 for x in array_slide]

    array_slide2 = ['SLIDE BERIKUTNYA', 'SLIDE SEBELUMNYA',
                    'SLIDE PERTAMA', 'SLIDE TERAKHIR', 'LAYAR PUTIH', 'LAYAR HITAM'] * 4
    array_slide2 = [[x] * 2 for x in array_slide2]

    count = 273

    with open(path, 'a') as the_file:
        # for i in range(len(array_slide)):
        #     for j in range(len(array_slide[i])):
        #         the_file.write(
        #             "sample" + str(count) + " SLIDE KE " +
        #             array_slide[i][j] + "\n")
        #         count = count + 1

        for i in range(len(array_slide2)):
            for j in range(len(array_slide2[i])):
                the_file.write(
                    "sample" + str(count) + " " +
                    array_slide2[i][j] + "\n")
                count = count + 1

        # the_file.write("\n")


def write_codetr_file(path, array):
    with open(path, 'a') as the_file:
        for i in range(len(array)):
            # print(array[i])
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
    # arrCodetr = [("./train/sample" + str(x) + ".wav") for x in arr]

    # print(arrCodetr)

    train = []
    test = []

    count = 36
    for i in range(0, len(arr), 8):
        for j in range(0, 7):
            train.append("./train_mfc/sample" + str(arr[i+j]) + ".mfc")

        test.append("./train_mfc/sample" + str(arr[i+7]) + ".mfc")

    # print(test)
    # write_codetr_file('./codetrain.scp', arrCodetr)
    write_train_file('./train.scp', train)
    write_train_file('./test.scp', test)
    # write_file_prompts('./prompts')

    # content = [x.strip()
    #            for x in read_file_string('./raw_prompts.txt').split('\n')]

    # for i in range(len(content)):
    #     print(i)

    # print(content)
