---
layout: page
title: 튜토리얼
---

## 1. 압축 파일 다운로드

[이 링크](https://example.com)에서 압축파일을 다운로드한 뒤, 압축을 푸세요.

## 2. 실행

실행하면, 다음과 같은 창을 볼 수 있습니다.

## 3. 코드 작성 & 실행

우선은 가장 간단하게, 랜덤한 위치에 블록을 놓는 예제를 보여 드리겠습니다.

```python
"""
random_blocks.py -- add randomly placed blocks in the world.

This script generates 1000 (default value) blocks in x, z range -50..50,
and y range 0..50.

"""

from craft_api import CraftAPI
import random

api = CraftAPI()
random.seed()

BLOCK_COUNT = 1000    # number of blocks to create
for _ in range(BLOCK_COUNT):
    x = random.randint(-50, 50)
    y = random.randint(0, 50)
    z = random.randint(-50, 50)
    texture = random.choice(['brick', 'sand', 'grass'])
    api.add_block((x, y, z), texture)
```

위 코드를 왼쪽에 있는 코드 편집기에 입력하세요 (복사&붙여넣기 하셔도 됩니다.)

그리고 나서 Run 버튼을 클릭하시면 오른쪽에 있는 Pycraft 창에서 아래 그림과 같이 코드가 실행되고, 결과가 화면에 보여지는 것을 알수 있습니다.
