from GameStats.Games.models import Rating, Comment


def game_rating_generator(game_title):
    all_ratings = Rating.objects.filter(game=game_title)
    try:
        return sum([rating.rating for rating in all_ratings]) / len(all_ratings)
    except ZeroDivisionError:
        return "---"


def next_comment_id_generator():
    new_comment = Comment(comment="Some", game="Something")
    new_comment.save()
    next_id = new_comment.id + 1
    new_comment.delete()
    return next_id
