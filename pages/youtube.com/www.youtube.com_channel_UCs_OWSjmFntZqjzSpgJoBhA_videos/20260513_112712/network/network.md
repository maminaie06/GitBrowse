# Network Log

این فایل خلاصه‌ی درخواست‌ها و پاسخ‌های ثبت‌شده توسط مرورگر است. جزئیات کامل در `network.json` و `network.jsonl` ذخیره شده است.

| # | Method | Type | Status | URL | Body |
|---:|---|---|---:|---|---|
| 1 | `GET` | `document` | 200 | `https://www.youtube.com/channel/UCs_OWSjmFntZqjzSpgJoBhA/videos` | network/bodies/0001_document.html |
| 2 | `GET` | `other` | 204 | `https://i.ytimg.com/generate_204` | binary body skipped |
| 3 | `GET` | `script` | 200 | `https://www.youtube.com/s/_/ytmainappweb/_/js/k=ytmainappweb.kevlar_base.en_US.81_ruFHWKHQ.es5.O/am=AAAAIAAABAAJ/d=1/br=1/rs=AGKMywGQVwYW8zbS-3eaCe2_3aWpziYX...` | network/bodies/0003_script.js |
| 4 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/web-animations-next-lite.min.vflset/web-animations-next-lite.min.js` | network/bodies/0004_script.js |
| 5 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/custom-elements-es5-adapter.vflset/custom-elements-es5-adapter.js` | network/bodies/0005_script.js |
| 6 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/webcomponents-sd.vflset/webcomponents-sd.js` | network/bodies/0006_script.js |
| 7 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/intersection-observer.min.vflset/intersection-observer.min.js` | network/bodies/0007_script.js |
| 8 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/scheduler.vflset/scheduler.js` | network/bodies/0008_script.js |
| 9 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/www-i18n-constants-en_US.vflset/www-i18n-constants.js` | network/bodies/0009_script.js |
| 10 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/spf.vflset/spf.js` | network/bodies/0010_script.js |
| 11 | `GET` | `script` | 200 | `https://www.youtube.com/s/desktop/47009d78/jsbin/network.vflset/network.js` | network/bodies/0011_script.js |
| 12 | `GET` | `stylesheet` | 200 | `https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=YouTube+Sans:wght@300..900&display=swap` | network/bodies/0012_stylesheet.css |
| 13 | `GET` | `stylesheet` | 200 | `https://www.youtube.com/s/desktop/47009d78/cssbin/www-onepick.css` | network/bodies/0013_stylesheet.css |
| 14 | `GET` | `stylesheet` | 200 | `https://www.youtube.com/s/_/ytmainappweb/_/ss/k=ytmainappweb.kevlar_base.CX8T9E_hg04.L.B1.O/am=AAAAIAAgBIAJ/d=0/br=1/rs=AGKMywGYrf3B6r7W1ClDEV1-Ic6HqQBM1A` | network/bodies/0014_stylesheet.css |
| 15 | `GET` | `font` | 200 | `https://fonts.gstatic.com/s/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2` | binary body skipped |
| 16 | `GET` | `document` | 302 | `https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%2...` | body unavailable: Response.body: Response body is unavailable for redirect responses |
| 17 | `GET` | `stylesheet` | 200 | `https://www.youtube.com/s/desktop/47009d78/cssbin/www-main-desktop-watch-page-skeleton.css` | network/bodies/0017_stylesheet.css |
| 18 | `GET` | `document` | 302 | `https://accounts.google.com/InteractiveLogin?continue=https://www.youtube.com/signin?action_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252Fsign...` | body unavailable: Response.body: Response body is unavailable for redirect responses |
| 19 | `GET` | `document` | 403 | `https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26ne...` | network/bodies/0019_document.html |
| 20 | `GET` | `xhr` | 302 | `https://googleads.g.doubleclick.net/pagead/id` | body unavailable: Response.body: Response body is unavailable for redirect responses |
| 21 | `GET` | `media` | 206 | `https://www.youtube.com/s/search/audio/failure.mp3` | binary body skipped |
| 22 | `GET` | `media` | 206 | `https://www.youtube.com/s/search/audio/no_input.mp3` | binary body skipped |
| 23 | `GET` | `media` | 206 | `https://www.youtube.com/s/search/audio/open.mp3` | binary body skipped |
| 24 | `GET` | `media` | 206 | `https://www.youtube.com/s/search/audio/success.mp3` | binary body skipped |
| 25 | `GET` | `xhr` | 200 | `https://googleads.g.doubleclick.net/pagead/id?slf_rd=1` | network/bodies/0025_xhr.json |
| 26 | `GET` | `script` | 200 | `https://www.google.com/js/th/GKHPdbjXdAzLptBtk5NastbDkUFAkaEKXg3Jazyf5I0.js` | network/bodies/0026_script.js |
| 27 | `GET` | `image` | 200 | `https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png` | binary body skipped |
| 28 | `GET` | `stylesheet` | 200 | `https://fonts.googleapis.com/css?family=Roboto:300italic,400italic,500italic,700italic` | network/bodies/0028_stylesheet.css |
| 29 | `GET` | `stylesheet` | 200 | `https://fonts.googleapis.com/css?family=Roboto+Mono:400` | network/bodies/0029_stylesheet.css |
| 30 | `POST` | `fetch` | 200 | `https://www.youtube.com/youtubei/v1/guide?prettyPrint=false` | network/bodies/0030_fetch.json |
| 31 | `GET` | `image` | 200 | `https://www.google.com/pagead/lvz?evtid=ACd6KtxJH95xy-dQxLhdZdgxW9fQanmwJNRq0KnQ4mRtmykrfqPungtMCLxi1RWS8HG5YrK8cznNIAAuhwtjG4lZx9dDfcLctQ&req_ts=1778671634&...` | binary body skipped |
| 32 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/BA0LZx2JYRM/hqdefault.jpg?sqp=-oaymwFBCNACELwBSFryq4qpAzMIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB8AEB-AH-CIAC0AWKAgwIABABGFIgZShQMA8=&rs=AOn4...` | binary body skipped |
| 33 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/xpXd5wiPdh0/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDJTO1hNW9KPHaCOnjMTLlQA4BgOg` | binary body skipped |
| 34 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/KVtg9JglYh8/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB1HnyOMADyMg1kx-tnJ1qDGfsO0Q` | binary body skipped |
| 35 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/7GSp-ZIMqxc/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBLhmapVzPq1IqI2oQJdzEOQeasyQ` | binary body skipped |
| 36 | `GET` | `image` | 200 | `https://yt3.googleusercontent.com/Cn8htB0qIagumFtyJXJnvpF68HYRDCTnwJFSQkQcIiGeL3yxRQieqJ1kAr4UQ95QBAPFAreV=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-...` | binary body skipped |
| 37 | `GET` | `image` | 200 | `https://yt3.googleusercontent.com/ytc/AIdro_n-0ulSSTftz28xM5dIM85qks_AuRG00Ac12rlzzfIQgg=s160-c-k-c0x00ffffff-no-rj` | binary body skipped |
| 38 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/FyhxH-QuEhM/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD_VrkyaH0HM88wXhZXZJokBlJzzw` | binary body skipped |
| 39 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/2K8mpX_kWN0/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLA7M00ue6zt2bdq82GqghfWi4iN4Q` | binary body skipped |
| 40 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/WceSGixAWSg/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD_KsONw1tv5epwaV1aYUn7eV03rg` | binary body skipped |
| 41 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/eLgCuf1wEuk/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDTUgWeKnbxkLIJI7Lo3q7ljmER3Q` | binary body skipped |
| 42 | `GET` | `fetch` | 301 | `https://youtube.com/` | body unavailable: Response.body: Response body is unavailable for redirect responses |
| 43 | `GET` | `fetch` |  | `https://www.youtube.com/` |  |
| 44 | `GET` | `image` | 204 | `https://www.youtube.com/generate_204?jei94g` | binary body skipped |
| 45 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/search/v15/24px.svg` | network/bodies/0045_fetch.svg |
| 46 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/menu/v1/24px.svg` | network/bodies/0046_fetch.svg |
| 47 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/yt-logo-updated/v3/24px.svg` | network/bodies/0047_fetch.svg |
| 48 | `POST` | `xhr` | 200 | `https://www.youtube.com/api/jnn/v1/GenerateIT` | network/bodies/0048_xhr.txt |
| 49 | `GET` | `script` | 200 | `https://www.youtube.com/s/player/74be5b62/player_es6.vflset/en_US/base.js` | network/bodies/0049_script.js |
| 50 | `GET` | `stylesheet` | 200 | `https://www.youtube.com/s/player/74be5b62/www-player.css` | network/bodies/0050_stylesheet.css |
| 51 | `POST` | `xhr` | 200 | `https://www.youtube.com/youtubei/v1/log_event?alt=json` | network/bodies/0051_xhr.json |
| 52 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/overflow_vertical/v13/24px.svg` | network/bodies/0052_fetch.svg |
| 53 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_outline/refresh/v1/24px.svg` | network/bodies/0053_fetch.svg |
| 54 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/chevron_down/v9/24px.svg` | network/bodies/0054_fetch.svg |
| 55 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/mic/v14/24px.svg` | network/bodies/0055_fetch.svg |
| 56 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/person_circle/v10/24px.svg` | network/bodies/0056_fetch.svg |
| 57 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/home/v10/24px.svg` | network/bodies/0057_fetch.svg |
| 58 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/shorts/v3/24px.svg` | network/bodies/0058_fetch.svg |
| 59 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/subscriptions/v12/24px.svg` | network/bodies/0059_fetch.svg |
| 60 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/history/v1/24px.svg` | network/bodies/0060_fetch.svg |
| 61 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/bag/v7/24px.svg` | network/bodies/0061_fetch.svg |
| 62 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/audio/v14/24px.svg` | network/bodies/0062_fetch.svg |
| 63 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/clapperboard/v3/24px.svg` | network/bodies/0063_fetch.svg |
| 64 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/chevron_up/v9/24px.svg` | network/bodies/0064_fetch.svg |
| 65 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/youtube_round/v2/24px.svg` | network/bodies/0065_fetch.svg |
| 66 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/unplugged_logo/v2/24px.svg` | network/bodies/0066_fetch.svg |
| 67 | `GET` | `script` | 200 | `https://www.youtube.com/s/_/ytmainappweb/_/js/k=ytmainappweb.kevlar_base.en_US.81_ruFHWKHQ.es5.O/am=AAAAIAAABAAJ/d=1/exm=kevlar_base_module,kevlar_base_sync_...` | network/bodies/0067_script.js |
| 68 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/youtube_music/v2/24px.svg` | network/bodies/0068_fetch.svg |
| 69 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/youtube_kids_round/v2/24px.svg` | network/bodies/0069_fetch.svg |
| 70 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/flag/v10/24px.svg` | network/bodies/0070_fetch.svg |
| 71 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/x/v11/24px.svg` | network/bodies/0071_fetch.svg |
| 72 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/location_pin/v2/24px.svg` | network/bodies/0072_fetch.svg |
| 73 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/add_circle/v6/24px.svg` | network/bodies/0073_fetch.svg |
| 74 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/add_circle/v6/24px.svg` | network/bodies/0074_fetch.svg |
| 75 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/alert_bubble/v2/24px.svg` | network/bodies/0075_fetch.svg |
| 76 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/audio/v14/24px.svg` | network/bodies/0076_fetch.svg |
| 77 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/bag/v7/24px.svg` | network/bodies/0077_fetch.svg |
| 78 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/bell/v11/24px.svg` | network/bodies/0078_fetch.svg |
| 79 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/bell/v11/24px.svg` | network/bodies/0079_fetch.svg |
| 80 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/clapperboard/v3/24px.svg` | network/bodies/0080_fetch.svg |
| 81 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/clock/v10/24px.svg` | network/bodies/0081_fetch.svg |
| 82 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/clock/v10/24px.svg` | network/bodies/0082_fetch.svg |
| 83 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/copy/v3/24px.svg` | network/bodies/0083_fetch.svg |
| 84 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/creator_studio_red_logo/v2/24px.svg` | network/bodies/0084_fetch.svg |
| 85 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/download/v11/24px.svg` | network/bodies/0085_fetch.svg |
| 86 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/fashion/v4/24px.svg` | network/bodies/0086_fetch.svg |
| 87 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/fashion/v4/24px.svg` | network/bodies/0087_fetch.svg |
| 88 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/flag/v10/24px.svg` | network/bodies/0088_fetch.svg |
| 89 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/gaming/v3/24px.svg` | network/bodies/0089_fetch.svg |
| 90 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/gaming/v3/24px.svg` | network/bodies/0090_fetch.svg |
| 91 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/gear/v10/24px.svg` | network/bodies/0091_fetch.svg |
| 92 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/gear/v10/24px.svg` | network/bodies/0092_fetch.svg |
| 93 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/help_circle/v2/24px.svg` | network/bodies/0093_fetch.svg |
| 94 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/home/v10/24px.svg` | network/bodies/0094_fetch.svg |
| 95 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/lightbulb/v4/24px.svg` | network/bodies/0095_fetch.svg |
| 96 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/lightbulb/v4/24px.svg` | network/bodies/0096_fetch.svg |
| 97 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/live/v3/24px.svg` | network/bodies/0097_fetch.svg |
| 98 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/mic/v14/24px.svg` | network/bodies/0098_fetch.svg |
| 99 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/news/v3/24px.svg` | network/bodies/0099_fetch.svg |
| 100 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/news/v3/24px.svg` | network/bodies/0100_fetch.svg |
| 101 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_fill/offline_no_content/v1/192px.svg` | network/bodies/0101_fetch.svg |
| 102 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/overflow_horizontal/v6/24px.svg` | network/bodies/0102_fetch.svg |
| 103 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/play_square_stack/v1/24px.svg` | network/bodies/0103_fetch.svg |
| 104 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/play_square_stack/v1/24px.svg` | network/bodies/0104_fetch.svg |
| 105 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/playlist/v5/24px.svg` | network/bodies/0105_fetch.svg |
| 106 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/podcast/v6/24px.svg` | network/bodies/0106_fetch.svg |
| 107 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/podcast/v6/24px.svg` | network/bodies/0107_fetch.svg |
| 108 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/search/v15/24px.svg` | network/bodies/0108_fetch.svg |
| 109 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/subscriptions/v12/24px.svg` | network/bodies/0109_fetch.svg |
| 110 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/thumb_up/v23/24px.svg` | network/bodies/0110_fetch.svg |
| 111 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/thumb_up/v23/24px.svg` | network/bodies/0111_fetch.svg |
| 112 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/trash_can/v10/24px.svg` | network/bodies/0112_fetch.svg |
| 113 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/trash_can/v10/24px.svg` | network/bodies/0113_fetch.svg |
| 114 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/trending/v2/24px.svg` | network/bodies/0114_fetch.svg |
| 115 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/trending/v2/24px.svg` | network/bodies/0115_fetch.svg |
| 116 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/trophy/v3/24px.svg` | network/bodies/0116_fetch.svg |
| 117 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/trophy/v3/24px.svg` | network/bodies/0117_fetch.svg |
| 118 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/video/v3/24px.svg` | network/bodies/0118_fetch.svg |
| 119 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/video/v3/24px.svg` | network/bodies/0119_fetch.svg |
| 120 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/video_camera_add/v2/24px.svg` | network/bodies/0120_fetch.svg |
| 121 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/youtube_shorts/v11/24px.svg` | network/bodies/0121_fetch.svg |
| 122 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/youtube_shorts/v11/24px.svg` | network/bodies/0122_fetch.svg |
| 123 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/arrow_down/v3/24px.svg` | network/bodies/0123_fetch.svg |
| 124 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/arrow_up/v3/24px.svg` | network/bodies/0124_fetch.svg |
| 125 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/pause/v9/24px.svg` | network/bodies/0125_fetch.svg |
| 126 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/play/v4/24px.svg` | network/bodies/0126_fetch.svg |
| 127 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/play/v4/24px.svg` | network/bodies/0127_fetch.svg |
| 128 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/share/v12/24px.svg` | network/bodies/0128_fetch.svg |
| 129 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/share/v12/24px.svg` | network/bodies/0129_fetch.svg |
| 130 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/text_bubble/v4/24px.svg` | network/bodies/0130_fetch.svg |
| 131 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/text_bubble/v4/24px.svg` | network/bodies/0131_fetch.svg |
| 132 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/thumb_down/v25/24px.svg` | network/bodies/0132_fetch.svg |
| 133 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/thumb_down/v25/24px.svg` | network/bodies/0133_fetch.svg |
| 134 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/volume_max/v2/24px.svg` | network/bodies/0134_fetch.svg |
| 135 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/volume_max/v2/24px.svg` | network/bodies/0135_fetch.svg |
| 136 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_fill_experimental/volume_mute/v2/24px.svg` | network/bodies/0136_fetch.svg |
| 137 | `GET` | `fetch` | 200 | `https://fonts.gstatic.com/s/i/youtube_outline_experimental/volume_mute/v2/24px.svg` | network/bodies/0137_fetch.svg |
| 138 | `GET` | `fetch` | 200 | `https://www.gstatic.com/youtube/img/icons/web/youtube_outline/waveform/v1/24px.svg` | network/bodies/0138_fetch.svg |
| 139 | `GET` | `script` | 200 | `https://www.youtube.com/s/_/ytmainappweb/_/js/k=ytmainappweb.kevlar_base.en_US.81_ruFHWKHQ.es5.O/am=AAAAIAAABAAJ/d=1/exm=De8mUc,QlbBce,kevlar_base_module,kev...` | network/bodies/0139_script.js |
| 140 | `GET` | `script` | 200 | `https://www.youtube.com/s/player/74be5b62/player_es6.vflset/en_US/offline.js` | network/bodies/0140_script.js |
| 141 | `GET` | `script` | 200 | `https://www.youtube.com/s/player/74be5b62/player_es6.vflset/en_US/remote.js` | network/bodies/0141_script.js |
| 142 | `GET` | `script` | 200 | `https://www.youtube.com/s/player/74be5b62/player_es6.vflset/en_US/miniplayer.js` | network/bodies/0142_script.js |
| 143 | `GET` | `script` | 200 | `https://www.gstatic.com/cv/js/sender/v1/cast_sender.js` | network/bodies/0143_script.js |
| 144 | `GET` | `script` | 200 | `https://static.doubleclick.net/instream/ad_status.js` | network/bodies/0144_script.js |
| 145 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/aQ7KfxQAKhs/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBKeothmuZS0EJsCCphM7343CnGlw` | binary body skipped |
| 146 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/iZUHXsAOW3o/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBbA0e8_60D4Yx1Zbwn4fU_avuqtA` | binary body skipped |
| 147 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/eQZlibAzUic/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCegC6IgCqTjj8jjNHrJBCMEZiV8A` | binary body skipped |
| 148 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/G5KBWseejYo/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCion5X40qPr0DxsRlNMMnIoSDJJg` | binary body skipped |
| 149 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/9BnWGmUdA5E/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB-jjN9JLtRi0XNwXB-0r7kBw_Kbg` | binary body skipped |
| 150 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/RL3H90V6mTY/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBnQlzAq92-IjJXBMYAyZDqAbpU8A` | binary body skipped |
| 151 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/dPow7Pd-tkc/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBwynLD7bHCqPXUTcmGXW6S588ZEA` | binary body skipped |
| 152 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/KIqkE8OYF6w/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAkzF1226Mh3VEg13ZHONtfq4CO5g` | binary body skipped |
| 153 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/gvYEQ4F_qp8/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDybvRtOSgYektNW0QujzcJRRnU8A` | binary body skipped |
| 154 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/tre6wc81XG8/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLC6ikGYJxBf5ML2Vzln7CtGW9Ey9A` | binary body skipped |
| 155 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/NEN1yRUZj5I/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBqk0jI6QCNF3EyF0Fiq5-MIn5yhQ` | binary body skipped |
| 156 | `GET` | `image` | 200 | `https://i.ytimg.com/vi/aZSkFL4ZXKk/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCq-4AovlNIsmWcugXG52uO9v6RVw` | binary body skipped |
