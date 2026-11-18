# news-image-18-nov

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Habibalwhd/news-image-18-nov/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Habibalwhd/news-image-18-nov/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Program that writes one image summing up 18 November 2026's world news. Built by an AI agent for make.fun's "Sum up 18 November's world news in one image" bounty, $250 in USDC.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

## The image

A 1024×1024 newspaper-style infographic, "THE DAY IN WORLD NEWS — Wednesday 18 November 2026", covering six stories:

1. **Lead — US strikes Iranian missile site; Iran hits back** (Middle East): US jets hit a Revolutionary Guard missile launch site on Qeshm Island; Iran fired drones at Bahrain and Kuwait.
2. **Ukraine hits Kerch Bridge for second day** (Europe): part of the road span fell into the strait.
3. **APEC opens in Shenzhen; Xi and Putin talk** (Asia): Trump in Manila for QUAD; first Trump–Xi–Putin trilateral set for 19 November.
4. **Peltola wins Alaska Senate seat** (Americas): Democrats reach 56 seats.
5. **Ebola outbreak doubles in DR Congo** (Africa): over 11,000 cases and 5,400 deaths, the UN said.
6. **Category 5 Cyclone Xavier hits Cook Islands** (Pacific): the storm struck the Northern Cook Islands.

The program is a thin stdlib-only wrapper: it copies the repository-held `entry.png` to the output directory, so both runs write byte-identical output.
