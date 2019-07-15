import requests
import json


def make_request(method, user_id, access_token):
	full_url = 'https://api.vk.com/method/' + method + '?user_id=' + user_id + '&v=5.52' + '&access_token=' + access_token + '&fields=city'
	return requests.get(full_url).json()

class VkUser():
	def __init__(self, user_id, token):
		self.token = token
		self.user_id = user_id
		api_response = make_request('users.get', self.user_id,self.token)
		if 'error' not in api_response.keys():
			self.first_name = api_response['response'][0]['first_name']
			self.last_name = api_response['response'][0]['last_name']
			self.friends = make_request('friends.get', self.user_id, self.token)
		else:
			self.first_name = api_response
			self.last_name = api_response
			self.friends = api_response

	def friend_list_table(self):
		if 'response' in self.friends.keys():
				fr_list = []
				for user in self.friends['response']['items']:
					print('Id: ', user['id'],'last_name: ', user['last_name'])
		else :
			print('Error get friends:', self.friends)

	def get_mutual(self, target_user):
		self.target_user = target_user
		full_url = 'https://api.vk.com/method/friends.getMutual' + '?source_uid=' + self.user_id + '&target_uid=' + self.target_user + '&v=5.52' + '&access_token=' + self.token
		return requests.get(full_url).json()

	def friend_list(self):
		fr_list = []
		if 'response' in self.friends.keys():
				for user in self.friends['response']['items']:
					fr_list.append(user['first_name'] + '_' + user['last_name'])
		else :
			fr_list.append(self.friends)
		return fr_list

token = input('Введите токен: ')


petrenko = VkUser('552646270',token)
belousova = VkUser('552646270', token)


print('Petrenko and bel mutual:', petrenko.get_mutual(bel.user_id))
