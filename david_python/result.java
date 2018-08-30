/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.session.Session;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * Simple Quickstart application showing how to use Shiro's API.
 *
 * @since 0.9 RC2
 */
public class Quickstart {

    private static final transient Logger log = LoggerFactory.getLogger(Quickstart.class);


    public static void main(String[] args) {

        // The easiest way to create a Shiro SecurityManager with configured
        //创建配置的Shiro SecurityManager的最简单方法
        // realms, users, roles and permissions is to use the simple INI config.
        //领域，用户，角色和权限是使用简单的INI配置。
        // We'll do that by using a factory that can ingest a .ini file and
        //我们将通过使用可以提取.ini文件的工厂来实现这一点
        // return a SecurityManager instance:
        //返回一个SecurityManager实例：

        // Use the shiro.ini file at the root of the classpath
        //在类路径的根目录中使用shiro.ini文件
        // (file: and url: prefixes load from files and urls respectively):
        //（文件：和url：前缀分别从文件和网址加载）：
        Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro.ini");
        SecurityManager securityManager = factory.getInstance();

        // for this simple example quickstart, make the SecurityManager
        // 对于这个简单的示例快速入门，请创建SecurityManager 
        // accessible as a JVM singleton.  Most applications wouldn't do this
        //可作为JVM单例访问。
        // and instead rely on their container configuration or web.xml for
        //而是依赖于他们的容器配置或web.xml 
        // webapps.  That is outside the scope of this simple quickstart, so
        // webapps。
        // we'll just do the bare minimum so you can continue to get a feel
        //我们会尽量做到最小，这样你就可以继续感受一下
        // for things.
        // 为了这些事。
        SecurityUtils.setSecurityManager(securityManager);

        // Now that a simple Shiro environment is set up, let's see what you can do:
        //现在设置了一个简单的Shiro环境，让我们看看你能做些什么：

        // get the currently executing user:
        //获取当前正在执行的用户：
        Subject currentUser = SecurityUtils.getSubject();

        // Do some stuff with a Session (no need for a web or EJB container!!!)
        //用Session做一些事情（不需要web或EJB容器!!!）
        Session session = currentUser.getSession();
        session.setAttribute("someKey", "aValue");
        String value = (String) session.getAttribute("someKey");
        if (value.equals("aValue")) {
            log.info("Retrieved the correct value! [" + value + "]");
        }

        // let's login the current user so we can check against roles and permissions:
        //让我们登录当前用户，这样我们就可以检查角色和权限：
        if (!currentUser.isAuthenticated()) {
            UsernamePasswordToken token = new UsernamePasswordToken("lonestarr", "vespa");
            token.setRememberMe(true);
            try {
                currentUser.login(token);
            } catch (UnknownAccountException uae) {
                log.info("There is no user with username of " + token.getPrincipal());
            } catch (IncorrectCredentialsException ice) {
                log.info("Password for account " + token.getPrincipal() + " was incorrect!");
            } catch (LockedAccountException lae) {
                log.info("The account for username " + token.getPrincipal() + " is locked.  " +
                        "Please contact your administrator to unlock it.");
            }
            // ... catch more exceptions here (maybe custom ones specific to your application?
            // ...在这里捕获更多例外（也许是特定于您的应用程序的自定义？
            catch (AuthenticationException ae) {
                //unexpected condition?  error?
                //意外情况？
            }
        }

        //say who they are:
        //说出他们是谁：
        //print their identifying principal (in this case, a username):
        //打印他们的识别主体（在这种情况下，用户名）：
        log.info("User [" + currentUser.getPrincipal() + "] logged in successfully.");

        //test a role:
        //测试一个角色：
        if (currentUser.hasRole("schwartz")) {
            log.info("May the Schwartz be with you!");
        } else {
            log.info("Hello, mere mortal.");
        }

        //test a typed permission (not instance-level)
        //测试类型化的权限（不是实例级别）
        if (currentUser.isPermitted("lightsaber:weild")) {
            log.info("You may use a lightsaber ring.  Use it wisely.");
        } else {
            log.info("Sorry, lightsaber rings are for schwartz masters only.");
        }

        //a (very powerful) Instance Level permission:
        //一个（非常强大的）实例级别权限：
        if (currentUser.isPermitted("winnebago:drive:eagle5")) {
            log.info("You are permitted to 'drive' the winnebago with license plate (id) 'eagle5'.  " +
                    "Here are the keys - have fun!");
        } else {
            log.info("Sorry, you aren't allowed to drive the 'eagle5' winnebago!");
        }

        //all done - log out!
        //全部完成 - 退出！
        currentUser.logout();

        System.exit(0);
    }
}
