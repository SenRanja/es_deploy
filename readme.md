
# 部署方式

### step1 

    git clone https://gitee.com/bochen1993/es_deploy.git
    cd es_deploy
    git submodule update --init --recursive
    git submodule update --remote

git submodule update 的操作比较耗费时间，以gitee为例，俩子仓库都得输入密码，否则需要 rm -rf es_deploy 目录重新上述步骤部署。

### step2

此步修改前端的API访问地址。

此步需要本机安装nodejs的编译环境，参考`https://nodejs.org/en/download/prebuilt-installer`。开发者本人的环境如下， 如果安装nodejs及npm，建议安装贴近版本。

    C:\Users\ranja>node -v
    v16.13.2

    C:\Users\ranja>npm -v
    8.1.2

进入 es_front 项目，修改`.env.production`中的`VITE_MEDIA_PREFIX_PATH='http://192.227.167.113/'`的URL地址（如访问 `http://192.227.167.113/`），改为客户需要被访问的IP地址。

本地（非服务器）进入ES_FRONT项目的vite.config.js所在目录，执行命令
    
    npm run build

构建出的**dist**手动复制到服务器的 ~/es_deploy/es_front 目录。

### step3

    docker-compose build && docker-compose up -d

如果有报错，使用`docker-compose logs`查看报错

### 移除镜像(希望重新构建前必须操作步骤)

    docker-compose down


