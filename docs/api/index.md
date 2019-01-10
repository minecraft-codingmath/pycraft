---

layout: page

title: API 

---

## API 초기화

```python
from craft_api import CraftAPI
api = CraftAPI()
```

## 블록 추가

```python
api.add_block((x, y, z), texture)
```

## 블록 삭제

```python
api.delete_block((x, y, z))
```


