import re
from bisect import bisect_left

from src.lib import banned_words


def spam_detector(username, message):
    """
    Check is chat message is spammy- Checks for URL, badwords(google list), CAPS and repeated words
    Consider implementing Rank system to allow users of certain rank to post URL for instance.
    :param username: name of user saying the message (not used currently)
    :param message: message from user
    :return: True or False
    """
    if is_badword_spam(message) or is_hyperlink_spam(message) or is_repeatedwords_spam(message) or is_uppercase_spam(message):
        return True


def is_uppercase_spam(message):
    """
    Detect if message is a majority of CAPS (75% currently)
    :param message:
    :return:
    """
    msg_length = len(message)
    uppcase_count = 0
    for pos in range(0, msg_length):
        if message[pos].upper() == message[pos]:
            uppcase_count += 1
    return (((100 - 100 * msg_length - uppcase_count) / msg_length) >= (75))


def is_repeatedwords_spam(message):
    """
    Detect if spam if 4 or more repeated words(4 or more chars) are repeating
    :param message: message from user
    :return:
    """
    words = sorted(message.split())
    duplicate_words = []
    for pos in range(0, len(words) - 1):
        if (words[pos + 1] == words[pos]) and len(words[pos]) > 3:
            duplicate_words.append(words[pos])
    duplicate_words_filterd = filter(bool, duplicate_words)
    return len(duplicate_words_filterd) >= 4


def is_hyperlink_spam(message):
    """
    Using regex to detect URL in message
    :param message: message from user
    :return:
    """
    urls = re.compile(
        ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))').findall(message)
    if urls:
        return True


def is_badword_spam(message):
    """
    Using Googles "official" list of bad words to check for spam
    :param message: message from user
    :return:
    """
    message_to_check = message.split()
    for word in message_to_check:
        if binary_search(banned_words, word):
            return True


def binary_search(lst, item):
    """
    Just a binary search function to speed up list search
    :param lst:
    :param item:
    :return:
    """
    return (item <= lst[-1]) and (lst[bisect_left(lst, item)] == item)
