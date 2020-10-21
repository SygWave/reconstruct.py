# reconstruct.py 🐍

Reconstruct social links to privacy-friendly front-ends via command line

## About

### Instagram -> [Bibliogram](https://github.com/cloudrac3r/bibliogram)

* Run script with full direct link to Instagram profile or post

### Twitter -> [Nitter](https://github.com/zedeus/nitter)

* Run script with full direct link to Twitter profile or tweet

### YouTube -> [Invidious](https://github.com/iv-org/invidious)

* Run script with full direct link to YouTube channel or video

## Usage

* `./python.exe ./reconstruct.py full-direct-link-here`

* Example 1: `python reconstruct.py https://www.instagram.com/instagram/?hl=en`

  * Output: `https://bibliogram.art/u/instagram/?hl=en`

* Example 2: `python reconstruct.py https://www.instagram.com/p/CGIxEaWD69G/ https://twitter.com/twitter`

  * Output:

        https://bibliogram.art/p/CGIxEaWD69G/
        https://nitter.net/twitter

## Testing

* To test for bugs, try converting links:

  * With random capitalization in the platform name, and/or...
  
  * ...with(out) a forward slash at the end, and/or...
  
  * ...with URL query parameters at the end, and/or...
  
  * ...with tracking information at the end
  
* If you come across a bug, please create an issue and/or submit a pull request!

### Instagram Test Links

    https://www.instagram.com/instagram/?hl=en -> https://bibliogram.art/u/instagram/?hl=en

    https://www.instagram.com/p/CGIxEaWD69G/ -> https://bibliogram.art/p/CGIxEaWD69G/
    
### Twitter Test Links

    https://twitter.com/twitter -> https://nitter.net/twitter

    https://twitter.com/Twitter/status/1308132903830925313 -> https://nitter.net/Twitter/status/1308132903830925313
    
### YouTube Test Links

    https://www.youtube.com/user/YouTube -> https://invidious.site/channel/YouTube

    https://www.youtube.com/watch?v=IPLaajIJq8M -> https://invidious.site/watch?v=IPLaajIJq8M

## Owner

SygWave
