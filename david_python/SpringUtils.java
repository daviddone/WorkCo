
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.DisposableBean;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.core.io.Resource;

public class SpringUtils implements ApplicationContextAware, DisposableBean {
    private static Logger logger = LoggerFactory.getLogger(SpringUtils.class);
    private static ApplicationContext applicationContext = null;

    public static ApplicationContext getApplicationContext() {
        assertContextInjected();
        return applicationContext;
    }

    public static <T> T getBean(String name) {
        assertContextInjected();
        return applicationContext.getBean(name);
    }

    public static <T> T getBean(Class<T> requiredType) {
        assertContextInjected();
        return applicationContext.getBean(requiredType);
    }

    public static void clearHolder() {
        if(logger.isDebugEnabled()) {
            logger.debug((new StringBuilder()).insert(0, MsgPushUtils.ALLATORIxDEMO("N\"h/\u007fnL>}\"d-l:d!c\rb y+u:7")).append(applicationContext).toString());
        }

        applicationContext = null;
    }


    public void setApplicationContext(ApplicationContext applicationContext) {
        if(applicationContext != null) {
            logger.info((new StringBuilder()).insert(0, MsgPushUtils.ALLATORIxDEMO("\u001d}<d j\rb y+u:E!a*h<丠益L>}\"d-l:d!c\rb y+u:袦览盛b-发朄\u000f}>a'n/y'b N!c:h6y乴7")).append(applicationContext).toString());
        }

        applicationContext = applicationContext;
    }

    public SpringUtils() {
    }

 
}
