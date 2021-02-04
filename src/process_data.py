import pandas as pd
import re
import os
import glob


def processDataset1():
    dataset_path = '../resources/dataset1.csv'
    new_dataset_path = '../data/dataset1.csv'
    df = pd.read_csv(dataset_path)
    labels = df['label']
    emails = df['text']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            email = re.sub(r'[\t\n]', ' ', emails[i])
            line = ['1' if labels[i] == 'FAKE' else '0', email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset2():
    dataset_path = '../resources/dataset2.csv'
    new_dataset_path = '../data/dataset2.csv'
    df = pd.read_csv(dataset_path)
    labels = df['target']
    emails = df['question_text']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            email = re.sub(r'[\t\n\r]', ' ', emails[i])
            line = [str(labels[i]), email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset3():
    dataset_path = '../resources/dataset3.csv'
    new_dataset_path = '../data/dataset3.csv'
    df = pd.read_csv(dataset_path)
    labels = df['label']
    emails = df['text']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            email = emails[i]
            label = labels[i]
            label = '1' if label == "spam" else '0'
            pos = re.search(r'\n', email).span()[1]
            email = email[pos:]
            email = re.sub(r'[\t\n\r]', ' ', email)
            line = [str(label), email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset4():
    dataset_path = '../resources/dataset4.csv'
    new_dataset_path = '../data/dataset4.csv'
    df = pd.read_csv(dataset_path)
    labels = df['spam']
    emails = df['text']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            email = emails[i]
            label = labels[i]
            label = str(label)
            if email[0] == '"':
                email = email[10:]
            else:
                email = email[9:]
            email = re.sub(r'[\t\n\r]', ' ', email)
            line = [label, email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset5():
    dataset_path = '../resources/dataset5.csv'
    new_dataset_path = '../data/dataset5.csv'
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        with open(dataset_path, mode='r', encoding='utf8') as old:
            new.write('label\temail\n')
            for line in old:
                # print(line)
                line = line.split('\t')
                line[0] = '1' if line[0] == 'spam' else '0'
                line[1] = re.sub(r'[\t\n\r]', ' ', line[1])
                line = '\t'.join(line)
                new.write(line)
                new.write('\n')


def processDataset6():
    dataset_path = '../resources/dataset6.csv'
    new_dataset_path = '../data/dataset6.csv'
    df = pd.read_csv(dataset_path)
    labels = df['label']
    emails = df['email']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            email = emails[i]
            label = labels[i]
            label = str(label)
            email = re.sub(r'[\t\n\r(NUMBER)]', ' ', email)
            email = re.sub(r' +', ' ', email)
            line = [label, email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset7():
    dataset_path = '../resources/dataset7.csv'
    new_dataset_path = '../data/dataset7.csv'
    df = pd.read_csv(dataset_path)
    labels = df['Label']
    emails = df['Body']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            label = labels[i]
            label = str(label)
            email = emails[i]
            email = email[9:]
            email = re.sub(r'[\t\n\r]', ' ', email)
            email = re.sub(r' +', ' ', email)
            line = [label, email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset8():
    dataset_path = '../resources/dataset8.csv'
    new_dataset_path = '../data/dataset8.csv'
    df = pd.read_csv(dataset_path)
    labels = df['Label']
    emails = df['Body']
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        for i in range(len(labels)):
            label = labels[i]
            label = str(label)
            email = emails[i]
            email = email[9:]
            email = re.sub(r'[\t\n\r]', ' ', email)
            email = re.sub(r' +', ' ', email)
            line = [label, email]
            new.write('\t'.join(line))
            new.write('\n')


def processDataset9():
    current_path = os.getcwd()
    spam_folder_path = r'../resources/dataset9/spam/'
    no_spam_folder_path = r'../resources/dataset9/ham/'
    new_dataset_path = r'../data/dataset9.csv'
    with open(new_dataset_path, mode='w', encoding='utf8') as new:
        new.write('label\temail\n')
        os.chdir(spam_folder_path)
        files = os.listdir()
        for file in files:
            with open(file, mode='r', errors='ignore') as f:
                content = f.read()
                content = content[9:]
                content = re.sub(r'[\t\n\r]', ' ', content)
                content = re.sub(r' +', ' ', content)
                line = ['1', content]
                new.write('\t'.join(line))
                new.write('\n')
    os.chdir(current_path)
    with open(new_dataset_path, mode='a', encoding='utf8') as new:
        os.chdir(no_spam_folder_path)
        files = os.listdir()
        for file in files:
            with open(file, mode='r', errors='ignore') as f:
                content = f.read()
                content = content[9:]
                content = re.sub(r'[\t\n\r]', ' ', content)
                content = re.sub(r' +', ' ', content)
                line = ['0', content]
                new.write('\t'.join(line))
                new.write('\n')
    os.chdir(current_path)


def mergeDatasets():
    current_path = os.getcwd()

    os.chdir('../data')
    files = glob.glob('*.csv')
    spam_counter = 0
    ham_counter = 0
    with open("data.csv", mode='w', encoding='utf8') as new:
        for file in files:
            with open(file, mode='r', encoding='utf8') as f:
                for line in f:
                    if line[0] == '1':
                        spam_counter += 1
                    else:
                        ham_counter += 1
                    new.write(line)

    print(spam_counter + ham_counter, spam_counter, ham_counter)
    os.chdir(current_path)


if __name__ == "__main__":
    mergeDatasets()
