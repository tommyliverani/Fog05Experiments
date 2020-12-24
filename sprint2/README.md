# Sprint1

Deployment of a docker container that print **_hello world!_**

## Requirements

Having a fog05 node visible in local with 3 plugins available:
* plugin-fdu-ctd
* plugin-net-linuxbridge
* plugin-os-linux

## Tips

* Go to **fog05/plugins** to install a plugin
* `systemctl status <fos_linux,fos_linuxbridge,fos_ctd>` to check if a service is active and check the logs
* `sudo systemctl start <fos_linux,fos_linuxbridge,fos_ctd>` to start a service
* [listNode](https://github.com/tommyliverani/Fog05Experiments/blob/main/utils/listNode.py) to check the available nodes id and their plugins

**_NB:_** The id of each plugin can be found in his json file

## Using

* Change the variable **_n_** with your node id
* call: `python3 deploy.py`
