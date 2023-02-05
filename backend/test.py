from flask import Flask, request, redirect, url_for, make_response
import os
from summarize import *
from classification import *
from speech_text import *
from addToNotion import createPage
from text_bulletpoint import bullet

file_name = "Stuart - Hotel Engine - Jan 17 2023.mp4"

transcribed = speech_text(file_name)
summarized = split_article(transcribed)
bulleted = bullet(summarized)
print(bullet)
