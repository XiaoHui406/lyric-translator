import httpx


class ZhipuWebSearchManager:
    def __init__(
        self,
        apikey: str
    ) -> None:
        self.apikey: str = apikey

    async def search(
        self,
        content: str,
        search_count: int = 10
    ):
        async with httpx.AsyncClient() as client:
            search_result = await client.post(
                url='https://open.bigmodel.cn/api/paas/v4/web_search',
                headers={
                    "Authorization": f"Bearer {self.apikey}",
                    "Content-Type": "application/json"
                },
                json={
                    "search_engine": "search-std",
                    "search_intent": False,
                    "search_query": content,
                    "count": search_count
                }
            )
        return search_result.json()
