# pyenv + virtualenv 的学习笔记

#### pyenv 和 virtualenv 的作用
* pyenv 是针对python版本的管理，是通过修改环境变量的方式来实现。
* virtualenv 是对python包的管理，通过创建不同的文件夹来作为包的虚拟环境。

#### 安装pyenv
* 1、自动安装（推荐）

	pyenv 提供了自动安装的工具，执行命令安装即可：

	    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

	保证系统有 git ，否则需要新安装git工具。
	会安装到~/.pyenv目录中，修改~/.bashrc文件。
	```shell
	export PYENV_ROOT="${HOME}/.pyenv"

	if [ -d "${PYENV_ROOT}" ]; then
	  export PATH="${PYENV_ROOT}/bin:${PATH}"
	  eval "$(pyenv init -)"
	fi
	```

* 2、手动安装

	+ 下载：git clone [git://github.com/yyuu/pyenv.git .pyenv](git://github.com/yyuu/pyenv.git .pyenv)
	+ 添加环境变量
		- PYENV_ROOT指向pyenv检出的根目录
		```shell
		[root@iZ2zee30op42zedrik59weZ ~]# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
		```
		- 向$PATH添加$PYENV_ROOT/bin提供访问pyenv的访问路径。
		```shell
		[root@iZ2zee30op42zedrik59weZ ~]# echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
		```
		- 向shell添加pyenv init以启用shims和命令补全功能
		```shell
		[root@iZ2zee30op42zedrik59weZ ~]# echo 'eval"$(pyenv init -)"' >> ~/.bash_profile
		```
		- 执行以下命令使其生效
		```shell
		[root@iZ2zee30op42zedrik59weZ ~]# source ~/.bash_profile
		```

* pyenv常用命令
	
	+ 查看pyenv中可安装的python版本
	```shell
	[root@iZ2zee30op42zedrik59weZ ~]# pyenv install --list
	Available versions:
	  2.1.3
	  2.2.3
	  2.3.7
	```
	+ 安装python 3.6.1
	```shell
	[root@iZ2zee30op42zedrik59weZ ~]# pyenv install 3.6.1
	```
	+ 查看安装的python版本
	```shell
	(pyenv) [root@iZ2zee30op42zedrik59weZ pyenv]# pyenv versions
	* system (set by /root/.pyenv/version)
		2.7.12
		3.6.1
	```
	+ 切换python版本(注意*号)

	有三种切换方式：shell、local、global;优先级：shell>local>global
	```python
	(pyenv) [root@iZ2zee30op42zedrik59weZ pyenv]# pyenv global 3.6.1 
	(pyenv) [root@iZ2zee30op42zedrik59weZ pyenv]# pyenv versions
	  system
	  2.7.12
	* 3.6.1 (set by /root/.pyenv/version)
	```
	+ 卸载某个版本的python
	```shell
	[root@iZ2zee30op42zedrik59weZ pyenv]# pyenv uninstall 2.7.12 
	```
* pyenv-virtualenv插件

	+ 在采用自动安装pyenv后，插件已经自动安装。如果是手动安装，先下载pyenv-virtualenv插件,下载到~/.pyenv/plugins/目录
	```shell
	git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
	```
	```shell
	[root@iZ2zee30op42zedrik59weZ plugins]# ll
	total 24
	drwxr-xr-x 4 root root 4096 Jul  9 10:53 pyenv-doctor
	drwxr-xr-x 5 root root 4096 Jul  9 10:53 pyenv-installer
	drwxr-xr-x 4 root root 4096 Jul  9 10:53 pyenv-update
	drwxr-xr-x 7 root root 4096 Jul  9 10:55 pyenv-virtualenv
	drwxr-xr-x 4 root root 4096 Jul  9 10:53 pyenv-which-ext
	drwxr-xr-x 5 root root 4096 Jul  8 13:10 python-build
	```
	+ 创建一个虚拟的干净的环境
	```shell
	[root@iZ2zee30op42zedrik59weZ pyenv]# pyenv virtualenv 2.7.12 env2.7
	[root@iZ2zee30op42zedrik59weZ pyenv]# pyenv versions
	  system
	  2.7.12
	  2.7.12/envs/env2.7
	* 3.6.1 (set by /root/.pyenv/version)
	  env2.7		## 多了一个env2.7环境
	```
	+ 切换到虚拟的环境
	```shell
	[root@iZ2zee30op42zedrik59weZ ~]# pyenv activate env2.7 
	pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
	(env2.7) [root@iZ2zee30op42zedrik59weZ ~]# 
	```
	+ 退出虚拟的环境
	```shell
	(env2.7) [root@iZ2zee30op42zedrik59weZ ~]# pyenv deactivate 
	[root@iZ2zee30op42zedrik59weZ ~]# 
	```
