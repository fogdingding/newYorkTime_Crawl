sudo apt-get update
sudo apt-get upgrade
sudo apt-get install docker.io
sudo docker images
sudo docker search ubuntu
sudo docker pull ubuntu
sudo docker run -it ubuntu /bin/bash
root# apt-get install python3
root# apt-get install python3-pip
root# pip3 install -r requirements.txt


----docker
指令縮寫
https://www.jinnsblog.com/2018/10/docker-container-command.html
run
	* -i
		標準輸入維持在打開的狀態
	* -t
		替Container配置一個虛擬的終端機
	* -d
		背景執行
	* -p
		port綁定
	* -v
		掛載目錄，達到共享
rm
	* 砍 container
rmi
	* 砍 image
hub
	* docker tag <Image Name> <docker_hub_帳號>/<docker_hub_名稱>
	* docker push <docker_hub_帳號>/<docker_hub_名稱>
----
sudo docker run -itd ubuntu /bin/bash
#有時候，images 會砍不掉，可能是因為還有映像檔案存在(相依)，所以用下列指令來觀看)
sudo docker ps -a
sudo docker exec -it <container_id> /bin/bash

#如果要存檔的話
docker export <container_id> > <name.tar>

#如果因為sudo docker load < ubuntu.tar 抱錯，JSON問題，請使用下列。
sudo cat ubuntu_export.tar | sudo docker import - ubuntu_export