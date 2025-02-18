class DataManager:
    def __init__(self):
        self.topics = []

    def get_topics(self):
        return self.topics

    def add_topic(self, title, content):
        self.topics.append({'title': title, 'content': content, 'comments': []})

    def add_comment(self, topic_id, comment):
        if 0 <= topic_id < len(self.topics):
            self.topics[topic_id]['comments'].append(comment)