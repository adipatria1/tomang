import json
from datetime import datetime

class CommentProcessor:
    def __init__(self, username):
        self.username = username
        self.processed_file = f'processed_comments_{username}.json'
        self.processed_comments = self.load_processed_comments()

    def load_processed_comments(self):
        try:
            with open(self.processed_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_processed_comments(self):
        with open(self.processed_file, 'w') as f:
            json.dump(self.processed_comments, f)

    def is_processed(self, comment_pk):
        return str(comment_pk) in self.processed_comments

    def mark_processed(self, comment_pk, post_id):
        self.processed_comments[str(comment_pk)] = {
            'processed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'post_id': post_id
        }
        self.save_processed_comments()