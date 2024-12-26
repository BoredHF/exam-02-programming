# Handles all the data


def load_words():
    """Load words from dictionary.txt into a list."""
    word_list = []
    try:
        with open('dictionary.txt', 'r') as file:
            for line in file:
                word = line.strip()  # Remove trailing newline
                if word not in word_list:
                    word_list.append(word)
    except FileNotFoundError:
        print("Error: 'dictionary.txt' not found. Make sure the file is in the same directory.")
        exit()
    return word_list

def load_leaderboard():
    """ Loads the leaderboard from winners.txt"""
    users = []
    try:
        with open('winners.txt', 'r') as file:
            for line in file:
                data = line.split(' ')
                users.append([data[0], data[1], data[2]])
    except FileNotFoundError:
        print("File not found. Please make a 'winners.txt' in the same folder.")
    return users

def display_leaderboard(users):
    print('=+ WORDLE LEADERBOARD +=')
    count = 1
    if count >= 5:
        for user in users:
            print('#' + str(count) + ' - ' + user[0] + ' - ' + user[1] + ' in ' + users[2]+ ' tries')
            count += 1     


def save_user(user, time, tries):
    try:
        with open('winners.txt', 'w') as file:
            file.write(user + ' ' + time + ' ' + tries)
            file.write('\n')
    except Exception as e:
        print("Failed to save player. Error: " + e)


