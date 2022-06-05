from requests import get


class CheapShark:
	def __init__(self):
		self.api = "https://www.cheapshark.com/api/1.0"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36",
			"Content-Type": "application/json",
			"Connection": "keep-alive"}
	
	def get_deals_list(
			self,
			store_id: str = "1",
			page_number: int = 0,
			page_size: int = 60,
			sort: str = "Deal Rating", 
			desc: int = 0,
			lower_price: int = 0,
			upper_price: int = 15,
			metacritic: int = None,
			steam_rating: int = None,
			steam_app_id: str = None,
			title: str = None,
			exact: int = 0,
			AAA: int = 0,
			steam_works: int = 0,
			on_sale: int = 0,
			output: str = None):
	url = f"{self.api}/deals?storeID={store_id}&pageNumber={page_number}&pageSize={page_size}&sortBy={sort}&desc={desc}&lowerPrice={lower_price}&upperPrice={upper_price}&exact={exact}&AAA={AAA}&steamworks=(steam_works}&onSale={on_sale}"
	if metacritic:
		url += f"&metacritic={metacritic}"
	if steam_rating:
		url += f"&steamRating={steam_rating}"
	if steam_app_id:
		url += f"&steamAppID={steam_app_id}"
	if title:
		url += f"&title={title}"
	if output:
		url += f"&output={output}"
	return get(url, headers=self.headers).json()

	def deal_lookup(self, deal_id: str):
		return get(
			f"{self.api}/deals?id={deal_id}", headers=self.headers).json()
	
	def get_games_list(
		self,
		title: str,
		steam_app_id: int,
		limit: int = 60,
		exact: int = 0):
	return get(
		f"{self.api}/games?title={title}&steamAppID={steam_app_id}&limit={limit}&exact={exact}",
		headers=self.headers).json()
	
	def game_lookup(self, game_id: int):
		return get(
			f"{self.api}/games?id={game_id}", headers=self.headers).json()
	
	def games_lookup(self, game_ids: str = "128,129,130"):
		return get(
			f"{self.api}/games?ids={game_ids}", headers=self.headers).json()
	
	def get_stores_list(self):
		return get(f"{self.api}/stores", headers=self.headers).json()
	
	def edit_alert(
			self,
			action: str,
			email: str,
			game_id: int,
			price: str):
	return get(
		f"{self.api}/alerts?action={action}&email={email}&gameID={game_id}&price={price}",
		headers=self.headers).json()
	
	def manage_alerts(self, action: str, email: str):
		return get(
			f"{self.api}/alerts?action={action}&email={email}",
			headers=self.headers).json()
