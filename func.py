import requests
import google.generativeai as gemini
from youtube_transcript_api import YouTubeTranscriptApi
from tldextract import extract
from urllib import parse
from marko import convert

def summarize(prompt):
    gemini.configure(api_key='YOUR_API_KEY')
    model = gemini.GenerativeModel("gemini-1.5-flash", "BLOCK_NONE")
    response = model.generate_content(f'Create summarized dot point notes from this transcript, with a clear hierarchy of headings. The structure must be consistent, # for title, ## for each subheading, etc. The title should be descriptive but not overly long. {str(prompt)}').text
    return convert(response)

def YTValidate(url):
    vurl = "https://www.youtube.com/oembed?url=" + url
    result = requests.get(vurl)
    if result.status_code == 200:
        return True
    return False

def getYTTranscript(url):
    tld = extract(url).suffix
    if tld == 'com':
        videoID = parse.parse_qs(parse.urlparse(url).query)['v'][0]
    if tld == 'be':
        videoID = url.split('/')[-1]
    rawCC = YouTubeTranscriptApi.get_transcript(videoID)
    transcript = [m['text'] for m in rawCC]
    return transcript