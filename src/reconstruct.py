import sys

# Reconstruct social links to privacy-friendly front-ends
def reconstruct(url: str) -> str:

    # If url is not a non-empty str
    if url:
        instagram = "instagram"
        twitter = "twitter"
        youtube = "youtube"
        com = ".com/"

        # If com in url
        if com in url:
            platform = url.split(com)[0]
            platform_lower = platform.lower()
            subdirectory = url.split(com)[1]
            key = url.split(platform + com)[1]

            # Instagram -> Bibliogram
            # If instagram in platform_lower and "p/" in subdirectory then url is treated as Instagram profile...
            if instagram in platform_lower and "p/" in subdirectory:
                return "https://bibliogram.art/" + key

            # ...Else if instagram in platform_lower then url is treated as Instagram post
            elif instagram in platform_lower:
                return "https://bibliogram.art/u/" + key

            # Twitter -> Nitter
            # Else if twitter in platform_lower then url is treated as Twitter profile or tweet
            elif twitter in platform_lower:
                return "https://nitter.net/" + key

            # YouTube -> Invidious
            # Else if youtube in platform_lower then url is treated as YouTube channel or video
            elif youtube in platform_lower:
                return "https://invidious.site/" + key

            # Else return empty str
            else:
                return ""

        # Else com is not in url
        else:
            return ""

    # Else url is a non-empty str then return empty str
    else:
        return ""

# Driver
for url in sys.argv:
    print(reconstruct(url))