#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from testcontainers.core.generic import GenericDbContainer


class MySqlContainer(GenericDbContainer):
    _super_user_name = "root"

    def __init__(self, user,
                 password,
                 root_password="secret",
                 db="test",
                 host_port=3306,
                 image_name="mysql",
                 version="latest"):
        super(MySqlContainer, self).__init__(image_name=image_name,
                                             version=version,
                                             host_port=host_port,
                                             user=user,
                                             password=password,
                                             database=db,
                                             root_password=root_password, name=image_name)
        self.container_port = 3306
        self._configure()

    def _configure(self):
        if not self._is_root():
            self.add_env("MYSQL_USER", self.username)
            self.add_env("MYSQL_PASSWORD", self.password)
        self.add_env("MYSQL_ROOT_PASSWORD", self.root_password)
        self.add_env("MYSQL_DATABASE", self.database)
        self.bind_ports(self.host_port, self.container_port)

    def _is_root(self):
        return self.username == self._super_user_name
