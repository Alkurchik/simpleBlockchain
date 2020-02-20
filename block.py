import json
import os
import hashlib

blocks_dir = os.curdir + '/doc/'


def get_hash(file_name):
    blocks_dir = os.curdir + '/doc/'
    file = open(blocks_dir + file_name, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(blocks_dir)
    files.remove('.DS_Store')
    return sorted([int(i) for i in files])


def check_integrity():
    files = get_files()
    results = []
    for file in files[1:]:
        f = open(blocks_dir + str(file))
        h = json.load(f)['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'ok'
        else:
            res = "Corrupted"

        # print('Block {} is: {}'.format(prev_file, res))
        results.append({'block': prev_file, 'result': res})

    return results


def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()
    prev_file = files[-1]
    file_name = str(prev_file + 1)
    prev_hash = get_hash(str(prev_file))
    data = {
        "name"   : name,
        "amount" : amount,
        "to_whom": to_whom,
        "hash"   : prev_hash
    }

    with open(blocks_dir + file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    # write_block(name='ivan', amount=2, to_whom='Katya')
    print(check_integrity())


if __name__ == '__main__':
    main()
