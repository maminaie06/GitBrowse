# Network Log

این فایل خلاصه‌ی درخواست‌ها و پاسخ‌های ثبت‌شده توسط مرورگر است. جزئیات کامل در `network.json` و `network.jsonl` ذخیره شده است.

| # | Method | Type | Status | URL | Body |
|---:|---|---|---:|---|---|
| 1 | `GET` | `document` | 200 | `https://www.google.com/search?sa=X&sca_esv=fbcbad65759593ad&sxsrf=ANbL-n6iBngN6bxSrj5GDveqoYrizQwzZQ:1778557573496&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpmAsn...` | body unavailable: Response.body: Protocol error (Network.getResponseBody): No resource with given identifier found |
| 2 | `GET` | `document` | 302 | `https://www.google.com/search?sa=X&sca_esv=fbcbad65759593ad&sxsrf=ANbL-n6iBngN6bxSrj5GDveqoYrizQwzZQ:1778557573496&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpmAsn...` | body unavailable: Response.body: Response body is unavailable for redirect responses |
| 3 | `GET` | `document` | 429 | `https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fsa%3DX%26sca_esv%3Dfbcbad65759593ad%26sxsrf%3DANbL-n6iBngN6bxSrj5GDveqoYrizQwzZQ:...` | network/bodies/0003_document.html |
| 4 | `GET` | `script` | 200 | `https://www.google.com/recaptcha/enterprise.js` | network/bodies/0004_script.js |
| 5 | `GET` | `script` | 200 | `https://www.gstatic.com/recaptcha/releases/U5VsmTDhJM1iOJUyw4DEUTYv/recaptcha__en.js` | network/bodies/0005_script.js |
| 6 | `GET` | `document` | 200 | `https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&co=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbTo0NDM.&hl=en&v=U5VsmTDhJM...` | network/bodies/0006_document.html |
| 7 | `GET` | `stylesheet` | 200 | `https://www.gstatic.com/recaptcha/releases/U5VsmTDhJM1iOJUyw4DEUTYv/styles__ltr.css` | network/bodies/0007_stylesheet.css |
| 8 | `GET` | `script` | 200 | `https://www.gstatic.com/recaptcha/releases/U5VsmTDhJM1iOJUyw4DEUTYv/recaptcha__en.js` | network/bodies/0008_script.js |
| 9 | `GET` | `script` | 200 | `https://www.google.com/recaptcha/enterprise/webworker.js?hl=en&v=U5VsmTDhJM1iOJUyw4DEUTYv` | network/bodies/0009_script.js |
| 10 | `GET` | `image` | 200 | `https://www.gstatic.com/recaptcha/api2/logo_48.png` | binary body skipped |
| 11 | `GET` | `font` | 200 | `https://fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2` | binary body skipped |
| 12 | `GET` | `other` | 200 | `https://www.gstatic.com/recaptcha/releases/U5VsmTDhJM1iOJUyw4DEUTYv/recaptcha__en.js` | network/bodies/0012_other.js |
| 13 | `GET` | `document` | 200 | `https://www.google.com/recaptcha/enterprise/bframe?hl=en&v=U5VsmTDhJM1iOJUyw4DEUTYv&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&bft=0dAFcWeA7P_ryed6zgn0IeDS1k...` | network/bodies/0013_document.html |
| 14 | `GET` | `stylesheet` | 200 | `https://www.gstatic.com/recaptcha/releases/U5VsmTDhJM1iOJUyw4DEUTYv/styles__ltr.css` | network/bodies/0014_stylesheet.css |
| 15 | `GET` | `script` | 200 | `https://www.gstatic.com/recaptcha/releases/U5VsmTDhJM1iOJUyw4DEUTYv/recaptcha__en.js` | network/bodies/0015_script.js |
| 16 | `GET` | `font` | 200 | `https://fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2` | binary body skipped |
