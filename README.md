### Шаг 1. Подготовка среды.
-  Скачиваем необходимые дистрибутивы программ:

Для Debian-подобных систем:
```
Debians-arch: # sudo apt update && sudo apt install maven && sudo apt install openjdk-8-jdk
```
[Установка Tomcat](https://www.digitalocean.com/community/tutorials/install-tomcat-9-ubuntu-1804-ru)

Для RedHat-подобных систем
```        
# sudo yum update && sudo yum install maven && sudo yum java-1.8.0-openjdk-devel
```
[Установка Tomcat](https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-8-on-centos-7)

### Шаг 2. Билд и деплой проекта.
- Скачиваем проект с репозитория GitLab:
```
cd /opt
git clone http://oz.it-alnc.ru:7088/root/smp-mortgage.git
cd smp-mortage/
mkdir mortage-ui/lib
mvn clean install
```
- Редактируем файл /opt/tomcat/conf/server.xml
```
<GlobalNamingResources>
    <Resource auth="Container" description="User database that can be updated and saved" factory="org.apache.catalina.users.MemoryUserDatabaseFactory" name="UserDatabase" pathname="conf/tomcat-users.xml" type="org.apache.catalina.UserDatabase"/>
    <Resource acquireIncrement="1" auth="Container" driverClass="oracle.jdbc.OracleDriver" factory="org.apache.naming.factory.BeanFactory" idleConnectionTestPeriod="300" jdbcUrl="jdbc:oracle:thin:@//192.168.0.3:1522/pcat.it-alnc.ru" maxIdleTimeExcessConnections="240" maxPoolSize="3" minPoolSize="1" name="jdbc/bo" password="bo" testConnectionOnCheckin="true" type="com.mchange.v2.c3p0.ComboPooledDataSource" user="bo"/>
    <Resource acquireIncrement="1" auth="Container" driverClass="com.microsoft.sqlserver.jdbc.SQLServerDriver" factory="org.apache.naming.factory.BeanFactory" idleConnectionTestPeriod="300" jdbcUrl="jdbc:sqlserver://192.168.0.7:1433;databaseName=MORTGAGE" maxIdleTimeExcessConnections="240" maxPoolSize="3" minPoolSize="1" name="jdbc/mortgage" password="mortgage" testConnectionOnCheckin="true" type="com.mchange.v2.c3p0.ComboPooledDataSource" user="mortgage"/> 
    <Resource acquireIncrement="1" auth="Container" driverClass="com.microsoft.sqlserver.jdbc.SQLServerDriver" factory="org.apache.naming.factory.BeanFactory" idleConnectionTestPeriod="300" jdbcUrl="jdbc:sqlserver://192.168.0.7:1433;databaseName=BPMOnline770_181218_anonymous" maxIdleTimeExcessConnections="240" maxPoolSize="3" minPoolSize="1" name="jdbc/crm" password="sa" testConnectionOnCheckin="true" type="com.mchange.v2.c3p0.ComboPooledDataSource" user="sa"/> 
    <Environment name="bo/mortgage/path" override="true" type="java.lang.String" value="/Users/parmn/git/smp-mortgage/boclasses"/>
  </GlobalNamingResources>
```
- Редактируем файл /opt/tomcat/conf/tomcat_users.xml

```
<role rolename="mortgage-admin"/>
<user username="admin" password="admin" roles="mortgage-admin"/>
```
- Перезапускаем TomCat:
```
sudo systemctl restart tomcat
```

### Шаг 3. Запуск проекта.
Переходим по адресу:
```
http://localhost:8180
```
- Заходим в - ManagerApp
- Внизу раздел - WAR file to deploy
- Выбераем наш War-файл из директории проекта: /opt/smp-mortage/mortage-ui/target/*.war
- Нажимаем Deploy
- Наверху, в разделе Applications, должен появиться проект - mortage/, нажимаем на него или переходим по:
```
http://localhost:8180/mortgage/itaforms
```
- Вход в админку: admin/admin
