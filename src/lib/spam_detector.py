from src.lib.queries.points_queries import get_user_time_points

banned_words = {
    "boobs": True,
}


def spam_detector(username, message):
    # Determine if user is a 'regular' viewer
    points = get_user_time_points(username)  # int - time_points
    message_to_check = message.split()
    if message.upper() == message:
        if points <= 15:
            if len(message) > 10:
                return True  # True means message is spam
            for word in message_to_check:
                if word in banned_words:
                    return True
