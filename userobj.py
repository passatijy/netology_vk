import requests
import json


def make_request(method, user_id, access_token):
	full_url = 'https://api.vk.com/method/' + method + '?user_id=' + user_id + '&v=5.52' + '&access_token=' + access_token + '&fields=city'
	return requests.get(full_url).json()

def friend_list(friends_dict):
	fr_list = []
	if 'response' in friends_dict.keys():
			for user in friends_dict['response']['items']:
				fr_list.append(user['first_name'] + '_' + user['last_name'])
	else :
		fr_list.append(friends_dict)
	return fr_list

def get_mutual(src_user, target_user, access_token):
	full_url = 'https://api.vk.com/method/get_mutual' + '?source_uid=' + src_user + '&target_uid=' + target_user + '&v=5.52' + '&access_token=' + access_token

def friend_list_table(friends_dict):
	if 'response' in friends_dict.keys():
			fr_list = []
			for user in friends_dict['response']['items']:
				print('Id: ', user['id'],'last_name: ', user['last_name'])
	else :
		print('Error get friends:', friends_dict)




class VkUser():
	def __init__(self, user_id, token):
		self.token = token
		self.user_id = user_id
		self.first_name = make_request('users.get', self.user_id,self.token)['response'][0]['first_name']
		self.last_name = make_request('users.get', self.user_id,self.token)['response'][0]['last_name']
		self.friends = make_request('friends.get', self.user_id,self.token)
	def get_name():
		pass
	def get_friends():
		pass



print('Korol and sidor mutual: ',get_mutual('547233513', '550885673', token))
print('Smir and pon mutual: ', get_mutual('550886021', '551160869', token))
print('petren and bel mutual: ', get_mutual('552610377', '552646270', token))
print('pug and cherne mutual: ', get_mutual('552748481', '552762252', token))
