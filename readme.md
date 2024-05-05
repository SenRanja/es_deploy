
# 部署方式

### step1 

    git clone https://gitee.com/bochen1993/es_deploy.git
    cd es_deploy
    git submodule update --init --recursive
    git submodule update --remote

git submodule update 的操作比较耗费时间，以gitee为例，俩子仓库都得输入密码，否则需要 rm -rf es_deploy 目录重新上述步骤部署。

### step2

进入ES_FRONT项目的vite.config.js所在目录，执行命令
    
    npm run build

进入 es_front 项目，修改`.env.production`中的`VITE_MEDIA_PREFIX_PATH='http://192.227.167.113/'`的URL地址，构建出的**dist**手动复制到服务器的 ~/es_deploy/es_front 目录。

### step3

    docker-compose build && docker-compose up -d

如果有报错，使用`docker-compose logs`查看报错




