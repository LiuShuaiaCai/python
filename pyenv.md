# pyenv + virtualenv 的学习笔记

#### pyenv 和 virtualenv 的作用
* pyenv 是针对python版本的管理，是通过修改环境变量的方式来实现。
* virtualenv 是对python包的管理，通过创建不同的文件夹来作为包的虚拟环境。

#### 安装pyenv
* 1、自动安装（没实验）

	pyenv 提供了自动安装的工具，执行命令安装即可：

	    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

	保证系统有 git ，否则需要新安装git工具。

* 2、手动安装（本次使用）

	+ 下载：[git clone git://github.com/yyuu/pyenv.git .pyenv](git clone git://github.com/yyuu/pyenv.git .pyenv)
	+ 添加环境变量
		- PYENV_ROOT指向pyenv检出的根目录
		- 向$PATH添加$PYENV_ROOT/bin提供访问pyenv的访问路径。
		```shell
		[root@iZ2zee30op42zedrik59weZ ~]# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
		[root@iZ2zee30op42zedrik59weZ ~]# echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
		```
