from transformers import pipeline

#call summarizer 
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_article(Article):
  #Maximum sequence length 
  K = 950
  #Total number of tokens in Document
  N = len(Article.strip().split(" "))
  #Let I be the number of sequences of K tokens or less in Document
  I = (N/K)
  return I



#article that we use to summarize
ARTICLE = """ What you're doing right now at this very moment is killing you. 
More than cars or the internet or even that little mobile device we keep talking about, the technology you're using the most almost every day is this, your TUSH. 
Nowadays people are sitting 9.3 hours a day, which is more than we're sleeping at 7.7 hours. Sitting is so incredibly prevalent, we don't even question how much we're doing it, and because everyone else is doing it, it doesn't even occur to us that it's not okay. 
In that way, sitting has become the smoking of our generation. And of course there's health consequences to this, scary ones besides the waste. 
Things like breast cancer and colon cancer are directly tied to our lack of physical inactivity, 10% in fact on both of those, 6% for heart disease, 7% for tied to diabetes, which is what my father died of. Now, any of those stats should convince each of us to get off our death more, but if you're anything like me, it won't. 
What did get me moving was a social interaction. Someone invited me to a meeting, but couldn't manage to fit me into a regular conference room meeting and said, I have to walk my dogs tomorrow, could you come to that? It's kind of odd to do. 
And actually that first meeting, I remember thinking I have to be the one to ask the next question, because I knew I was going to huff and puff during this conversation. 
And yet, I've taken that idea and made it my own. So instead of going to coffee meetings or a fluorescent lit conference room meetings, I asked people to go on a walking meeting to the tune of 20 to 30 miles a week. 
It's changed my life. But before that, what actually happened was I used to think about it as you could take care of your health or you could take care of obligations and one always came at the cost of the other. 
So now several hundred of these walking meetings later, I've learned a few things. First, there's this amazing thing about actually getting out of the box that leads to out of the box thinking. 
Whether it's nature or the exercise itself, it certainly works. And probably the more reflective one is just about how much each of us can hold problems in opposition when they're really not that way. 
And if we're going to solve problems and look at the world really differently, whether it's in governance or business or environmental issues, job creation, maybe we can think about how to reframe those problems as having both things be true. 
Because it was when that happened with this walk-and-talk idea that things became doable and sustainable and viable. 
So I started this talk talking about the tish. So I'll end with the bottom line. Walk-and-talk. Walk the talk. 
You'll be surprised at how fresh air drives fresh thinking. And in the way that you do, you'll bring into your life an entirely new set of ideas. Thank you.
"""
def summarize(Article):
  summary = summarizer(Article, max_length=350, min_length=200, do_sample=False)
  return summary

print(summarize(ARTICLE))