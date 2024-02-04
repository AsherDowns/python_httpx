import time
import asyncio
import httpx


async def fetch_httpx():
    urls = [
        "https://www.bitchofrome.com/fandom/transcripts/season1/sinsofthepast.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/chariotsofwar.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/dreamworker.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/cradleofhope.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/thepathnottaken.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/thereckoning.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/thetitans.html"
        "https://www.bitchofrome.com/fandom/transcripts/season1/prometheus.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/deathinchains.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/hoovesandharlots.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/theblackwolf.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/bewaregreeksbearinggifts.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/athenscityacademyoftheperformingbards.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/afistfulofdinars.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/warriorprincess.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/mortalbeloved.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/theroyalcoupleofthieves.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/theprodigal.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/altaredstates.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/tiesthatbind.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/thegreatergood.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/callisto.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/deathmask.html",
        "https://www.bitchofrome.com/fandom/transcripts/season1/isthereadoctorinthehouse.html"
    ]

    async with httpx.AsyncClient() as client:
        req = [client.get(addr) for addr in urls]
        result = await asyncio.gather(*req)


start = time.perf_counter()
asyncio.run(fetch_httpx())
finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
