# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class AddMediaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'AddMedia','mts')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OverrideParams(self):
		return self.get_query_params().get('OverrideParams')

	def set_OverrideParams(self,OverrideParams):
		self.add_query_param('OverrideParams',OverrideParams)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_InputUnbind(self):
		return self.get_query_params().get('InputUnbind')

	def set_InputUnbind(self,InputUnbind):
		self.add_query_param('InputUnbind',InputUnbind)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_CoverURL(self):
		return self.get_query_params().get('CoverURL')

	def set_CoverURL(self,CoverURL):
		self.add_query_param('CoverURL',CoverURL)

	def get_CateId(self):
		return self.get_query_params().get('CateId')

	def set_CateId(self,CateId):
		self.add_query_param('CateId',CateId)

	def get_FileURL(self):
		return self.get_query_params().get('FileURL')

	def set_FileURL(self,FileURL):
		self.add_query_param('FileURL',FileURL)

	def get_MediaWorkflowId(self):
		return self.get_query_params().get('MediaWorkflowId')

	def set_MediaWorkflowId(self,MediaWorkflowId):
		self.add_query_param('MediaWorkflowId',MediaWorkflowId)

	def get_MediaWorkflowUserData(self):
		return self.get_query_params().get('MediaWorkflowUserData')

	def set_MediaWorkflowUserData(self,MediaWorkflowUserData):
		self.add_query_param('MediaWorkflowUserData',MediaWorkflowUserData)