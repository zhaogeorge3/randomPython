import praw
import re
import time
import numpy as np
import urllib
import cv2
from getpass import getpass

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image
	# return the image
	#return image
	#with open("code2", "wb") as code:
	#	code.write(resp.read())
	#print(resp)

def getSubReddits(subreddit):
	return reddit.subreddit(subreddit).hot(limit=20)

def getPhotos(subredditPosts):
	enumSubmissions = enumerate(subredditPosts)
	photos = {}
	#for i in subredditPosts:
		#print(i.title)
	for count, submission in enumSubmissions:
		if(submission.url.endswith(".jpg")):
			photos[count] = [submission.title, submission.url]
	return photos


def printSubreddit(subredditPosts):
	return getPhotos(subredditPosts)
	#for post in subredditPosts:
		#print(post.title)
		#print(post.url)


def searchSubreddits(searchQuery):
	enumSubmissions = enumerate(reddit.subreddit('all').search(searchQuery, limit=1000))
	for count,submission in enumSubmissions:
		print(submission.title)
		print(submission.url)
		print(count)


print("Welcome to Reddit Cli")
#username = input("please enter your username: ")
#password = getpass()
username = "zhaogeorge3"
password = "CheezyweezY17"
reddit = praw.Reddit(client_id="iKRb6iKw6gvjsA", client_secret="mcePjOj1kbdRFMPNldz4TY10oIE", user_agent="<macOs:georgeTest:1.0 (by /u/zhaogeorge3)>", username=username, password=password)
command = input(">>>")
while command != "quit":
	args = command.lower().split(" ")
	if(args[0] == "view"):
		photos = printSubreddit(getSubReddits(args[1]))
		for key, value in photos.items():
			print(key, ". ", value)
		photo = input("which photo to view: ")
		while int(photo) in photos.keys():
			image = url_to_image(photos[int(photo)][1])
			cv2.imshow("Image", image)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			cv2.waitKey(1)
			photo = input("which photo to view: ")
	elif(args[0] == "search"):
		searchSubreddits(" ".join(args[1:]))
	else:
		count = 0
		r = reddit.subreddit("nsfw").hot(limit=20)
		for i in range(20):
			print(next(r).title)
			count+=1
			print(count)
	command = input(">>>")

	#print ("downloading %s", (submission.url))
	#image = url_to_image(submission.url)
	#cv2.imshow("Image", image)
	#cv2.waitKey(0)
