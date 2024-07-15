def create_youtube_video (title, description)
	likes = 0
	dislikes = 0
	count = 0
	new_youtube_video = {"title":title, "description":description, "likes":likes, "dislikes":dislikes, "comments":{"username":"","comment_text":""}}
	return  new_youtube_video
def like(youtube video)
	if "likes" in new_youtube_video:
		count += 1
	return new_youtube_video
def dislike(youtube video)
	if "dislikes" in new_youtube_video:
		count += 1
	return new_youtube_video
def add_comment(youtubevideo, username, comment_text)
	youtubevideo["comments"]["username"]= username
	youtubevideo["comments"]["comment_text"] = comment_text

vid = create_youtube_video("A title", "A description")
add_comment(vid,"hello", "How are you?")
