# 导入logging
import logging

# 设置配置信息
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

# 定义日志名称getlogger
logger = logging.getLogger("log_demo")

# info debug
logger.info("info")
logger.debug("debug")
logger.warning("warning")