# tempNotes
for record something

## 基于goose的rabbitmq-rpc服务

需求：
1. 本地使用工程获取url，提供给rabbitmq，使用rabbitmq中的rpc服务将url交给远程goose工程进行处理<br />
2. 使用gevent,在io等待时候继续获取url并交给goose抓取<br />
3. 工厂模式，可横向扩展<br />

do()<br />
step 1. 封装goose 提供获取url的接口 [goose](https://github.com/grangier/python-goose)<br />
step 2. <br />


