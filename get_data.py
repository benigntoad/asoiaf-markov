import praw
import time
from markov_python.cc_markov import MarkovChain

def get_data():
	open('text.txt', 'w').close() # Clear previous text (since this is only called when a new source is generated)

	reddit = praw.Reddit(client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
	                     password='USER_PASSWD', user_agent='USER_AGENT',
	                     username='USER_NAME')

	print(reddit.user.me()) # Just checking we're logged in as the right user

	last_week_unix = int(time.time()) - (86400 * 7) # Getting a UNIX timestamp for the last week

	asoiaf_ids = []
	subreddit = reddit.subreddit('asoiaf')
	for subm_id in subreddit.submissions(last_week_unix):
	    asoiaf_ids.append(subm_id.id) # Append all the IDs for the pulled submissions to a list

	for ids in asoiaf_ids:
		submission = reddit.submission(id=ids) # Set submission
		submission.comments.replace_more(limit=0) # Replace the 'More Comments' with actual comments
		for comment in submission.comments.list():  # Breadth-first traverse of the comments (to grab all replies)
		    doc = open('text.txt', 'a')
		    doc.write(comment.body.encode('utf-8'))
		    doc.close() # Write comments to the text fie

