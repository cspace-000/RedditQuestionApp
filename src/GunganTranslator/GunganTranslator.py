import praw
import keys
import json
from translator import translate


reddit = praw.Reddit(
    client_id=keys.client_id,
    client_secret=keys.client_secret,
    password=keys.password,
    user_agent=keys.user_agent,
    username=keys.username,
)

subreddit = reddit.subreddit('all')    
    

def read_comment(comment):
    if hasattr(comment, 'body') and hasattr(comment.author, 'name'):
        if '!binkabot' in comment.body:
            if comment.parent():
                parent = comment.parent()  
                parent.refresh()
                if type(parent) == praw.models.Comment:
                    reply = translate(parent.body)
                    comment.reply(reply)
                    
                    
                    print('replying to comment {}'.format(comment.id))
                
            # except Exception as e:
                # print(e)
                
                
def main():
    print("running binka_bot")
    for comment in subreddit.stream.comments(skip_existing=True):
        read_comment(comment)

    



if __name__ == "__main__":
    main()